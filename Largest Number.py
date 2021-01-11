class Solution:
    def largestNumber(self, nums):
        if not any(map(bool,nums)):
            return "0"
        if len(nums)<2:
            return "".join(map(str,nums))
        i=0
        j=1
        while i<len(nums):
            while j<len(nums):
                num1="".join(str(nums[i])+str(nums[j]))
                num2="".join(str(nums[j])+str(nums[i]))
                if int(num2) > int(num1):
                    self.swap(nums,i,j)
                j+=1
            i+=1
            j=i+1
            
        return "".join(map(str,nums))
    def swap(self,nums,i,j):
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
