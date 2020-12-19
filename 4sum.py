def sumquadruplets(array, t):
  array.sort()
  result =[]
  for i in range(0, len(array)):
    for j in range(i+1, len(array)):
      startptr = j+1
      endptr=len(array)-1
      target = t-array[i] - array[j]
      while(startptr<endptr):
        total = array[startptr]+array[endptr]
        if(total==target):
          result.extend((array[i],array[j],array[startptr],array[endptr]))
          return result
        elif (total > target):
          endptr-=1
        else:
          startptr+=1
      
print(sumquadruplets([2,7,4,0,9,5,1,3],20))
