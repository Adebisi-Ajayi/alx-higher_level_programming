#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first
    character
    """
    ade_len = len(sentence)
    if ade_len == 0:
        ade_char = None
    else:
        ade_char = sentence[0]
    return ((ade_len, ade_char))
