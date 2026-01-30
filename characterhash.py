# Input: a string of characters (no need to split)
s = input("Enter characters: ")

# Initialize a hash table for all ASCII characters
hash_table = [0] * 256

# Count frequency of each character
for char in s:
    ascii_val = ord(char)  # Get ASCII value of the character
    hash_table[ascii_val] += 1

# Number of queries
q = int(input("Enter number of queries: "))

# Handle queries
for _ in range(q):
    c = input("Enter query character: ")
    if len(c) == 1:
        ascii_val = ord(c)
        print(f"{c}-{hash_table[ascii_val]}")
    else:
        print("Please enter only one character.")
