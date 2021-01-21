class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        row = len(matrix)-1
        col = 0
        while row>=0 and col <len(matrix[0]):
            print(matrix[row][col])
            if matrix[row][col] > target:
                row-=1
            elif matrix[row][col] < target:
                col+=1
            else:
                return True
        return False
        
        
        
Time -> O(n+m)


Intuition behind the problem:

It is given that rows and columns are sorted. So the optimal way should involved binary search / complexity can be optimized to logarithmic.
In any search problem, the basic motive is to reduce the decision space progressively. The more aggressively the search space is reduced, the more efficient the algorithm.
To reduce decision space means to eliminate certain portion completely from search in future. Here, due to the property of rows & columns being sorted, we can verify that we can utilise the given properties to reduce search space only if we begin at bottom left corner or top right corner. This is because at only those two starting positions, we would be able to exercise decisions to reduce our decision/search space in both directions i.e.
i. if we start at bottom left corner => we can go right to get elements in increasing order & top to get elements in decreasing order.
ii. if we start at top right corner => we can go left to get elements in decreasing order & bottom to get elements in increasing order.
We can't have both choices if we start at top left or bottom right indices.
