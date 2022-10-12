from sacred import Experiment

ex = Experiment('basic idea')

@ex.config
def my_config():
    message = "Hello world!"

@ex.automain
def my_main(message):
    print(message)