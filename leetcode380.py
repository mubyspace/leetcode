"""
实现RandomizedSet 类：
RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

"""
import random
class RandomizedSet:

    def __init__(self):
        self.dic = dict()
        self.list = list()

    def insert(self, val):
        if val in self.dic:
            return False
        else:
            self.dic[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val):
        if val not in self.dic:
            return False
        else:
            idx = self.dic[val]
            self.list[idx] = self.list[-1]
            self.dic[self.list[-1]] = idx
            self.list.pop()
            self.dic.pop(val)
            return True

    def getRandom(self):
        return self.list[random.randint(0, len(self.list) - 1)]


if __name__ == '__main__':

    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.insert(2)
    param_3 = obj.remove(1)
    param_4 = obj.remove(1)
    param_5 = obj.getRandom()
    print(param_1, param_2, param_3, param_4, param_5)
