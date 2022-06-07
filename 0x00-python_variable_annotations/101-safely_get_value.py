#!/usr/bin/env python3
""" Module that add type annotations to the function """


from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """ Return values with the appropriate types """
    if key in dct:
        return dct[key]
    else:
        return default
