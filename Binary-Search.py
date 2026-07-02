#binary search
#recursive -> O(logn) Time | O(logn) Space

arr = [1, 3, 5, 5, 7, 24]
target = 7


def binaryrecursivesearch(arr, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    potentialMatch = arr[mid]
    if target == potentialMatch:
        return True
    elif potentialMatch < target:
        return binaryrecursivesearch(arr, mid + 1, end)
    else:
        return binaryrecursivesearch(arr, start, mid - 1)


print(binaryrecursivesearch(arr, 0, len(arr) - 1))


#iterative -> O(logn) Time | O(1) Space
arr = [1, 3, 5, 5, 7, 24]
target = 242


def binaryrecursivesearch(arr, start, end):
    while start<=end:
        mid=(start+end)//2
        potentialMatch = arr[mid]
        if target == potentialMatch:
            return True
        elif target > potentialMatch:
            start=mid+1
        else:
            end=mid-1
    return False


print(binaryrecursivesearch(arr, 0, len(arr) - 1))
