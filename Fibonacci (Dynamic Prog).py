def bootmupfib(n):
  if n==1 or n==2:
    return 1
  bottomup= [None]*(n+1)
  bottomup[1]=1
  bottomup[2]=1
  for i in range(3,n+1):
    bottomup[i]= bottomup[i-1]+bottomup[i-2]
  return bottomup


print(bootmupfib(20))



O(n) -> Time
