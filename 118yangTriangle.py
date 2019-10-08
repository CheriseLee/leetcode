# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
class Solution:
    def generate(self, numRows):
        lst = []
        for i in range(numRows):
            if i==0:
                childlst = [1]
                lst.append(childlst)
            elif i==1:
                childlst1=[1,1]
                lst.append(childlst1)
            else:
                childlst = [1]
                for j in range(len(lst[i-1])-1):
                    num = lst[i-1][j]+lst[i-1][j+1]
                    print("sum")
                    print(num)
                    childlst.append(num)
                childlst.append(1)
                lst.append(childlst)
        return lst
nums = 5
an=Solution().generate(nums)
print(an)

