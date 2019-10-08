class Solution:
    def removeDuplicates(self, S):
        count = 1
        while (count > 0):
            if(len(S)==0):
                return ""
            if(len(S)==1):
                return S
            elif(len(S)==2):
                lis = list(S)
                if(lis[0]==lis[1]):
                    return ""
                else:
                    return S
            else:
                lis = list(S)
                lon = len(lis)
                indexList=[]
                count=0
                for (index,value)in enumerate(lis[0:lon-1]):
                    if(lis[index+1]==lis[index]):
                        count=count+1
                        indexList.insert(0,index)
                        indexList.insert(0,index+1)
                #对indexList去重
                newIndexList=[]
                for (index,value)in enumerate(indexList):
                    if(value not in newIndexList):
                        newIndexList.append(value)
                newIndexList.sort(reverse=True)
                for (index,value)in enumerate(newIndexList):
                    del lis[value]
                print(lis)
                print(count)
                S=''.join(lis)
            continue


                # print(S)
S="aaaaaaaaa"
# S=""
a=Solution().removeDuplicates(S)
print("result:"+a)

