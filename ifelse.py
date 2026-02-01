class Solution:
    def studentGrade(self, marks):
        if marks>= 90:
           return"A"
        elif marks>=70:
            return"B"
        elif marks>=50:
            return "c"
        elif  marks>=35:
            return"D"
        else:
            return"fail"
marks=76
sol=Solution()
print("result is:",sol.studentGrade(marks))