#!/usr/bin/env python3
""" Module Unnitest """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parametrized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(TestCase):
    """ Class that check test json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Method that allow return correct """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()
