#!/usr/bin/env python3
"""
   FileStorage class
i   Does serialization and deserialization of data to JSON files
"""
import sys
import json


sys.path.append("/home/elisha/Documents/AirBnB_clone/models")

from base_model import BaseModel

class FileStorage():
    """
i       File storade
       Attrs:
       - file_path: private, shows path to storage file
       - objects: private, dict of all objects
       
       Methods
       - all()
       - new()
    """

    __file_path = ""
    __objects = {}
    writes = 0

    def __init__(self):
        pass

    def all(self):
        return __objects

    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        dict_ = {}
        dict_[key] = obj.to_dict()
        json_obj = json.dumps(dict_, indent=4)


	#Remove last and first digits

        #Add this JSON object to a storage file
        f= open("file.json", 'a')
        if self.writes > 0:
            f.write(", ")
            f.write(json_obj)
        else:
            f.write(json_obj)

        f.close()
        self.writes += 1

if __name__ == "__main__":
    print("Testing File store...")

    base = BaseModel()
    store = FileStorage()

    base.number = 2000

    print(json.dumps(base.to_dict(), indent=4))
    store.new(base)
    store.new(base)
    store.new(base)
