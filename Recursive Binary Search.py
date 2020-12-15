
(Reference CodeBasics) :D

def binarySearchrecursive(nums,num_to_find, left_index, right_index):

  if right_index < left_index:
    return -1

  mid_index = (left_index + right_index) // 2
  if mid_index >= len(nums) or mid_index < 0:
    return -1
  
  mid_num = nums[mid_index]
  if mid_num == num_to_find:
    return mid_index
  if mid_num > num_to_find:
    right_index = mid_index - 1 
  else:
    left_index = mid_index + 1
  
  return binarySearchrecursive(nums,num_to_find, left_index,right_index)
  
  

nums = [12, 15, 17, 19, 21, 24, 45, 67]
num_to_find = 15

index = binarySearchrecursive(nums,num_to_find,0, len(nums))
print(f"Number found at index {index} using binary search")



Number found at index 1 using binary search 
