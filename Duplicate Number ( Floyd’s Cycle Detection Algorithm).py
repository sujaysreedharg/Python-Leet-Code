def findDuplicate(nums):
  tortoise = nums[0]
  hare = nums[0]
  while True:
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
    if tortoise == hare:
      break
  ptr1 =nums[0]
  ptr2 = tortoise
  while ptr1!=ptr2:
    ptr1= nums[ptr1]
    ptr2 =nums[ptr2]
  return ptr1
print(findDuplicate([1,2,3,4,2]))



C:
  
  
  int findDuplicate(int* nums, int numsSize){

    int slow = 0, fast=0,finder =0;
    while(true){
        slow = nums[slow];
        fast = nums[nums[fast]];
        if (slow == fast)
            break;
        
    }
while(true){
    slow = nums[slow];
     finder =  nums[finder];
    if(slow == finder)
        return slow;

}
