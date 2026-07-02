# O(n^3) Tie | O(n) Space
def kSum(array, target):
    array.sort()

    def recursion(array, k, target):
        if len(array) == 0 or array[0] * k > target or array[-1] * k < target:
            return []
        if k == 2:
            return twoSum(array, target)
        result = []
        for i in range(len(array)):
            if i == 0 or array[i - 1] != array[i]:
                for set in recursion(array[i + 1:], k - 1, target - array[i]):
                    result.append([array[i]] + set)
        return result

    def twoSum(array, target):
        i = 0
        j = len(array) - 1
        result = []
        while i < j:
            potentialTarget = array[i] + array[j]
            if potentialTarget == target:
                result.append([array[i]] + [array[j]])
            if potentialTarget > target:
                j -= 1
            else:
                i += 1
        return result

    return recursion(array, 4, target)


print(kSum([1, 0, -1, 0, -2, 2], 0))
