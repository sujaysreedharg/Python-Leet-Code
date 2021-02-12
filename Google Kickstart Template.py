# Template 1:

t=int(input())
u=t
while t>0:
    t-=1
    n,k,p=map(int,input().split())
    print(n)
    print(k)
    print(p)
    for i in range(n):
        b=[int(x) for x in input().split()]
        print(b)

    print("Case #",end="")
    print(u-t,end="")
    print(":",0)
    
# Template 2:


t=int(input())
u=t
while t>0:
    t-=1
    n,k,p=map(int,input().split())
    print(n)
    print(k)
    print(p)
    for i in range(n):
        b=[int(x) for x in input().split()]
        print(b)

    print("Case #{}: {} ".format(u-t,80))
    
    
    
    
    
    
    
Input :


2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10


    
    
    
    
    

