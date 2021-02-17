t= int(input())
u=t
while t>0:
    t-=1
    N,K= map(int,input().split())
    nums =[int(x) for x in input().split()]
    def check(mid):
        noofadditionalsessions = 0
        for i in range(1,N):
            noofadditionalsessions+= (nums[i]-nums[i-1]-1)//mid
        if noofadditionalsessions <=K:
            return True
        return False
    def binarysearch(low,high):
        while low<high:
            mid  = (low+high)//2
            if check(mid):
                high=mid
            else:
                low = mid+1
        return low
    ans = binarysearch(1,10**9)
    print("Case #{}: {} ".format(u-t,ans))
