class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=len(nums)
        def rev(start,end):
            while start<end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start+=1
                end-=1
            return nums
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
        
        
        
     
