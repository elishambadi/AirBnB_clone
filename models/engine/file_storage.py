#!/usr/bin/env python3

"""
   FileStorage class
   Does serialization and deserialization of data to JSON files
   Classes:
   - FileStorage
"""

import sys
import json

sys.path.append("/home/elisha/Documents/AirBnB_clone/models")


class FileStorage():
    """
       File storage
       Attrs:
       - file_path: private, shows path to storage file
       - objects: private, dict of all objects

       Methods
       - all()
       - new()
       - save()
       - reload
    """

    __file_path = "/home/elisha/Documents/AirBnB_clone/models/engine/file.json"
    __objects = {}
    writes = 0

    def __init__(self):
        self.__objects = {}

    @property
    def file_path(self):
        return self.__file_path

    def test(self):
        print("File storage is accessible")

    def all(self):
        return self.__objects

    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self, obj):
        # add saved obj to objects dict
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

        # Serialize everything to json
        json_obj = json.dumps(self.__objects)
        with open(self.file_path, 'w+') as f1:
            f1.write(json_obj)

    def reload(self):
        try:
            with open(self.file_path, 'r') as f1:
                self.__objects = json.load(f1)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    print("Testing File store...")
