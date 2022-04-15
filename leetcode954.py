"""

给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <=i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

"""
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr):
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:  # 无法找到足够的 2x 与 x 配对
                return False
            cnt[2 * x] -= cnt[x]
        return True



if __name__ == '__main__':
    s = Solution()
    print(s.canReorderDoubled([2, 4, 0, 0, 8, 1]))
