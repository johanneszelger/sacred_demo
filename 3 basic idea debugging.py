from sacred import Experiment

def optionHook(options):
    options['--debug'] = True
    options['--pdb'] = True

ex = Experiment('basic idea debugging')
ex.option_hook(optionHook)

@ex.config
def my_config():
    message = "Hello world!"

@ex.automain
def my_main(message):
    print(message)