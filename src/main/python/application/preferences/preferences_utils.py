import os
import json


def create_config_file(path):
    obj = {
        "deviceId": "",
        "primaryKey": ""
    }
    if os.path.isfile(path) is not True:
        with open(path, 'x') as json_file:
            json_string = json.dumps(obj)
            json_file.write(json_string)

def get_device_id(path):
    if os.path.isfile(path):
        f = open(path, 'r')
        json_file = json.load(f)
        f.close()
        if json_file['deviceId'] == "":
            json_file['deviceId'] = os.popen("cat /sys/class/net/eth0/address").read()
            write_device_id(json_file)
        return json_file['deviceId']
    return None

def get_device_key(path):
    if os.path.isfile(path):
        f = open(path, 'r')
        json_file = json.load(f)
        f.close()
        return json_file['primaryKey']
    return None

def write_device_id(path, obj):
    if os.path.isfile(path):
        with open(path, 'w') as json_file:
            json_string = json.dumps(obj)
            json_file.write(json_string)

def write_device_key(path, key):
    if os.path.isfile(path):
        with open(path, 'r+') as json_file:
            json_obj = json.load(json_file)
            json_obj['primaryKey'] = key
            json_string = json.dumps(json_obj)
            json_file.write(json_string)

def write_username(path, name):
    if os.path.isfile(path):
        with open(path, 'r+') as json_file:
            json_obj = json.load(json_file)
            json_obj['userName'] = name
            json_string = json.dumps(json_obj)
            json_file.write(json_string)

def get_username(path):
    if os.path.isfile(path):
        f = open(path, 'r')
        json_file = json.load(f)
        f.close()
        return json_file['userName']
    return None

if __name__ == "__main__":

    device_name = get_device_id()

    print(device_name)