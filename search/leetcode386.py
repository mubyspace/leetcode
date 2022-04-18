"""
leetcode389 字典序排数
给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
"""


class Solution:
    def lexicalOrder(self, n: int):
        ans, cur = [], 1
        for i in range(1, n + 1):
            ans.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur == n:
                    cur = cur // 10
                cur += 1
        return ans

    def lexicalOrder2(self, n: int):
        ans = []

        def dfs(cur, nn, ans):
            # nonlocal ans
            if cur > nn:
                return
            ans.append(cur)
            for ii in range(0, 10):
                dfs(10 * cur + ii, nn, ans)

        for i in range(1, n + 1):
            dfs(i, n, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lexicalOrder2(99))
