from sacred import Experiment
from sacred.observers import MongoObserver
from dataloader import dataloader_ing, load_data

ex = Experiment('ingredients', ingredients=[dataloader_ing])

# dataloader_ing.add_config({"data_dir": "/new_dir"})
# dataloader_ing.add_config("config.yaml")
# with dataloader.data_dir="/cmd_line_dir"

@ex.automain
def my_main(_config, _seed, _rnd, _log, _run):
    load_data()
    # load_data("/manual_param_dir")