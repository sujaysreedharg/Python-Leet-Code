class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        people = (i for i,seat in enumerate(seats) if seat)
        prev,future = None, next(people)
        ans=0
        for i,seat in enumerate(seats):
            if seat:
                prev=i
            else:
                while future is not None and future <i:
                    future = next(people,None)
                left = float("inf") if prev is None else i - prev
                right = float("inf") if future is None else future - i
                ans =  max(ans, min(left,right))
        return ans
                
    
   Time Complexity: O(N) where NN is the length of seats.

Space Complexity: O(1)

 
    
    
    Java:                    ( Pre increment is available in java but in python we use generators to access only when we need people so that future will not be equal to the next index( its not required) 
    and error wont show up as list index out of range because of generate[next index in while loop will not exist] due to the unnecessary incrementation of future. Simple way: ++i is not equal to i++ 
    class Solution {
    public int maxDistToClosest(int[] seats) {
        int N = seats.length;
        int prev = -1, future = 0;
        int ans = 0;

        for (int i = 0; i < N; ++i) {
            if (seats[i] == 1) {
                prev = i;
            } else {
                while (future < N && seats[future] == 0 || future < i)
                    future++;

                int left = prev == -1 ? N : i - prev;
                int right = future == N ? N : future - i;
                ans = Math.max(ans, Math.min(left, right));
            }
        }

        return ans;
    }
}
