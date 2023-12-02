#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the first two elements of two tuples together
    and returns the result
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    ade_tup = ()
    for i in range(2):
        if i >= len_a:
            a = 0
        else:
            a = tuple_a[i]
        if i >= len_b:
            b = 0
        else:
            b = tuple_b[i]

        if (i == 0):
            ade_tup = (a + b)
        else:
            ade_tup = (ade_tup, a + b)
    return (ade_tup)
