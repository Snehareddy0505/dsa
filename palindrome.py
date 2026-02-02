class Solution:    
    def palindromeCheck(self, s,i=0):
        #your code goes here
        n=len(s)
        if i>= n//2:
            return True
        if s[i]!=s[n-i-1]:
            return False
        return self.palindromeCheck(s,i+1)
s= "hannah"
sol=Solution()
print("result is:",sol.palindromeCheck(s))
