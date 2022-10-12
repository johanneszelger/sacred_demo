from sacred import Experiment

def optionHook(options):
    options['--debug'] = True
    options['--pdb'] = True

ex = Experiment('captures')
ex.option_hook(optionHook)

@ex.config
def my_config():
    message = "Hello world!"

@ex.capture
def show_message(message):
    print(message)

@ex.automain
def my_main():
    show_message()