def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


# Driver code 
A = [900] 
B = [10, 13,56, 14] 
n = len(A) 
m = len(B) 

# we need to define the 
# smaller array as the 
# first parameter to make 
# sure that the time complexity 
# will be O(log(min(n,m))) 

print ("The median is : {}".format(median(A, B))) 

# Time : O(log(min(n,m))




# simple but not   O(log(min(n,m))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        l = len(nums1)
        if l%2==0:
            return (nums1[int(l/2)-1]+nums1[int(l/2)])/2
        else:
            return nums1[int(l/2)]
           
            
            
            


