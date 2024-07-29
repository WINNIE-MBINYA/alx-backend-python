#!/usr/bin/env python3
"""Integration tests for GithubOrgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
import fixtures


@parameterized_class([
    {"org_payload": fixtures.org_payload,
     "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos,
     "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patcher"""
        cls.get_patcher.stop()

    @staticmethod
    def side_effect(url):
        """Side effect method for mocking requests.get"""
        if "orgs" in url:
            return MockResponse(fixtures.org_payload)
        elif "repos" in url:
            return MockResponse(fixtures.repos_payload)
        return MockResponse(None)

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license method"""
        client = GithubOrgClient("google")
        self.assertEqual(
            [repo["name"] for repo in client.public_repos()
                if GithubOrgClient.has_license(repo, "apache-2.0")],
            self.apache2_repos
        )


class MockResponse:
    """Mock response class for requests.get"""

    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        """Return json data"""
        return self.json_data
