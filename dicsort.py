from collections import Counter
class Solution:
    def frequencySort(self,s):
        d=Counter(s)
        u_d=sorted(d.items(),key=lambda x:-x[1])
        result="" 
        for i,j in u_d:
            result+=i*j
        return result
sol=Solution()
print(sol.frequencySort("tree"))
