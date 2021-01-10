def quickselect(array,k):
    position=k-1
    return quickselecthelper(array,0,len(array)-1,position)
def quickselecthelper(array,start,end,position):
    while True:
        pivot= start
        left= start+1
        right= end
        while left<=right:
            if array[left]<array[pivot] and array[right]>array[pivot]:
                swap(array,left,right)
            if array[left]>=array[pivot]:
                left+=1
            if array[right]<=array[pivot]:
                right-=1
        swap(array,right,pivot)
        if right == position:
            return array[right],array
        elif right < position:
            start= right+1
        else:
            end=right-1
    

        
def swap(array,left,right):
    array[left],array[right]=array[right],array[left]



print(quickselect([8,5,2,9,7,6,3],3))


For Kth Smallest Element in an array: Change the Relational Operators in the three if loops :D
                    
                    
                    
                  
