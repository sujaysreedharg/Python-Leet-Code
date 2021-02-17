t= int(input())
u=t
while t>0:
    t-=1
    N,B= map(int,input().split())
    arrays =[int(x) for x in input().split()]
    maxhouses = 0
    arrays.sort()
    for i in range(N):
        if arrays[i] <= B:
            maxhouses+=1
            B-=arrays[i]
    
    print("Case #{}: {} ".format(u-t,maxhouses))
