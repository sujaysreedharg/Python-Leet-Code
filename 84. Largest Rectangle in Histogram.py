class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  
        n =len(heights)
        left =[0]*n
        right = [0]*n
        
        stack=[]
        for i in range(len(heights)):
            if len(stack)==0:
                left[i]=0
                stack.append(i)
            else:
                while len(stack)!=0 and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if len(stack)==0:
                    left[i] = 0
                else:
                    left[i] = stack[-1] +1
                stack.append(i)
        while len(stack)!=0:
            stack.pop()
        for i in range(len(heights)-1,-1,-1):
            if len(stack)==0:
                right[i]=n-1
                stack.append(i)
            else:
                while len(stack)!=0 and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if len(stack)==0:
                    right[i] = n-1
                else:
                    right[i] = stack[-1] -1
                stack.append(i)   
        print(left,right)
        mx_area = 0
        for i in range(len(heights)):
            mx_area = max(mx_area,heights[i]* (right[i] - left[i] + 1))
        return mx_area
        
        
        
        
        
        
        
        
                    
        
