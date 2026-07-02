# Maximum Subarray or Kadane's algorithm
arr= [-2,1,-3,4,-1,2,1,-5,4]

def kadane(array):
    maxendinghere=arr[0]
    maxsofar=arr[0]
    for i in range(1,len(arr)):
        maxendinghere = max(maxendinghere+arr[i], arr[i])
        maxsofar= max(maxendinghere,maxsofar)
    return maxsofar


print(kadane(arr))
