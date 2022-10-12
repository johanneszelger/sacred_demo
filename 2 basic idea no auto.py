from sacred import Experiment

ex = Experiment('basic idea no auto')

@ex.config
def my_config():
    message = "Hello world!"

@ex.main
def my_main(message):
    print(message)

ex.run()