'''
   Base model to initialize and serialize data
'''

import datetime
import uuid


class BaseModel():
    id = 0

    def __init__(self, name=None, my_number=None):
        self.id = uuid.uuid4()
        if name is not None:
            self.name = name
        if my_number is not None:
            self.my_number = my_number
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def str(self):
        return ("[{:s}] ({:d}) {{:s}}".format(type(self).__name__, self.id, self.to_dict()))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return self.__dict__
