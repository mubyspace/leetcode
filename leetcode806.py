"""
我们要把给定的字符串 S从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组widths，
这个数组widths[0] 代表 'a' 需要的单位，widths[1] 代表 'b' 需要的单位，...，widths[25] 代表 'z' 需要的单位。

现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。

"""


class Solution:
    def numberOfLines(self, widths, s):
        ans, tmp = 0, 0
        for ch in s:
            if widths[ord(ch) - ord('a')] + tmp <= 100:
                tmp += widths[ord(ch) - ord('a')]
            else:
                tmp = widths[ord(ch) - ord('a')]
                ans += 1
        return [ans+1, tmp]

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))