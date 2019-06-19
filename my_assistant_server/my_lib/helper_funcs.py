import json
import os
import sys
sys.path.append("..")
from my_assistant.settings import BASE_DIR


file_path = os.path.join(BASE_DIR, 'config/global_config.json')

def read_config_file():
    try:
        with open(file_path, 'rt') as f:
            data = json.load(f)
        return data
    except IOError as err:
        print('File error: ' + str(err))
    except Exception as other:
        print('Something else broke: ' + str(other))
