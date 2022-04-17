"""
leetcode480 滑动窗口中位数

中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
例如：
[2,3,4]，中位数是3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。


我们维护一个最大堆 max_heap，用来存储小于中位数的数，维护一个最小堆 min_heap，用来存储大于中位数的数。
    最小堆中有效元素的个数与最大堆中有效元素的个数相等，或者刚好多一个（反之亦可）。有效元素的个数记为 len(heap)len(heap)
    这里有效元素指的是在当前滑动窗口内的元素。

我们只需要保证两个堆中有效元素的个数符合我们的规定，并且两个堆顶的元素也在窗口内即可保证计算出来的中位数是正确的，其他多余的元素我们暂时不必要弹出。
于是，如果k是奇数，每次只需要把最小堆的堆顶放入答案；如果k是偶数，就取两个堆顶的平均值作为答案。

"""

import heapq


class Solution:
    def medianSlidingWindow(self, nums, k):
        min_heap, max_heap = [], []

        # 初始化
        for i in range(k):
            heapq.heappush(min_heap, (nums[i], i))
        for i in range(k // 2):
            n, idx = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-n, idx))

        res = [(min_heap[0][0] - max_heap[0][0]) / 2 if k % 2 == 0 else min_heap[0][0] * 1.0]

        for i in range(k, len(nums)):
            # 如果新数字应该放到最大堆
            if nums[i] < min_heap[0][0]:
                heapq.heappush(max_heap, (-nums[i], i))
                # 如果要弹出的元素在最小堆中，调整
                if nums[i - k] >= min_heap[0][0]:
                    n, idx = heapq.heappop(max_heap)
                    heapq.heappush(min_heap, (-n, idx))
            else:
                heapq.heappush(min_heap, (nums[i], i))
                # 如果要弹出的元素在最大堆中，调整
                # 取等号是特殊情况
                if nums[i - k] <= min_heap[0][0]:
                    n, idx = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, (-n, idx))

            # 将堆顶在窗口外的元素清除出去
            while min_heap and min_heap[0][1] <= i - k:
                heapq.heappop(min_heap)
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)

            # 添加答案
            res.append((min_heap[0][0] - max_heap[0][0]) / 2 if k % 2 == 0 else min_heap[0][0] * 1.0)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
