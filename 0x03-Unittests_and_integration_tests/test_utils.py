#!/usr/bin/env python3
"""Test utils"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self):
        """Test access_nested_map exception"""
        nested_map = {"a": {"b": 2}}
        path = ("a", "c")
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), "c")


class TestGetJson(unittest.TestCase):
    """Test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test memoize"""
    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            """Test class"""
            def __init__(self):
                """Init method"""
                self._nb = 0

            @memoize
            def nb_calls(self):
                """nb_calls method"""
                self._nb += 1
                return self._nb

        test = TestClass()
        self.assertEqual(test.nb_calls(), 1)
        self.assertEqual(test.nb_calls(), 1)
        self.assertEqual(test.nb_calls(), 1)


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""
    @parameterized.expand([
        ("google", {"repos_url": "http://google.com"}),
        ("abc", {"repos_url": "http://abc.com"})
    ])
    def test_org(self, org_name, org_payload):
        """Test org"""
        test_client = GithubOrgClient(org_name)
        test_client._org_name = org_name
        with patch('client.get_json', return_value=org_payload):
            self.assertEqual(test_client.org(), org_payload)

    @parameterized.expand([
        ("google", "http://google.com", "apache", ["repo1", "repo2"]),
        ("abc", "http://abc.com", "mit", ["repo3", "repo4"])
    ])
    def test_public_repos(self, org_name, repos_url, license_key, expected):
        """Test public_repos"""
        test_client = GithubOrgClient(org_name)
        test_client._org_name = org_name
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = [{"name": "repo1",
                                           "license": {"key": license_key}},
                                          {"name": "repo2",
                                          "license": {"key": "other"}},
                                          {"name": "repo3",
                                          "license": {"key": license_key}},
                                          {"name": "repo4",
                                          "license": {"key": "other"}}]
            self.assertEqual(test_client.public_repos(license_key), expected)
            self.assertEqual(test_client.public_repos(), ["repo1", "repo3"])
            mock_get_json.assert_called_once_with(repos_url)

    def test_has_license(self):
        """Test has_license"""
        repo = {"license": {"key": "mit"}}
        self.assertTrue(GithubOrgClient.has_license(repo, "mit"))
        self.assertFalse(GithubOrgClient.has_license(repo, "apache"))
        self.assertFalse(GithubOrgClient.has_license(repo, None))


if __name__ == '__main__':
    unittest.main()
