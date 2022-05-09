"""
leetcode 887 鸡蛋掉落
给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

"""
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if n == 1:
            return 1
        # f[i][j] 表示j个鸡蛋操作i次在最坏的情况下最多可以确认的楼层高度
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, k + 1):
            f[1][i] = 1
        ans = -1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                # 楼下可以确定 f[i - 1][j - 1]层，楼上可以确定 f[i - 1][j]层
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
            if f[i][k] >= n:
                ans = i
                break
        return ans

    def superEggDrop2(self, K, N):
        dp = [[0] * (N+1) for _ in range(K+1)]
        for k in range(1, K+1):
            for n in range(1, N+1):
                if k == 1:
                    dp[k][n] = n
                elif n == 1:
                    dp[k][n] = 1
                else:
                    # 碎了 dp[k-1][i-1]
                    # 没碎 dp[k][n-i]
                    dp[k][n] = min(1+max(dp[k-1][i-1], dp[k][n-i]) for i in range(1, n+1))
        return dp[K][N]


if __name__ == '__main__':
    s = Solution()
    print(s.superEggDrop(3, 14))
    print(s.superEggDrop2(3, 14))