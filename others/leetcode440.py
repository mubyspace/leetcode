"""
给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ans = 1
        k -= 1
        while k > 0:
            step, tmp, next = 0, ans, ans + 1
            while tmp <= n:
                step += min(next, n + 1) - tmp
                for i in range(tmp, min(tmp+step, n)):
                    print(i)
                # print(tmp, min(tmp+step, n))
                next *= 10
                tmp *= 10
            if step <= k:
                k -= step
                ans += 1
            else:
                ans *= 10
                k -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findKthNumber(13, 13))
