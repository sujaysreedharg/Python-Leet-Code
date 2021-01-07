class Solution:
    def swap(self,nums,index1,index2):
        temp = nums[index1]
        nums[index1]=nums[index2]
        nums[index2]=temp
    def reverse(self,nums,beginidx,endidx):
        while beginidx<endidx:
            self.swap(nums,beginidx,endidx)
            beginidx+=1
            endidx-=1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return 
        if len(nums)==2:
            return self.swap(nums,0,1)
        decrement = len(nums)-2
        while decrement>=0 and nums[decrement]>= nums[decrement+1]:
            decrement-=1
        self.reverse(nums,decrement+1,len(nums)-1)
        if decrement==-1:
            return
        next_number =decrement+1
        while nums[next_number]<=nums[decrement] and next_number<len(nums):
            next_number+=1
        self.swap(nums,decrement,next_number)
       
        
    Time -> O(n)
    Space -> O(1)
