list_first = raw_input()
list_00=list_first.split()
p=map(int,list_00)

def avg(d):
    return sum(d)/len(d)

for j in range(len(p)):
    order = False
    i = 0
    while i<len(p)-1:    ## till i is less than length x
        if p[i]>p[i+1]:   ## checking for adjacent elements
            p[i],p[i+1] = p[i+1],p[i]
            order = True
        i = i+1
    if order == False:
        break
print (p)

def middlevalue(thelist):
	if len(thelist)%2 == 0:
    	a= len(thelist)/2
    	b= len(thelist)/2 -1
    	return (thelist[b]+thelist[a])/(2.0)
    else:
    	a = len(thelist)/2
    	return thelist[a]

def high_occuring_value(thelist):
  counts = {}
  for item in thelist:
    counts [item] = counts.get (item, 0) + 1
  maxcount = 0
  maxitem = None
  for k, v in counts.items ():
    if v > maxcount:
      maxitem = k
      maxcount = v
  if maxcount == 1:
    print "No mode"
  elif counts.values().count(maxcount) > 1:
    print maxitem
  else:
    print maxitem , maxcount

print "The mean of the list is :"avg(p)
print "The median of the list is :"middlevalue(p)
print "The mode of the list :"high_occuring_value(x)

