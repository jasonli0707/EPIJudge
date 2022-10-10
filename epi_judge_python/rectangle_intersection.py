import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    """return the rectangle formed by intersection of two rectangles r1 & r2

    Args:
        r1 (Rect): XY-axis aligned rectangle
        r2 (Rect): XY-axis aligned rectangle

    Returns:
        Rect: intersection oof r1 and r2
    """

    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2
    xw1, yh1, xw2, yh2 = x1+w1, y1+h1, x2+w2, y2+h2

    if not ((x1<=xw2) and (x2<=xw1) and (y1<=yh2) and (y2<=yh1)): # check if two rectangles intersect or not
        return Rect(0, 0, -1, -1)

    left = max(x1, x2)
    bottom = max(y1, y2)
    right = min(xw1, xw2)
    top = min(yh1, yh2)

    return Rect(left, bottom, right-left, top-bottom)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
