import yaml
from yaml.loader import SafeLoader

class Config:
    with open('config.yml','r') as config_file:
        config = yaml.load(config_file.read(),Loader=SafeLoader)