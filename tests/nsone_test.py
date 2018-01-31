import ns1
import nsone
import unittest


class LegacyTest(unittest.TestCase):
    def test_import(self):
        self.assertEqual(nsone, ns1)

    def test_main_class(self):
        self.assertEqual(nsone.NSONE, ns1.NS1)
