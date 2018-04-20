alist = raw_input("Input your list of munbers : " )
list_01=alist.split()
x=map(int,list_01)

for j in range(len(x)):
	order = False
	i = 0
	while i<len(x)-1:
		if x[i]>x[i+1]:
			x[i],x[i+1] = x[i+1],x[i]
			order = True
		i=i+1
	if order == False:
		break
print (x)

def middlevalue(thelist):
	if len(thelist)%2 == 0:
		a = len(thelist)/2
		b = len(thelist)/2 -1
		return (thelist[b]+thelist[a])/(2.0)
	else:
		a = len(thelist)/2
		return thelist[a]

def quartiles(lst):
	mid = len(lst)/2
	if (len(lst) % 2 == 0):
		lower = middlevalue(lst[:mid])
		upper = middlevalue(lst[mid:])
	else:
		lower = middlevalue(lst[:mid])
		upper = middlevalue(lst[mid+1:])
		return(lower,middlevalue(lst),upper)

print ("The median of list of numbers is" , middlevalue(x))
print ("The quartiles of list are ", quartiles(x))
