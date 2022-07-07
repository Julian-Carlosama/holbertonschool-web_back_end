#!/usr/bin/env python3
""" Module Unnitest """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parametrized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ Testing function Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, outputResult):
        """ Testing for access_nested-map """
        self.assertEqual(access_nested_map(map, path), outputResult)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, outError):
        """ Method that access nested exection """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(outError, e.exception)
