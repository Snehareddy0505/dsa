n=int(input())
resultBinaryString="" 
while(n!=0):
    rem = n%2 #we will divide the remainder
    resultBinaryString+=str(rem) # we will convert rem into string and add into result
    n=n//2 # divide the quotient
print(resultBinaryString[::-1]) # slicing:to get output in reverse