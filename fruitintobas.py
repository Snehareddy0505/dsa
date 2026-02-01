def fruitintobasket(arr):
    n = len(arr)
    maxlen = 0

    for i in range(n):
        st = set()
        for j in range(i, n):
            st.add(arr[j])
            if len(st) <= 2:
                maxlen = max(maxlen, j - i + 1)
            else:
                break 

    print(maxlen)
arr = [1, 2, 1, 2, 3]
fruitintobasket(arr)
