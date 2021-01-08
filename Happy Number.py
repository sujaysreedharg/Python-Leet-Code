class Solution:
    def getsum(self,n): 
        sum=0
        while n:
            d= n%10
            print(d)
            sum+=d**2
            n=n//10
            print(sum)
        return sum
    
    
    def isHappy(self, n: int) -> bool:
        seen =set()
        while n!=1:
            n=self.getsum(n)
            print(n)
            if n in seen:
                return False
            seen.add(n)
            print(seen)
        return True
