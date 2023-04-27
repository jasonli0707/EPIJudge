from typing import Iterator, List
from collections import namedtuple

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    """Process buildings from east-to-west order and returns the set of buildings which view the sunset
       Time: O(n) 
       Space: O(1) best-case (increasing height from east-to-west) and O(n) worst-case (decreasing height from east-to-west)

    Args:
        sequence (Iterator[int]): buildings from east-to-west

    Returns:
        List[int]: buildings which view the sunset from west-to-east
    """
    Building = namedtuple("Building", ['id', 'height'])

    buildings_have_view = []

    for id, height in enumerate(sequence):
        while buildings_have_view and height >= buildings_have_view[-1].height:
            buildings_have_view.pop() # remove all buildings of which sunset view are blocked 

        buildings_have_view.append(Building(id, height))

    return [b.id for b in reversed(buildings_have_view)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
