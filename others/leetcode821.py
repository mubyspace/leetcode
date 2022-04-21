"""
leetcode821 字符最短距离
给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。

返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。

两个下标i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数

"""
import bisect


class Solution:
    def shortestToChar(self, s, c):
        n = len(s)
        res = [0] * n
        left, right = -n, 0
        for i in range(n):
            if i > right:
                left = right
                right = i
            while right < n and s[right] != c:
                right += 1
            if right == n:
                right = 2 * n
            res[i] = min(i - left, right - i)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.shortestToChar("loveleetcode", "e"))
