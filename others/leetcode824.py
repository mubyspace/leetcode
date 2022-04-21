"""
leetcode824
"""
class Solution:
    def toGoatLatin(self, sentence):
        s = sentence.split(" ")
        for i in range(len(s)):
            if s[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                s[i] += 'ma'
            else:
                ss = s[i][1:] + s[i][0] + 'ma'
                s[i] = ss
            s[i] += 'a' * (i + 1)
        return " ".join(s)
if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))
