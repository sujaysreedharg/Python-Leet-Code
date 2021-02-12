Botto-up:

def fib(n):
    dp = [0 for i in range(n+1)]
    dp[0]= 0
    dp[1]=1
    if n==0:
        return dp[0]
    if n==1:
        return dp[1]
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]
print(fib(10))



O(n) -> Time



Top-down:

  
  
n=int(input())

def fib(n,dp):
    
    if dp[n] is not None:
        return dp[n]
    if n==1 or n==2:
        return 1
    result= fib(n-1,dp)+fib(n-2,dp)
    dp[n]=result
    print(dp)
    return result
def findfib(n):
    dp = [None for i in range(n+1)]
    return fib(n,dp)
print(findfib(10))
