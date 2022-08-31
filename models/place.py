from base import BaseModel
'''
   Place class - place e.g. City Park
'''


class Place(BaseModel):
    def __init__(self, name=None):
        super.__init__()
        if name is not None:
            self.name = name

    '''
       To-do:
       1. Name - add getter, setter, validation
       2. Add id
    '''
