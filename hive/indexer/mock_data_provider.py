""" Data provider for test operations """
from json import dumps

class MockDataProvider():
    """ Data provider for test operations """
    block_data = {}

    @classmethod
    def print_data(cls):
        print(dumps(cls.block_data, indent=4, sort_keys=True))