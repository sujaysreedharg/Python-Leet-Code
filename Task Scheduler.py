class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in range(0,len(tasks)):
            value = tasks[i]
            if value in freq:
                freq[value]+=1
            else:
                freq[value]=1
        highestfreq=float("-inf")
        for values in freq.values():
            highestfreq = max(highestfreq,values)
        nooftaskswithhighestfreq = 0
        for values in freq.values():
            if values == highestfreq:
                nooftaskswithhighestfreq+=1
        print(highestfreq,n,nooftaskswithhighestfreq)
        print(freq)
        result = (highestfreq -1) * (n+1) + nooftaskswithhighestfreq
        return max(len(tasks),result)
