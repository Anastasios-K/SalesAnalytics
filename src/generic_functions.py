import yaml


def read_yaml_file(path: str):
    with open(path) as file:
        content = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
    return content