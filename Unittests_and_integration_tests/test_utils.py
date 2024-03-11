#!/usr/bin/env python3
"""
Parameterize a unit test
"""
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


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
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, ErrMessage):
        """
        Parameterize a unit test
        """
        with self.assertRaises(KeyError) as er:
            access_nested_map(map, path)
            self.assertEqual(ErrMessage, er.exception)


class TestGetJson(TestCase):
    """
    Mock HTTP calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that function returns the expected result.
        """
        mock_returned = Mock()
        mock_returned.json.return_value = test_payload
        with patch('requests.get', return_value=mock_returned):
            test_response = get_json(test_url)
            self.assertEqual(test_response, test_payload)
            # Test that the mocked get method was called exactly once
            mock_returned.json.assert_called_once()
