import json

def read_transactions(file_path):
  with open(file_path, "r") as json_file:
    data = json.load(json_file)
  return data

def write_transactions(file_path, data):
  with open(file_path, "a") as json_file:
    json.dump(json_file, data)
