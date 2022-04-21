"""
给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果NestedInteger 。
列表中的每个元素只可能是整数或整数嵌套列表

输入：s = "324",
输出：324
解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。

输入：s = "[123,[456,[789]]]",
输出：[123,[456,[789]]]
解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789


1. 首先判断s是否为空，为空直接返回；

2. s不为空的话看首字符是否为’[’，不是的话说明s为一个整数，我们直接返回结果。

3. 如果s中首字符是’[’，且s长度小于等于2，说明没有内容，直接返回结果。（’[‘或’[]’）

4. 如果s长度大于2，我们从i=1开始遍历，我们需要一个变量start来记录某一层的真实位置，用cnt来记录跟真实位置是否为同一深度，cnt=0表示同一深度，
   由于中间每段都是由逗号隔开，所以当我们判断当cnt为0，且当前字符是逗号或者已经到字符串末尾了，我们把start到当前位置之间的字符串取出来递归调用函数，
   把返回结果加入res中，然后start更新为i+1。如果遇到’[’，计数器cnt自增1，若遇到’]’，计数器cnt自减1。
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if len(s) == 0:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        if len(s) <= 2:
            return NestedInteger()
        res = NestedInteger()
        start,cnt = 1, 0
        for i in range(1, len(s)):
            if cnt == 0 and (s[i] == ',' or i == len(s) - 1):
                res.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == '[':
                cnt += 1
            elif s[i] == ']':
                cnt -= 1
        return res