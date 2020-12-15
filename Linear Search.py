def linearSearch(nums,num_to_find):
  for index,element in enumerate(nums):
    if element == num_to_find:
      return index
  return -1
numberList = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
num_to_find = int(input())
print(linearSearch(numberList,num_to_find))


//Enter the list size : 5


Enter number at location 0 :
47
Enter number at location 1 :
57
Enter number at location 2 :
69
Enter number at location 3 :
77
Enter number at location 4 :
585
77
3
 
