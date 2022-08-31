#!/usr/bin/python3
"""
Module: base_model.py
This module contains the base class(model) to be inherited for all the models
Copyright (c) 2022
"""


class BaseModel():
    id = 0

    def __init__(self, id):
        Base.id += 1
        self.id = Base.id
        self.created_at = 0
        self.update_at = 0

    '''
       Todo:
       1. Add json serialization - json.dumps()
       2. Add json deserialization - json.loads()
       3. Add string method - __str__
       4. Add uuid to generate ids
       5. Add times for update and create
       6. Add save method
       7. Add to_dict method
    '''
