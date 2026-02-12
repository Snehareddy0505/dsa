def removekthdigits(num,k):
    st=[]
    for ch in num:
        while st and k>0 and st[-1]>ch:
            st.pop()
            k-=1
        st.append(ch)
    while k>0:
        st.pop()
        k-=1
    res="".join(st).lstrip('0')
    if res:
        return res
    else:
      return '0'
num=input()
k=int(input())
print("remanining elemnts:",removekthdigits(num,k))