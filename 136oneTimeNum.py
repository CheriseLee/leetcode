# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
class Solution:
    def singleNumber(self, nums):
        maps = {}
        for index,value in enumerate(nums):
            if value not in maps.keys():
                maps[value]=1
            else:
                maps[value] +=1
        print(maps)
        for key in maps:
            if maps[key]==1:
                return key
nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))