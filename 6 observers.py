from sacred import Experiment
from sacred.observers import MongoObserver

ex = Experiment('observers')

######################################
# also provides observers for sql, tinyDB, files, many more (even telegram)
ex.observers.append(MongoObserver(url='localhost:27017', db_name='sacred'))
######################################

@ex.config
def my_config():
    message = "Hello world!"

@ex.automain
def my_main(_config, _seed, _rnd, _log, _run):
    print(_config["message"])
    _log.info(f"seed: {_seed}")
    _log.info(f"random number with {_seed}: {_rnd.randint(100)}")
    _run.log_scalar("test", 1, 1)
    _run.log_scalar("test", 2, 2)
    _run.log_scalar("test", 3, 3)