class Solution:
    def plusOne(self, digits):
        newlist = []
        for key,value in enumerate(digits):
            newlist.append(str(value))
        s = ''.join(newlist)
        num = int(s) + 1
        lst = []
        for key,value in enumerate(list(str(num))):
            lst.append(int(value))
        return(lst)




digits = [1,2,3]
p = Solution().plusOne(digits)
print(p)