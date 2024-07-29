#!/usr/bin/env python3
"""Unit tests for utils module"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test that get_json returns expected result."""
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
        for test_url, test_payload in test_cases:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)
            mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""

    class TestClass:
        """Test class with a_method and memoized a_property"""

        def a_method(self) -> int:
            """Returns 42"""
            return 42

        @memoize
        def a_property(self) -> int:
            """Returns result of a_method"""
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """Test that memoized method is called once"""
        obj = self.TestClass()
        self.assertEqual(obj.a_property(), 42)
        self.assertEqual(obj.a_property(), 42)
        mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
