"""
leetcode123 买卖股票的最佳时机3
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


由于我们最多可以完成两笔交易，因此在任意一天结束之后，我们会处于以下五个状态中的一种：
    未进行过任何操作；
    只进行过一次买操作；
    进行了一次买操作和一次卖操作，即完成了一笔交易；
    在完成了一笔交易的前提下，进行了第二次买操作；
    完成了全部两笔交易。

无论题目中是否允许「在同一天买入并且卖出」这一操作，最终的答案都不会受到影响，这是因为这一操作带来的收益为零。
"""


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 6, 5, 4, 3, 2, 1]))
