"""
leetcode479 最大回文乘积

给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。

枚举回文数的左半部分，降序检测
"""


class Solution:
    def largestPalindrome(self, n):
        if n == 1:
            return 9
        upper = 10 ** n - 1
        for left in range(upper, upper // 10, -1):
            p, x = left, left
            while x:
                p = p * 10 + x % 10
                x = x // 10
            x = upper
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.largestPalindrome(2))
