import json

def read_transactions(file_path):
  try:
    with open(file_path, "r") as json_file:
      data = json.load(json_file)
  except json.JSONDecodeError:
    data = []
  except FileNotFoundError:
    data = []
  return data

def write_transactions(file_path, data):
  with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)
