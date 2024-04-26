from functools import cache

import pygame

from .constants import (
    MAX_COLOR_SHIFT,
)


@cache
def _tuplize_if_not_container(value):
    if '__iter__' not in dir(value):
        return (value, )
    return value


def check_types_or_keys(event, types, keys):
    target_types = _tuplize_if_not_container(types)
    if event.type in target_types:
        return True
    if event.type == pygame.KEYUP:
        target_keys = _tuplize_if_not_container(keys)
        return event.key in target_keys
    return False


def update_shifts_inplace(data, pointer):
    new_pointer = (pointer + 1) % len(data)
    if not data[pointer] == MAX_COLOR_SHIFT:
        data[pointer] -= 1
    else:
        if not data[new_pointer] == MAX_COLOR_SHIFT:
            data[new_pointer] += 1
        else:
            data[pointer] -= 1
    pointer_upgrade = pointer
    if not data[pointer]:
        pointer_upgrade = new_pointer
    return pointer_upgrade
