list_first = raw_input()
list_00=list_first.split()
p=map(int,list_00)

list_weights = raw_input()
list_01=list_weights.split()
q=map(int,list_01)

def weightedMean(X,W,n) :
    sum = 0
    numWeight = 0
    i = 0
    while  i < n :
         
        numWeight = numWeight + X[i] * W[i]
        sum = sum + W[i]
        i = i + 1
  
    return (float)(numWeight / sum)


weightedMean(p,q,len(q))


