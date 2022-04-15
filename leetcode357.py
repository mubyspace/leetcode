"""
给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10^n
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        f = [0] * 11
        f[0], f[1], f[2] = 1, 9, 81
        for i in range(3, 11):
            f[i] = f[i-1] * (11-i)
        return sum(f[0:n+1])

if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(0))