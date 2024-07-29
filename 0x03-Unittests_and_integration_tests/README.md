# GitHub Organization Client and Utility Tests

This project consists of utilities and a client for interacting with the GitHub API, along with comprehensive unit and integration tests to ensure functionality.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow the pycodestyle style (version 2.5)
- All files must be executable
- All modules, classes, and functions should have documentation
- All functions and coroutines must be type-annotated

## Directory Structure


## Modules and Tests

### 0-utils.py
This module provides utility functions:
- `access_nested_map(nested_map, path)`: Accesses a nested dictionary using a sequence of keys.
- `get_json(url)`: Fetches JSON data from a URL.
- `memoize(method)`: Decorator to cache method calls.

### 1-test_utils.py
This module contains unit tests for the utility functions in `0-utils.py`. It uses the `unittest` framework and `parameterized` for parameterized testing.
- `TestAccessNestedMap`: Tests for `access_nested_map`.
- `TestGetJson`: Tests for `get_json`.
- `TestMemoize`: Tests for `memoize`.

### 2-client.py
This module defines a client for GitHub API interactions:
- `GithubOrgClient`: A class to interact with GitHub organizations.
  - `org`: Property to fetch organization details.
  - `_public_repos_url`: Property to get the URL for public repositories.
  - `public_repos`: Method to get the list of public repositories.
  - `has_license`: Method to check if a repository has a specific license.

### 3-test_client.py
This module contains unit tests for the `GithubOrgClient` class in `2-client.py`. It uses `unittest`, `parameterized`, and `unittest.mock` for testing.
- `TestGithubOrgClient`: Tests for `GithubOrgClient` class methods and properties.

### 4-fixtures.py
This module provides example payloads for integration tests.

### 5-test_integration.py
This module contains integration tests for `GithubOrgClient` using fixtures from `4-fixtures.py`. It uses `unittest`, `parameterized_class`, and `unittest.mock`.
- `TestIntegrationGithubOrgClient`: Integration tests for `GithubOrgClient`.
