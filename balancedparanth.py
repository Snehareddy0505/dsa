class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapi={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in mapi:
               if st:
                 top=st.pop()
               else:
                 top='#'
               if mapi[ch]!=top:
                 return False
            else:
              st.append(ch)
        return not st
if __name__ == "__main__":
    s = input("Enter brackets string: ")
    obj = Solution()
    result = obj.isValid(s)
    print(result)