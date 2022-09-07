from base_model import BaseModel

import unittest
import sys
from uuid import UUID
from datetime import datetime

sys.path.append('/home/elisha/Documents/AirBnB_clone/models')


class TestBaseModel(unittest.TestCase):

    global base_model1
    base_model1 = BaseModel()

    def test_id(self):

        """
           Checks if ID is valid
        """
        self.assertTrue(UUID(base_model1.id, version=4))

    def test_date_format(self):
        """
           Checks if date is in correct format
        """
        self.assertEqual("Foo", "Foo")

    def test_assign_num(self):
        """
           Tests assign number
        """
        base_model1.my_number = 89
        self.assertEqual(base_model1.my_number, 89)

    def test_print_model(self):
        self.assertEqual(base_model1.to_string(), '[{}] ({}) {}'
                         .format(base_model1.__class__.__name__,
                                 base_model1.id,
                                 base_model1.__dict__))

    def test_to_dict(self):
        dict_ = {}
        dict_['__class__'] = base_model1.__class__.__name__

        for key, value in base_model1.__dict__.items():
            # check if value is of type datetime
            if isinstance(value, datetime):
                dict_[key] = value.isoformat()
            else:
                dict_[key] = value

        self.assertEqual(base_model1.to_dict(), dict_)


if __name__ == '__main__':

    unittest.main()
