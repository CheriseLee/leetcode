#给定一个Excel表格中的列名称，返回其相应的列序号。
import string
class Solution(object):
    def titleToNumber(self, s):
        lst = []
        maps={}
        sum = 0
        for index,value in enumerate(list(string.ascii_uppercase)):
            maps[value]=int(index)+1
        lst=list(s)
        for index,value in enumerate(list(s)):
            a = int(maps[value])
            b = 26**(len(lst)-index-1)
            # sum = sum +[26**(len(lst))]*int(maps[value])
            sum = sum + a*b

        return sum



Solution().titleToNumber("BA")


