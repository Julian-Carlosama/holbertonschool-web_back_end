#!/usr/bin/env python3
""" Module Unnitest """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parametrized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Testing function Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, outputResult):
        """ Testing for access_nested-map """
        self.assertEqual(access_nested_map(map, path), outputResult)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
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


class TestMemoize(TestCase):
    """ Class that allow testing memoization """

    def test_memoize(self):
        """ Method that testing memoize functions """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method that return 42"""
                return 42

            @memoize
            def a_property(self):
                """ Method that Returns memoized """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
