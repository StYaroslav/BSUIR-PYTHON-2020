import unittest
import json
from tasks.json_deserializer import from_json, FormatException


class TestFromJson(unittest.TestCase):
    def setUp(self):
        self.expected_object = json.loads(json.dumps({None: True, 18: [1, 2, '6'], False: {12: (1, 2), 'string': 123}}))

    def test_from_json_converter(self):
        self.assertEqual(self.expected_object, from_json(json.dumps({None: True, 18: [1, 2, '6'], False: {12: (1, 2), 'string': 123}})))

    def test_invalid_input(self):
        invalid_string_1 = '{"string": True, "18": null, "false": [1, 2, 3]}'
        invalid_string_2 = '{string: true, "18": null, "false": [1, 2, 3]}'
        invalid_string_3 = '{"string": true, "18": None, "false": [1, 2, 3]}'
        self.assertRaises(FormatException, from_json, invalid_string_1)
        self.assertRaises(FormatException, from_json, invalid_string_2)
        self.assertRaises(FormatException, from_json, invalid_string_3)