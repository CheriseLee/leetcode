class Solution:
    def transpose(self, lst):
        newlst=[]
        for index,value in enumerate(lst):
            print(index)
            print(value)
            for childIndex,childValue in enumerate(value):
                print(childIndex)
                print(childValue)
                newlst[index][childIndex]=childValue
        return newlst



lst=[[1,2,3],[4,5,6],[7,8,9]]
newlst = Solution().transpose(lst)
print(newlst)