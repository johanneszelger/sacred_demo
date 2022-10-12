from sacred import Experiment
from sacred.observers import MongoObserver

ex = Experiment('configs')

ex.add_config({"message": "New message"})
# ex.add_config("config.yaml")
# with message="cmd line message"

@ex.automain
def my_main(_config, _seed, _rnd, _log, _run):
    print(_config["message"])
    _log.info(f"seed: {_seed}")
    _log.info(f"random number with {_seed}: {_rnd.randint(100)}")
    _run.log_scalar("test", 1, 1)
    _run.log_scalar("test", 2, 2)
    _run.log_scalar("test", 3, 3)