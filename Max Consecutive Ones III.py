class Solution:
    def longestOnes(self, A, K):
        begin=0
        end=0
        n= len(A)
        for end in range(n):
            print("end")
            print(end)
            if A[end]== 0:
                K-=1
                print("K")
                print(K)
            if K<0:
                if A[begin]==0:
                    K+=1
                    print(K)
                begin+=1
                print("begin")
                print(begin)
        return (end-begin+1)


sol = Solution()
print(sol.longestOnes([0,0,1,1,1,0,0], 0))



THE POWER OF FOR LOOP:
    
In 'for' loop iteration statement is written at top, hence, executes only after all statements in loop are executed.	In 'while' loop, the iteration statement can be written anywhere in the loop.    
   


In essence, we are incrementing the size of the window until our number of flips (K) is used up. When it is, we shift the left boundary of the window to alleviate the usage of flips.

we start expanding the "right boundary" of the window from 0 to the right for each iteration of the for loop
whenever a 0 is reached, we decrement K to account for a flip from 0 to 1
when K becomes negative, we increment the index of the "left boundary" regardless
if the number at this left boundary was a 0, we can increment K as we don't need to use one of our flips on this value if it is not in our current window anymore
we return the size of this window









Output:
end
0
K
-1
0
begin
1
end
1
K
-1
0
begin
2
end
2
end
3
end
4
end
5
K
-1
begin
3
end
6
K
-2
begin
4
3
