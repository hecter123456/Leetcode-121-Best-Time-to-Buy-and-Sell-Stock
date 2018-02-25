import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = 0
        self.assertEqual(Solution().maxProfit(Input),Output)
    def testSample(self):
        Input = [7, 1, 5, 3, 6, 4]
        Output = 5
        self.assertEqual(Solution().maxProfit(Input),Output)

class Solution():
    def maxProfit(self, prices):
        ans = 0
        low = prices[0]
        for i in prices:
            ans = max(ans,(i-low))
            low = min(i,low)
        return ans

if __name__ == '__main__':
    unittest.main()
