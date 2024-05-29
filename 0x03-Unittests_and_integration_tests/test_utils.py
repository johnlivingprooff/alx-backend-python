#!/usr/bin/env python3
"""Test utils"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

        @parameterized.expand([
            ({}, ("a,")),
            ({"a": 1}, ("a", "b")),
        ])
        def test_access_nested_map_exception(self, nested_map, path):
            """Test access_nested_map raises KeyError for invalid path"""
            with self.assertRaises(KeyError):
                access_nested_map(nested_map, path)
            self.assertRaises(KeyError, access_nested_map, nested_map, path)

        
class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns a dict"""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        mock_get.return_value = mock_resp

        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""

    def test_memoize(self):
        """Test memoize stores result of function"""
        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            
        with patch.object(TestClass, "a_method") as mock_method:
            test = TestClass()
            mock_method.return_value = 42
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
