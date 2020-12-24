class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask =0xffffffff
        while b!=0:
            sum = (a ^ b)& mask
            carry =  (( a & b)<<1) & mask
            a = sum
            b = carry
        if (a >> 31):
            return ~( a^ mask)
        return a
        
        
        
        
        Sum of two int without using the  + sign
        
        
        
        
