# -*- coding: utf-8 -*-
"""
Configuration file for BERT pre-training .
"""

# Training configuration
config = {
    #Domain to train
    "domain": "blocksworld",
    
    # Model architecture
    "architecture": "BertForMaskedLM",
    
    # Training hyperparameters
    "learning_rate": 1e-4,
    "epochs": 25,
    "batch_size": 32,
    "accumulation_steps": 1,
    
    # Data parameters
    "max_length": 200,  # 200 for blocksworld, 140 for satellite
    "num_val": 2,
    "perc_train": 1,
    "perc_test": 1,
    
    # Paths
    "tokenizer_path": "models/blocksworld/tokenizer",
    "plans": "examples_data/blocksworld",
    "out_dir_model": "models/blocksworld/model/model_base/",
    
    # Early stopping
    "enable_early_stopping": False,
    "early_stopping": 5,
}

# Model architecture configuration
model_config = {
    "hidden_size": 256,
    "hidden_act": "gelu",
    "initializer_range": 0.02,
    "hidden_dropout_prob": 0.1,
    "num_attention_heads": 4,
    "type_vocab_size": 2,
    "max_position_embeddings": 512,
    "num_hidden_layers": 2,
    "intermediate_size": 512,
    "attention_probs_dropout_prob": 0.1,
}
