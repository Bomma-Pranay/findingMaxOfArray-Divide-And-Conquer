def f(a,lo,hi):
    if lo==hi:
        return a[lo]
    mid=(lo+hi)//2
    m=max(f(a,lo,mid),f(a,mid+1,hi))
    return m
#Give elements as input
a=list(map(int,input().split())
mx=f(a,0,len(a)-1)
print('maximum element in',a,'is ',mx)
