class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        elif n==2:
            return 0
        prime=[True for i in range(0,n+1)]
        prime[0]=False
        prime[1]=False
        p=2
        while(p*p<=n):
            if prime[p]==True:
                for i in range(p*2,n+1,p):
                    prime[i]=False
            p+=1

        count=0
        for p in range(n):
            if prime[p]:
                count+=1
        return count
        
        
        Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
