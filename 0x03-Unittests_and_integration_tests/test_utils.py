#!/usr/bin/env python3
"""Utilities module"""

import requests
from typing import Callable, Dict, Tuple, Any


def access_nested_map(nested_map: Dict[str, Any],
                      path: Tuple[str, ...]) -> Any:
    """Access a nested map with a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Dict:
    """Fetch JSON data from a URL."""
    response = requests.get(url)
    return response.json()


def memoize(method: Callable) -> Callable:
    """Decorator to cache method calls."""
    import functools

    @functools.wraps(method)
    def memoized_method(self):
        if not hasattr(self, '_cache'):
            self._cache = {}
        if method not in self._cache:
            self._cache[method] = method(self)
        return self._cache[method]

    return memoized_method
