# Saving a dict to json file
import json


def save_dict(_dict, filepath):
    json.dump(_dict, open(filepath, 'w'))
    print("Saved")

