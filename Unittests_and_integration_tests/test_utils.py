#!/usr/bin/env python3
"""
Parameterize a unit test
"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """
    class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, map, path, expected_output):
        """
        method to test that the method returns what it is supposed to.
        """
        output = access_nested_map(map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, ErrMessage):
        """
        Parameterize a unit test
        """
        with self.assertRaises(KeyError) as er:
            access_nested_map(map, path)
            self.assertEqual(ErrMessage, er.exception)
