def smallestdifference(arrayone,arraytwo):
  arrayone.sort()
  arraytwo.sort()
  indexone = 0
  indextwo = 0
  smallestdiff = float("inf")
  currentdiff = 0
  result = []
  while indexone < len(arrayone) and indextwo < len(arraytwo):
    firstnum = arrayone[indexone]
    secondnum = arraytwo[indextwo]
    if firstnum < secondnum:
      currentdiff = secondnum - firstnum
      indexone+=1
    elif firstnum > secondnum:
      currentdiff = firstnum - secondnum 
      indextwo+=1
    else:
      return [firstnum,secondnum]
    if smallestdiff > currentdiff:
      smallestdiff = currentdiff
      result = [firstnum, secondnum]
  return result
print(smallestdifference([-1,5,10,20,28,3],[26,134,135,15,17]))


O(nlog(n) + mlog(m)) -> Time
O(1) -> Space
