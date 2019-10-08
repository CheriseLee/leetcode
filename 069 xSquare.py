#求平方根
import math
class Solution(object):
    def mySqrt(self, x):
        return int(math.sqrt(x))

x=8
a=Solution().mySqrt(x)
print(a)