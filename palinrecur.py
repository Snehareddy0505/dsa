def palindrome(i):
    if i >= n // 2:
        return True
    if s[i] != s[n - i - 1]:
        return False
    return palindrome(i + 1)

s = input()
n = len(s)

print(palindrome(0))
