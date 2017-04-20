data_config = {
    'word_size' : 16,
    'word_count_threshold' : 10,
    'char_count_threshold' : 50,
    'max_context_len' : 870,
    'max_query_len' : 65,
    'pickle_file' : 'vocabs.pkl',
}

model_config = {
    'hidden_dim'     	: 100,
    'char_convs'     	: 100,
    'char_emb_dim'   	: 8,
    'dropout'        	: 0.2,
    'highway_layers' 	: 2,
    'two_step'       	: True,
    'use_cudnn'      	: False,
}

training_config = {
    'minibatch_size'	: 4096,    # in samples when using ctf reader
    'epoch_size'     	: 85540,   # in sequences, when using ctf reader
    'log_freq'       	: 500,     # in minibatchs
    'max_epochs'     	: 300,
    'lr'             	: 0.5,
    'train_data'     	: 'train.ctf',
    #'train_data'     	 : 'train.tsv',
    'val_data'       	: 'val.ctf',
    'val_interval'   	: 1,       # interval in epochs to run validation
    'stop_after'     	: 10,      # num epochs to stop if no CV improvement
    'minibatch_seqs' 	: 16,      # num sequences of minibatch, when using tsv reader

    # block momentum settings
    'block_size'     	: 10000,    # block size in sequences, for block momentum
    'distributed_after' : 250000, # num sequences after which to start distributed training
}