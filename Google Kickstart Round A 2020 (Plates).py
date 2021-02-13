t= int(input())
u=t
while t>0:
    t-=1
    n,k,p = map(int,input().split())
    a=[]
    dp = [[-1]*31 for i in range(n)]
    for i in range(n):
        b=[int(x) for x in input().split()]

        c=[0]
        
        for i in range(0,k):
            c.append(c[i]+b[i])
        a.append(c)
    print(a)
    def dfs(idx,taken):
        if taken==p:
            return 0
        if idx>n-1 or taken>p:
            return float("-inf")
        if dp[idx][taken]!=-1:
            return dp[idx][taken]
        ans = float("-inf")
        for i in range(0,k+1):
            ans = max(ans,a[idx][i]+dfs(idx+1,taken+i))
            print(idx,i,a[idx][i],"+",dfs(idx+1,taken+i))
            dp[idx][taken]= ans
        return dp[idx][taken]
    
    print("Case #{}: {} ".format(u-t,dfs(0,0)))
    
    
    
    
    
    
    
    
    Recursion visualizer:
    
    
    array [[0, 10, 20, 120, 150], [0, 80, 130, 140, 190]
    n 2
    
    function fn(idx,taken) {
  if (taken==5) return 0
  if (idx >n-1 || taken >5) return -Infinity
  var ans = -Infinity
  var i=0
  for (i = 0; i <= 4; i++) {
  ans= Math.max(ans, array[idx][i]+fn(idx+1,taken+i));
}    
return ans
}


fn(0,0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
