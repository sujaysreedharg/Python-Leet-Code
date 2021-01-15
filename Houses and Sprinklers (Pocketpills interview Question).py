Given an array of houses and sprinkler positions find the minimum radius such that all the houses are covered by at least one sprinkler.(all the sprinklers will have the same radius)
Houses = [1,4,7]
Sprinkler = [2,5]
Radius = 2.

def getminradius(houses,sprinklers):
        
    i=0
    j=0
    minradius=0
    while i<len(houses)-1:
        difftocurrentnearestsprinkler = abs(houses[i]-sprinklers[j])
        difftonextnearestsprinkler = float("inf")
        if j < len(sprinklers)-1:
            difftonextnearestsprinkler= abs(sprinklers[j+1]-houses[i])
        if difftocurrentnearestsprinkler>difftonextnearestsprinkler:
            j+=1
        minradius = max(minradius,min(difftocurrentnearestsprinkler,difftocurrentnearestsprinkler))
        i+=1
    return minradius
        


print(getminradius([1,4,7],[2,5]))
