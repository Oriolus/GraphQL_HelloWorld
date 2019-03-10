import yaml


def load():
    settings = None
    with open('config.yaml', 'r') as conf_file:
        settings = yaml.load(conf_file)
    return settings

