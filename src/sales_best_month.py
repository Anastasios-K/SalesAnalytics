import os
import pandas as pd
from src.generic_functions import read_yaml_file

config = read_yaml_file(os.path.join("src", "config.yaml"))

df = pd.read_excel(config["paths"]["data_path"])
