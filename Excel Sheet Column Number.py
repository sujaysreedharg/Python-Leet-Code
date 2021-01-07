class Solution:
    def titleToNumber(self, s: str) -> int:
        base=26
        value=0
        tots=0
        power=0
        i=len(s)-1
        while i>=0:
            value = ord(s[i])-64
            print(value)
            tots += value * (base ** power)
            print(tots)
            power+=1
            print(power)
            i-=1
            print(i)
        return tots
        
        
        
     Time -> O(n)
     Space -> O(1)
