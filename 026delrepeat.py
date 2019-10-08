#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
class Solution(object):
    def removeDuplicates(self, nums):
        maps = {}
        for index,value in enumerate(nums):
            if value not in maps.values():
                maps[index]=value
            else:
                nums[index]='willdelete'
        for i in range(len(nums)-1,-1,-1):
            if nums[i]=='willdelete':
              nums.remove(nums[i])
        print(nums)
        return len(nums)

nums = [1,1,1,1,1,1,1,2]
Solution().removeDuplicates(nums)

