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
from torch.optim import AdamW
from tqdm import tqdm
import numpy as np
import evaluate
import statistics
import datetime
import pickle

# Import from local modules
from utils.dataset import Dataset
from config import config, model_config

if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"   
    
    
    # Setup simple logging to file
    log_file = os.path.join(config['out_dir_model'], 'training_log.txt')
    os.makedirs(config['out_dir_model'], exist_ok=True)
    
    domain=config["domain"]

    with open(log_file, 'w') as f:
        f.write("BERT Blocksworld Pre-Training Log\n")
        f.write("=" * 50 + "\n")
        f.write(f"Configuration:\n")
        for key, value in config.items():
            f.write(f"  {key}: {value}\n")
        f.write("=" * 50 + "\n\n")
    
    accelerator = Accelerator(gradient_accumulation_steps=config['accumulation_steps'])#mixed_precision="fp16", # type: ignore
    

    print(f"Device: {accelerator.device}")

    print("Loading data...")
    
    read_test_plans_dir=config['plans']
    problem_dirs = os.listdir(read_test_plans_dir)
    #Shuffle plans randomly
    random.seed(10)
    random.shuffle(problem_dirs)
    piani=[]
    piani_mask=[]

    for problem_dir in problem_dirs:

        obs_path = os.path.join(read_test_plans_dir, problem_dir, 'obs.dat')
        init_path = os.path.join(read_test_plans_dir, problem_dir, 'template.pddl')
        goal_path = os.path.join(read_test_plans_dir, problem_dir, 'real_hyp.dat')
        poss_goal= os.path.join(read_test_plans_dir, problem_dir, 'hyps.dat')
        azioni=[]
        with open(obs_path, 'r') as obs_file:
            obs = obs_file.readlines()
            piano="[SG] [A] "
            for o in obs:
                azioni.append(o.lower().split('|')[0].replace('(', '').replace(')','').replace("\n",""))

        azioni_spezzate=[]
        for a in azioni:
            azioni_spezzate+=a.split()
        mask=random.sample(range(0, len(azioni_spezzate)), round(len(azioni_spezzate)*0.33))
        azioni_masked=copy.deepcopy(azioni_spezzate)
        for i in mask:
            azioni_masked[i]="[MASK]"
        
        #########################
        with open(init_path, 'r') as init_file:
            init = init_file.readlines()
            initial_state=[]

            check=False
            for i in init:
                
                if '(:goal' in i:
                    break
                if check:
                    if domain=="logistics" and "in-city" not in i:
                        initial_state+=i.lower().replace('(', '').replace(')','').replace('\n', '').replace('\t', '')
                    elif domain=="zeno" and "next" not in i:
                        initial_state.append(i.lower().replace('(', '').replace(')','').replace('\n', '').replace('\t', ''))
                    elif domain=="driverlog" and "link" not in i and "path" not in i and "next" not in i:
                        initial_state.append(i.lower().replace('(', '').replace(')','').replace('\n', '').replace('\t', ''))
                    elif domain=="satellite" and "satellite " not in i and "instrument " not in i and "mode " not in i and "direction " not in i and "calibration_target " not in i and "supports " not in i and "on_board " not in i:
                        initial_state.append(i.lower().replace('(', '').replace(')','').replace('\n', '').replace('\t', ''))
                    elif domain=="depots":
                        initial_state.append(i.lower().replace('(', '').replace(')','').replace('\n', '').replace('\t', ''))
                    elif domain=="blocksworld":
                        initial_state.append(i.lower().replace('(', '').replace(')','').replace('\n', '').replace('\t', ''))

                if '(:init' in i:
                    check=True
            
            initial_state=[a.lower().strip() for a in initial_state]

        ####################################
        with open(goal_path, 'r') as goal_file:
            goal = goal_file.read()
            goals = goal.split(', ')
            goal=[a.lower().strip().replace('(', '').replace(')','') for a in goals]

        
        piano="[SI] "+ " ".join(initial_state) + " [SG] " + " ".join(goal) + " [A] " + " ".join(azioni_spezzate)
        piano_masked="[SI] "+ " ".join(initial_state) + " [SG] " + " ".join(goal) + " [A] " + " ".join(azioni_masked)
        piani.append(piano)
        piani_mask.append(piano_masked)
        print(piano)
        print(piano_masked)
    
            
    #split dataset in train and test
        
    train=piani[:-config["num_val"]]
    train_mask=piani_mask[:-config["num_val"]]
    
    validation=piani[-config["num_val"]:]
    validation_mask=piani_mask[-config["num_val"]:]
    
    # test=piani[-config["num_test"]:]
    # test_mask=piani_mask[-config["num_test"]:]
    
    print(f"Len train:{len(train)}, Len val: {len(validation)}")

    print("Loading tokenizer...")
    tokenizer = PreTrainedTokenizerFast.from_pretrained(config["tokenizer_path"])
    print("Tokenizer loaded.")
  
    print("Masking data...")
    
    #Mask data and create labels
    batch = tokenizer(train, max_length=config['max_length'], padding='max_length', truncation=True)
    batch_mask = tokenizer(train_mask, max_length=config['max_length'], padding='max_length', truncation=True)
    mask = torch.tensor([x for x in batch["attention_mask"]])
    labels = torch.tensor([x for x in batch["input_ids"]])
    input_ids = torch.tensor([x for x in batch_mask["input_ids"]])

    batch_val = tokenizer(validation, max_length=config['max_length'], padding='max_length', truncation=True)
    batch_mask_val = tokenizer(validation_mask, max_length=config['max_length'], padding='max_length', truncation=True)
    labels_val = torch.tensor([x for x in batch_val["input_ids"]])
    input_ids_val = torch.tensor([x for x in batch_mask_val["input_ids"]])
    mask_val = torch.tensor([x for x in batch_val["attention_mask"]])

    # batch_test = tokenizer(test, max_length=config['max_length'], padding='max_length', truncation=True)
    # batch_mask_test = tokenizer(test_mask, max_length=config['max_length'], padding='max_length', truncation=True)
    # labels_test = torch.tensor([x for x in batch_test["input_ids"]])
    # input_ids_test = torch.tensor([x for x in batch_mask_test["input_ids"]])
    # mask_test = torch.tensor([x for x in batch_test["attention_mask"]])

    #Set -100 the logits in labels where is padding  
    for i in range(input_ids.shape[0]):
        labels[i][mask[i]==0]=-100

    for i in range(input_ids_val.shape[0]):
        labels_val[i][mask_val[i]==0]=-100
    
    # for i in range(input_ids_test.shape[0]):
    #     labels_test[i][mask_test[i]==0]=-100
        
    print("Data masked.")
    
    
    print("Building Dataset...")
    #Build dataset
    encodings = {'input_ids': input_ids, 'attention_mask': mask, 'labels': labels}
    encodings_val = {'input_ids': input_ids_val, 'attention_mask': mask_val, 'labels': labels_val}
    # encodings_test = {'input_ids': input_ids_test, 'attention_mask': mask_test, 'labels': labels_test}

    dataset = Dataset(encodings)
    dataset_val = Dataset(encodings_val)
    # dataset_test = Dataset(encodings_test)


    loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, pin_memory=True, num_workers=4) # type: ignore
    val_loader= DataLoader(dataset_val, batch_size=config["batch_size"], shuffle=True, pin_memory=True, num_workers=4) # type: ignore
    # test_loader= DataLoader(dataset_test, batch_size=1, shuffle=True, pin_memory=True, num_workers=4) # type: ignore
    print("Dataset built.")

    #Build model
    bert_config = BertConfig(
        vocab_size=tokenizer.vocab_size, 
        pad_token_id=tokenizer.pad_token_id, 
        is_decoder=False,
        **model_config
    )
    model = BertForMaskedLM(bert_config)  
    
    
    model.to(accelerator.device) # type: ignore
    optim = AdamW(model.parameters(), lr=config['learning_rate']) # type: ignore

    #sched = torch.optim.lr_scheduler.StepLR(optim, step_size=1)
    sched=transformers.get_constant_schedule(optim) # type: ignore


    model, optim, loader, val_loader, sched = accelerator.prepare(model, optim, loader, val_loader, sched)
        
    
    
    print("Training...")
    
    best_loss=10000
    accuracy = evaluate.load("accuracy")
    count=0
    best_val=0
    
    for epoch in range(config['epochs']): # type: ignore
        model.train()
        
        print("Epoch: "+str(epoch))
        print("Training...")
        total_loss = 0
        if count==config["early_stopping"] and config["enable_early_stopping"]:
            break
        count+=1
        #with accelerator.autocast():
        for batch in tqdm(loader):
            with accelerator.accumulate(model):

                input_ids = batch['input_ids']
                attention_mask = batch['attention_mask']
                labels = batch['labels']
                outputs = model(input_ids, attention_mask=attention_mask,
                                labels=labels, return_dict=True)

                loss = outputs.loss
                
                accelerator.backward(loss)
                
                total_loss += loss.item()
                optim.step()
                sched.step()
                
                optim.zero_grad()
                
                predictions=outputs.logits.detach().cpu().numpy()
                labels=labels.detach().cpu().numpy()
                #Compute accuracy on masked tokens
                for i in range(len(outputs.logits)):
                    pred = np.argmax(predictions[i], axis=1)
                    pred[labels[i] == -100] = -100
                    #Set -100 the logits in pred where labels =-100
                    pr=pred[pred!=-100]
                    lb=labels[i][labels[i]!=-100]
                    accuracy.add_batch(predictions=pr, references=lb)

        
        loss=total_loss/len(loader)
        acc=accuracy.compute()
        memory_usage=float(torch.cuda.memory_allocated()/1000000000)
        print(f"Training loss: {loss}, Accuracy: {acc['accuracy']}, Time: {datetime.datetime.now()}, Memory Usage: {memory_usage}")
        
        # Log to file
        with open(log_file, 'a') as f:
            f.write(f"Epoch {epoch} - Training: loss={loss:.6f}, accuracy={acc['accuracy']:.6f}, memory={memory_usage:.2f}GB\n")


        model.eval()
        val_loss = 0
        print("Validazione...")
        with torch.no_grad():
            for val_batch in tqdm(val_loader):
                input_ids = val_batch['input_ids']
                attention_mask = val_batch['attention_mask']
                labels = val_batch['labels']

                val_outputs = model(input_ids, attention_mask=attention_mask,
                                labels=labels)
                predictions=val_outputs.logits.detach().cpu().numpy()
                labels=labels.detach().cpu().numpy()
                for i in range(len(val_outputs.logits)):
                    pred = np.argmax(predictions[i], axis=1)
                    pred[labels[i] == -100] = -100
                    pr=pred[pred!=-100]
                    lb=labels[i][labels[i]!=-100]
                    accuracy.add_batch(predictions=pr, references=lb)
                

                val_loss += val_outputs.loss.item()

            val_loss /= len(val_loader)
            if val_loss<best_loss:
                best_loss=val_loss
                count=0
            val_acc=accuracy.compute()
            if val_acc["accuracy"]>best_val:
                best_val=val_acc["accuracy"]
                model.save_pretrained(config['out_dir_model'])
            memory_usage=float(torch.cuda.memory_allocated()/1000000000)
            print(f"Validation loss: {val_loss}, Accuracy: {val_acc['accuracy']}, Time: {datetime.datetime.now()}, Memory Usage: {memory_usage}")
            
            # Log to file
            with open(log_file, 'a') as f:
                f.write(f"Epoch {epoch} - Validation: loss={val_loss:.6f}, accuracy={val_acc['accuracy']:.6f}, memory={memory_usage:.2f}GB\n")
            
        # with torch.no_grad():
        #     for test_batch in test_loader:
        #         input_ids = test_batch['input_ids']
        #         attention_mask = test_batch['attention_mask']
        #         labels = test_batch['labels']
        #         test_outputs = model(input_ids, attention_mask=attention_mask,
        #                         labels=labels)
        #         predictions=test_outputs.logits.detach().cpu().numpy()
        #         labels=labels.detach().cpu().numpy()
        #         for i in range(len(test_outputs.logits)):
        #             pred = np.argmax(predictions[i], axis=1)
        #             pred[labels[i] == -100] = -100
        #             pr=pred[pred!=-100]
        #             lb=labels[i][labels[i]!=-100]
        #             accuracy.add_batch(predictions=pr, references=lb)
        #     test_acc=accuracy.compute()
    print("Training done.")

        