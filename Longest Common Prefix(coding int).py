firstArr=[25,288,2655,544,54,555]
secArr=[2,255,266,244,26,5,5444444]
firstArr.sort()
secArr.sort()
lcp=0
print(firstArr,"\n",secArr)
for i in range(len(firstArr)-1,-1,-1):
    if lcp >= len(str(secArr[i])):
        break
    for j in range(len(secArr)-1,-1,-1): 
        if lcp >= len(str(secArr[j])):
            break
        
        word1=str(firstArr[i])
        word2=str(secArr[j])
        length=min(len(str(word1)),len(str(word2)))
        k=0
        currLcp=0
        while k<length:
            if word1[k]==word2[k]:
                currLcp+=1
            else:
                break
            k+=1
        lcp = max(lcp,currLcp)
    lcp = max(lcp,currLcp)

print(lcp)
        
            
