def asteroidcollision(asteriods):
    st=[]
    for ast in asteriods:
        while st and ast<0 and st[-1]>0:
            if st[-1]<-ast:
                st.pop()
                continue
            elif st[-1]==-ast:
                st.pop()
            break
        else:
            st.append(ast)
    return st
asteroids=nums=list(map(int,input("Enter asteriods:").split()))
print(asteroidcollision(asteroids ))