# -*- coding: utf-8 -*-
import sys
import os

# Add parent directory to Python path to allow imports from utils
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import copy
import torch
from accelerate import Accelerator
from torch.utils.data import DataLoader
import transformers
from transformers import BertConfig, BertForMaskedLM, PreTrainedTokenizerFast # type: ignore
import random
from tqdm import tqdm
import numpy as np
import evaluate
import pickle
import datetime

# Import from local modules
from utils.dataset import Dataset
from config import config, model_config

if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    # Setup accelerator (for device placement)
    accelerator = Accelerator()
    print(f"Device: {accelerator.device}")

    # Load configuration
    print("Loading configuration from config.py...")
    # Using the same config as training to ensure consistency
    
    print("Loading data...")
    with open(config["plans"], 'rb') as f:
        plans = pickle.load(f)
        
    # Shuffle plans randomly using SAME seed as training to reproduce splits
    random.seed(10)
    random.shuffle(plans)
    
    # Replicate data processing from training.py
    piani = []
    piani_mask = []
    
    # NOTE: Training script limits to 100 plans. Replicating this here.
    for p in plans[:10]:
        azioni = [a.name.lower().strip() for a in p.actions]
        
        # Mask 33% of actions (same logic as training)
        azioni_spezzate = []
        for a in azioni:
            azioni_spezzate += a.split()
            
        mask = random.sample(range(0, len(azioni_spezzate)), round(len(azioni_spezzate) * 0.33))
        azioni_masked = copy.deepcopy(azioni_spezzate)
        for i in mask:
            azioni_masked[i] = "[MASK]"
        
        initial_state = [a.lower().strip() for a in p.initial_state]
        goal = [a.lower().strip() for a in p.goals]
        
        piano = "[SI] " + " ".join(initial_state) + " [SG] " + " ".join(goal) + " [A] " + " ".join(azioni_spezzate)
        piano_masked = "[SI] " + " ".join(initial_state) + " [SG] " + " ".join(goal) + " [A] " + " ".join(azioni_masked)
        
        piani.append(piano)
        piani_mask.append(piano_masked)
            
    # Split dataset in train and validation (same logic as training)
    # We only care about validation/test here
    validation = piani[-config["num_val"]:]
    validation_mask = piani_mask[-config["num_val"]:]
    
    print(f"Validation set size: {len(validation)}")

    print("Loading tokenizer...")
    tokenizer = PreTrainedTokenizerFast.from_pretrained(config["tokenizer_path"])
    print("Tokenizer loaded.")
  
    print("Masking data and creating dataset...")
    
    # Tokenize validation data
    batch_val = tokenizer(validation, max_length=config['max_length'], padding='max_length', truncation=True)
    batch_mask_val = tokenizer(validation_mask, max_length=config['max_length'], padding='max_length', truncation=True)
    
    labels_val = torch.tensor([x for x in batch_val["input_ids"]])
    input_ids_val = torch.tensor([x for x in batch_mask_val["input_ids"]])
    mask_val = torch.tensor([x for x in batch_val["attention_mask"]])

    # Set -100 the logits in labels where is padding  
    for i in range(input_ids_val.shape[0]):
        labels_val[i][mask_val[i]==0] = -100
    
    # Build dataset
    encodings_val = {'input_ids': input_ids_val, 'attention_mask': mask_val, 'labels': labels_val}
    dataset_val = Dataset(encodings_val)

    # Validate loader
    val_loader = DataLoader(
        dataset_val, 
        batch_size=config["batch_size"], 
        shuffle=False,  # No need to shuffle for inference
        pin_memory=True, 
        num_workers=4
    )
    print("Dataset built.")

    # Load Model
    print("Loading trained model from:", config['out_dir_model'])
    try:
        model = BertForMaskedLM.from_pretrained(config['out_dir_model'])
    except Exception as e:
        print(f"Error loading model from {config['out_dir_model']}: {e}")
        print("Please ensure the model has been trained and saved to this directory.")
        sys.exit(1)
    
    model.to(accelerator.device)
    
    # Prepare model and loader with accelerator
    model, val_loader = accelerator.prepare(model, val_loader)
        
    print("Starting Inference...")
    
    accuracy = evaluate.load("accuracy")
    model.eval()
    
    val_loss = 0
    total_samples = 0
    
    with torch.no_grad():
        for val_batch in tqdm(val_loader, desc="Evaluating"):
            input_ids = val_batch['input_ids']
            attention_mask = val_batch['attention_mask']
            labels = val_batch['labels']

            # Forward pass
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            
            # Helper for loss calculation
            val_loss += outputs.loss.item()
            
            # Predictions
            predictions = outputs.logits.detach().cpu().numpy()
            labels_np = labels.detach().cpu().numpy()
            
            # Compute accuracy on masked tokens
            for i in range(len(outputs.logits)):
                # Get prediction for each token
                pred = np.argmax(predictions[i], axis=1)
                
                # Mask out tokens that are -100 in labels (padding/ignored)
                pred[labels_np[i] == -100] = -100
                
                # Filter out -100s for metric calculation
                pr = pred[pred != -100]
                lb = labels_np[i][labels_np[i] != -100]
                
                # Add to metric
                accuracy.add_batch(predictions=pr, references=lb)

    # Compute final metrics
    val_loss /= len(val_loader)
    val_acc = accuracy.compute()
    
    print("\n" + "="*30)
    print("INFERENCE RESULTS")
    print("="*30)
    print(f"Validation Loss: {val_loss:.6f}")
    print(f"Accuracy:        {val_acc['accuracy']:.6f}")
    print("="*30)
