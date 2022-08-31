from base import BaseModel

'''
   Review class - review e.g. bad
'''


class Review(BaseModel):
    def __init__(self, name=None):
        super.__init__()
        if name is not None:
            self.name = name

    '''
       To-do:
       1. Name - add getter, setter, validation
       2. Add id
    '''
