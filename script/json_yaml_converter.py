import json

import yaml

root_dir = "../"
json_dir = root_dir + "translations"
yaml_dir = root_dir + "translations_yaml"


def yaml_to_json(source_path, target_path):
    data = yaml.load(open(source_path, "r"))
    json.dump(data, open(target_path, "w+"))


def json_to_yaml(source_path, target_path):
    data = json.load(open(source_path, "r"))
    yaml.dump(data, open(target_path, "w+"))
