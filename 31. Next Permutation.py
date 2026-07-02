class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(idx1,idx2):
            nums[idx1],nums[idx2]=nums[idx2],nums[idx1]
        def rev(idx1,idx2):
            while idx1<idx2:
                swap(idx1,idx2)
                idx1+=1
                idx2-=1
        if len(nums)==1:
            return
        if len(nums)==2:
            return swap(0,1)
        dec=len(nums)-2
        while dec>=0 and nums[dec] >= nums[dec+1]:
            dec-=1
        rev(dec+1,len(nums)-1)
        if dec==-1:
            return
        next_num = dec+1
        
        while next_num < len(nums) and nums[dec]>=nums[next_num]:
            next_num+=1
        swap(dec,next_num)
