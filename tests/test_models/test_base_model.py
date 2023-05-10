#!/usr/bin/python3

"""test_base_model module to test BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class to run tests on BaseModel"""

    def setUp(self):
        """Instantiate BaseModel"""

        self.bm = BaseModel()

    def test_base_model(self):
        """Test BaseModel object"""

        print(self.bm)
        self.bm.save()
        print(self.bm)
        bm_json = self.bm.to_dict()
        print(bm_json)
        print("JSON of bm:")
        for key in bm_json.keys():
            print("\t{}: ({}) - {}".format(key, type(bm_json[key]), bm_json[key]
            ))

if __name__ == "__main__":
    unittest.main()
