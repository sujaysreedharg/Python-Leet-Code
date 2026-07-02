class Solution:
    def isHappy(self, n: int) -> bool:
        res=set()
        while 1:
            x=0
            s=str(n)
            for i in s:
                x+= int(i)**2
            if x==1:
                return True
            if x in res:
                return False
            res.add(x)
            n=x
