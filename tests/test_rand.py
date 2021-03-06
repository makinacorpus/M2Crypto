#!/usr/bin/env python

"""Unit tests for M2Crypto.Rand.

Copyright (C) 2006 Open Source Applications Foundation (OSAF).
All Rights Reserved.
"""

import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from M2Crypto import Rand

class RandTestCase(unittest.TestCase):
    def test_bytes(self):
        with self.assertRaises(MemoryError):
            Rand.rand_bytes(-1)
        self.assertEqual(Rand.rand_bytes(0), '')
        self.assertEqual(len(Rand.rand_bytes(1)), 1)

    def test_pseudo_bytes(self):
        with self.assertRaises(MemoryError):
            Rand.rand_pseudo_bytes(-1)
        self.assertEqual(Rand.rand_pseudo_bytes(0), ('', 1))
        a, b = Rand.rand_pseudo_bytes(1)
        self.assertEqual(len(a), 1)
        self.assertEqual(b, 1)

    def test_load_save(self):
        try:
            os.remove('tests/randpool.dat')
        except OSError:
            pass
        self.assertEqual(Rand.load_file('tests/randpool.dat', -1), 0)
        self.assertEqual(Rand.save_file('tests/randpool.dat'), 1024)
        self.assertEqual(Rand.load_file('tests/randpool.dat', -1), 1024)

    def test_seed_add(self):
        self.assertIsNone(Rand.rand_seed(os.urandom(1024)))

        # XXX Should there be limits on the entropy parameter?
        self.assertIsNone(Rand.rand_add(os.urandom(2), 0.5))
        Rand.rand_add(os.urandom(2), -0.5)
        Rand.rand_add(os.urandom(2), 5000.0)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RandTestCase))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
