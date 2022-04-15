"""
自除数 是指可以被它包含的每一位数整除的数。

例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
自除数 不允许包含 0 。

给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。

"""

class Solution:
    def selfDividingNumbers(self, left, right):
        ans = list()
        for i in range(left, right+1):
            if all([ 1 if int(item) > 0 and i % (int(item)) == 0 else 0 for item in str(i)]):
                ans.append(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.selfDividingNumbers(1, 22))