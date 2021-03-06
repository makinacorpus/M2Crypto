"""
M2Crypto wrapper for OpenSSL BN (BIGNUM) API.

Copyright (c) 2005 Open Source Applications Foundation. All rights reserved.
"""

import m2

def rand(bits, top=-1, bottom=0):
    """
    Generate cryptographically strong random number.

    @param bits:   Length of random number in bits.
    @param top:    If -1, the most significant bit can be 0. If 0, the most
                   significant bit is 1, and if 1, the two most significant
                   bits will be 1.
    @param bottom: If bottom is true, the number will be odd.
    """
    return m2.bn_rand(bits, top, bottom)


def rand_range(range):
    """
    Generate a random number in a range.

    @param range: Upper limit for range.
    @return:      A random number in the range [0, range)
    """
    return m2.bn_rand_range(range)


def randfname(length):
    """
    Return a random filename, which is simply a string where all
    the characters are from the set [a-zA-Z0-9].

    @param length: Length of filename to return.
    @type length:  int
    @return:       random filename string
    """
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
    lettersLen = len(letters)
    fname = []
    for x in range(length):
        fname += [letters[m2.bn_rand_range(lettersLen)]]

    return ''.join(fname)
