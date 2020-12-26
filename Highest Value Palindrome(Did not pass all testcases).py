def highestValuePalindrome(s, n, k):
    
    
    left=0
    right=n-1
    newlist=list(s)
    hashset = [None]*n
    while left<=right:
        
        if newlist[left]!=newlist[right]:
                    
            
            if newlist[left]>  newlist[right]:
                
                
                newlist[right]=newlist[left]
                hashset[right]=1
            else:
                
                
                newlist[left]=newlist[right]
                hashset[left]=1
            k-=1
        left+=1
        right-=1 
    
    if k<0:
        return '-1'
    
    
    left=0
    right=n-1
    
    
    while left <= right:
        
        
        
        if left==right and k>=1:
            
            
            newlist[left]='9'
            break
        if newlist[left]< '9':
            if hashset[left]==0 and hashset[right]==0 and k>=2:
                
                
                newlist[left]=newlist[right]='9'
                k-=2
            
            
            if  (hashset[left]==1 or hashset[right]==1) and k>=1:
                
                
                newlist[left]=newlist[right]='9'
                k-=1
            
        left+=1
        right-=1

    return "".join(newlist)
print(highestValuePalindrome('9849',4,1))
