p=2**31
class Solution:
    def reverse(self, x: int):
            if(x < (2)**31) :
                if (x<0):
                    x=x*-1
                    rev=0 
                    while(x>0): 
                        dig=x%10 
                        rev=rev*10+dig 
                        x=x//10
                    if rev >p-1 or rev<-p:
                        return 0
                    else:
                        return rev*-1
                elif (x>0):
                    rev=0 
                    while(x>0): 
                        dig=x%10 
                        rev=rev*10+dig 
                        x=x//10
                    if rev > p-1 or rev<-p:
                        return 0
                    else:
                        return rev
                else:
                    return 0
            else:
                return 0







// 


Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
