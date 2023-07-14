l=list(map(int,input().split()))
cummulativeSum=[]
cummulativeSum.append(l[0])
for i in l[1:]:
    cummulativeSum.append(cummulativeSum[-1]+i)
length=len(cummulativeSum)
index=-1
for i in range(1,length):
    if cummulativeSum[i-1]==cummulativeSum[length-1]-cummulativeSum[i]:
        index=i
        break
print(index)
