
# coding: utf-8

# In[ ]:


def weightedMean(X,W,n) :
    sum = 0
    numWeight = 0
    i = 0
    while  i < n :
         
        numWeight = numWeight + X[i] * W[i]
        sum = sum + W[i]
        i = i + 1
  
    return (float)(numWeight / sum)


# In[ ]:


def print_mode (thelist):
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


# In[ ]:


#sort_list=[]
#for i in range(len(x)):
    #min_value=x[0]
    #if x < min_value:
        #minimum=x
        #sort_list.append(min)
        #x.remove(min)
        
# main()
# if "__name__" ==

