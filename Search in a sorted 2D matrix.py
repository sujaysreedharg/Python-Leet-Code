class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col =len(matrix[0])
        left=0
        right = (row*col)-1
        while left<=right:
            mid= (left+right)//2
            rowpos= mid//col
            colpos= mid%col
            if target == matrix[rowpos][colpos]:
                return True
            elif target > matrix[rowpos][colpos]:
                left = mid+1
            else:
                right = mid-1
        return False
        
        
    
