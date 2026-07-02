# Upperbound: O(n^2*n!) Time |  O(n*n!) Space (Non-backtracking recursive  method)
def permutations(array,currperm=[],finalperms=[]):
    if len(array)==0 and len(currperm):
        finalperms.append(currperm)
    else:
        for i in range(len(array)):
            newArr = array[:i] + array[i+1:]
            newPerms= currperm + [array[i]]
            permutations(newArr,newPerms,finalperms)
    return finalperms        


print(permutations([1,2,3]))

# O(n*n!) Time |  O(n*n!) Space (backtracking recursive  method)
def permutations(i,array,finalperms):
    if i==len(array)-1:
        finalperms.append(array[:])
    else:
        for j in range(i,len(array)):
            swap(array,i,j)
            permutations(i+1,array,finalperms)
            swap(array,i,j)
    return finalperms
def swap(array,i,j):
    array[i],array[j] = array[j],array[i]
print(permutations(0,[1,2,3],[]))
