"""
你有 k个服务器，编号为 0到 k-1，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 不能同时处理超过一个请求。请求分配到服务器的规则如下：

第i（序号从 0 开始）个请求到达。
如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。
如果第(i % k)个服务器空闲，那么对应服务器会处理该请求。
否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。
比方说，如果第 i个服务器在忙，那么会查看第 (i+1)个服务器，第 (i+2)个服务器等等。
给你一个 严格递增的正整数数组arrival，表示第i个任务的到达时间，和另一个数组load，其中load[i]表示第i个请求的工作量
（也就是服务器完成它所需要的时间）。你的任务是找到 最繁忙的服务器。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。

请你返回包含所有最繁忙服务器序号的列表，你可以以任意顺序返回这个列表。

"""

from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heapq.heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heapq.heappush(busy, (start + t, id))
            available.remove(id)
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]


if __name__ == '__main__':
    s = Solution()
    print(s.busiestServers(3, [1,2,3,4,5], [5,2,3,3,3]))