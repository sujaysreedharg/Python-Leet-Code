def isPalindrome(string):
  leftptr =0
  rightptr=len(string)-1
  while leftptr < rightptr:
    if (string[leftptr]!= string[rightptr]):
      return False
    leftptr+=1
    rightptr-=1
  return True
print(isPalindrome('abcdcba'))
