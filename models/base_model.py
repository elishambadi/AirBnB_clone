#!/usr/bin/python3
"""
Module: base_model.py
This module contains the base class(model) to be inherited for all the models
Copyright (c) 2022
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    The base class for the AirBnB console

    Methods:
        __init__(self)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes id, created_at, updated_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation for model object.
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_string(self):
        """
        Return a string representation for model object for use in unittest
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the instance attribute 'updated_at' with the current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values pair of __dict__ of the
        instance.
        """
        dict_ = {}
        dict_['__class__'] = self.__class__.__name__

        for key, value in self.__dict__.items():
            # check if value is of type datetime
            if isinstance(value, datetime):
                dict_[key] = value.isoformat()
            else:
                dict_[key] = value

        return dict_
