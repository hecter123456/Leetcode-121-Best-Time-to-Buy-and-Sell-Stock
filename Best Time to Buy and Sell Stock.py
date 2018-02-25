import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = 0
        self.assertEqual(Solution().maxProfit(Input),Output)

class Solution():
    def maxProfit(self, prices):
        if prices == []:
            return 0

if __name__ == '__main__':
    unittest.main()
