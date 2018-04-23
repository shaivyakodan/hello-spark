list_first = raw_input()
list_00=list_first.split()
p=map(int,list_00)


def mode_of_list (thelist):
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

mode_of_list(p)