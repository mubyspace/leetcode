from functools import lru_cache


class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        dp = [[[-1] * n for _ in range(n)] for _ in range(2 * n)]
        return self.helper(graph, 0, 1, 2, dp)

    def helper(self, graph, t, x, y, dp):
        if t == len(dp): return 0
        if x == y:
            dp[t][x][y] = 2
            return dp[t][x][y]
        if x == 0:
            dp[t][x][y] = 1
            return dp[t][x][y]
        if t % 2 == 0:
            flag = True
            for i in range(len(graph[x])):
                next = self.helper(graph, t + 1, graph[x][i], y, dp)
                if next == 1:
                    dp[t][x][y] = 1
                    return dp[t][x][y]
                elif next != 2:
                    flag = False
            if flag:
                dp[t][x][y] = 2
                return dp[t][x][y]
        else:
            flag = True
            for i in range(len(graph[y])):
                if graph[y][i] == 0:
                    continue
                next = self.helper(graph, t + 1, x, graph[y][i], dp)
                if next == 2:
                    dp[t][x][y] = 2
                    return dp[t][x][y]
                elif next != 1:
                    flag = False
            if flag:
                dp[t][x][y] = 1
                return dp[t][x][y]
        dp[t][x][y] = 0
        return dp[t][x][y]

    def catMouseGame2(self, graph):
        @lru_cache(None)
        def search(t, x, y):
            return 0 if t == (len(graph) << 1) else 2 if x == y else 1 if not x else 2 if (
                    t & 1 and any(search(t + 1, x, i) == 2 for i in graph[y] if i)) else 0 if (
                    t & 1 and any(search(t + 1, x, i) == 0 for i in graph[y] if i)) else 1 if t & 1 else 1 if any(
                search(t + 1, i, y) == 1 for i in graph[x]) else 0 if any(
                search(t + 1, i, y) == 0 for i in graph[x]) else 2

        return search(0, 1, 2)


if __name__ == '__main__':
    s = Solution()
    print(s.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
