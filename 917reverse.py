import string
class Solution:
    def reverseOnlyLetters(self, S):
        allletter = []
        for key in S:
            if key in string.ascii_letters:
                allletter.append(key)
        allletter.reverse()
        listS = list(S)
        reindex = 0
        for index,value in enumerate(listS):
            if value in string.ascii_letters:
                listS[index]=allletter[reindex]
                reindex = reindex +1
            else:
                continue
        str = ''.join(listS)
        return str







S="a-bC-dEf-ghIj"
ne = Solution().reverseOnlyLetters(S)
print(ne)