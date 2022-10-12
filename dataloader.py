from sacred import Ingredient

dataloader_ing = Ingredient("dataloader")

@dataloader_ing.config
def cfg():
    data_dir = "/tmp/data/abc"

@dataloader_ing.capture
def load_data(data_dir):
    print(f"Loaded data from {data_dir}")