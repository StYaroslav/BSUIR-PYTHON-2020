import json
import unittest

from tasks.json_serializer import to_json



class TestToJsonConverter(unittest.TestCase):
    def setUp(self):
        self.test_object = {None: True, 18: [1, 2, '6'], False: {12: (1, 2), 'string': 123}}
        self.expected_string = json.dumps(self.test_object)

    def test_normal_performance(self):
        self.assertEqual(self.expected_string, to_json(self.test_object))
