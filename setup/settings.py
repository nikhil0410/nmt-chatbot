import os

# root package path (leave as is, or type full path)
package_path = os.path.realpath(os.path.dirname(__file__) + '/..')

# model path
out_dir = os.path.join(package_path, "model")

# training data path
train_dir = os.path.join(package_path, "data")

# raw data path (data to be prepared and tokenized)
source_dir = os.path.join(package_path, "new_data")

# preprocessing settings
preprocessing = {
    # number of samples to save in training data set
    # -1 means all available in source data set
    'samples': -1,

    # vocab max size
    'vocab_size': 100000,

    # test sets' max size
    'test_size': 100,

    # vocab max entity length (-1 for no limit)
    'vocab_entity_len': -1,

    # source (raw) data folder
    'source_folder': source_dir,

    # place to save preprocessed and tokenized training set
    'train_folder': train_dir,

    # file with protected phrases
    'protected_phrases_file': os.path.join(package_path, 'setup/protected_phrases.txt'),

}

# hparams
hparams = {
    'attention': 'scaled_luong',
    'src': 'from',
    'tgt': 'to',
    'vocab_prefix': os.path.join(train_dir, "vocab"),
    'train_prefix': os.path.join(train_dir, "train"),
    'dev_prefix': os.path.join(train_dir, "tst2012"),
    'test_prefix': os.path.join(train_dir, "tst2013"),
    'out_dir': out_dir,
    'num_train_steps': 500000,
    'num_layers': 5,
    'num_units': 1024,
#    'override_loaded_hparams': True,
    'decay_factor': 0.99998,
    'decay_steps': 1,
#    'residual': True,
    'start_decay_step': 1,
    'beam_width': 10,
    'length_penalty_weight': 1.0,
    'num_translations_per_input': 10
}
