import unittest
from activities import drinks

"""
testejä voi ajaa python filenimi, kunhan 
if __name__ == "__main__":
    unittest.main()

on olemassa.
"""

class ActivityTests(unittest.TestCase):
    def setUp(self):
        print()
        print("jepa jee testejää!")

    def test_enough_drinks(self):
        """More the merrier, but no less than two kind of drinks"""
        self.assertGreater(len(drinks()), 2)
        # self.assertEqual(len(drinks()), 2)

    def tearDown(self):
        print("No miten meni, noin niinq omasta mielestä?")


if __name__ == "__main__":
    unittest.main()
