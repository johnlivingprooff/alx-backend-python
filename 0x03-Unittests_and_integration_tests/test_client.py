#!/usr/bin/env python3
"""Test client"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_public_repos_url(self, org_name, mock_get_json):
        """Test _public_repos_url method"""
        test_class = GithubOrgClient(org_name)
        test_class.org = PropertyMock(
            return_value={"repos_url": "http://test.com"})
        self.assertEqual(test_class._public_repos_url, "http://test.com")

    @parameterized.expand([
        ("google", TEST_PAYLOAD),
        ("abc", TEST_PAYLOAD),
    ])
    @patch('client.get_json')
    def test_repos_payload(self, org_name, test_payload, mock_get_json):
        """Test repos_payload method"""
        test_class = GithubOrgClient(org_name)
        test_class.org = PropertyMock(
            return_value={"repos_url": "http://test.com"})
        test_class.repos_payload()
        mock_get_json.assert_called_once_with("http://test.com")

    @parameterized.expand([
        ("google", TEST_PAYLOAD, None, ["test"]),
        ("abc", TEST_PAYLOAD, None, ["test"]),
        ("google", TEST_PAYLOAD, "MIT", ["test"]),
        ("abc", TEST_PAYLOAD, "MIT", ["test"]),
    ])
    @patch('client.GithubOrgClient.repos_payload', new_callable=PropertyMock)
    def test_public_repos(self, org_name, test_payload,
                          license, expected, mock_repos_payload):
        """Test public_repos method"""
        test_class = GithubOrgClient(org_name)
        mock_repos_payload.return_value = test_payload
        self.assertEqual(test_class.public_repos(license), expected)

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("example_org")

        # Patch access_nested_map to return the appropriate license_key
        with patch('github_org_client.access_nested_map') as mock_access_n_map:
            mock_access_n_map.return_value = repo['license']['key']

            # Call the has_license method
            result = client.has_license(repo, license_key)

            # Assert the result matches the expected value
            self.assertEqual(result, expected)


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"), [
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Patch requests.get to return example payloads
        cls.get_patcher = patch('github_org_client.requests.get')

        # Start the patcher
        cls.mock_get = cls.get_patcher.start()

        # Configure side_effect for requests.get().json()
        # to return the appropriate payloads
        cls.mock_get.side_effect = [
            cls.org_payload,  # For the organization payload
            cls.repos_payload  # For the repositories payload
        ]

    @classmethod
    def tearDownClass(cls):
        # Stop the patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("example_org")

        # Call the public_repos method
        repos = client.public_repos()

        # Assert that the returned repositories match the expected ones
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("example_org")

        # Call the public_repos method with a specific license
        repos = client.public_repos(license="Apache-2.0")

        # Assert that the returned repositories match
        # the expected ones with Apache-2.0 license
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
