def longpalindrmesubstring(string):
  currentlongest=[0,1]
  for i in range(1,len(string)):
    odd = getlongestpalindrome(string,i-1,i+1)
    even = getlongestpalindrome(string,i-1,i)
    longest= max(odd,even,key= lambda x : x[1] -x[0])
    currentlongest= max(currentlongest,longest,key= lambda x : x[1]-x[0])
  return string[currentlongest[0] : currentlongest[1]]
def getlongestpalindrome(string,left,right):
  while left>=0 and right<len(string):
    if string[left]!=string[right]:
      break
    else:
      left-=1
      right+=1
  return (left+1,right)
print(longpalindrmesubstring("daccac"))



O(n^2) -> Time
O(1) -> Space



















Complexity Analysis

Time complexity : O(n^2) 

Space complexity : O(n^2)
