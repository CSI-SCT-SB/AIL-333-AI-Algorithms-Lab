#best first search
#331_gadha lekshmi

def bfs(n,g,visited,c,hvalue,hew,pc):
	print(n)
	l=[]
	if n==g:
			print("goal node reached")
			print("path cost is ",pc)
			return
	for con in c[n]:  #c[n] graph
		if con not in visited:
			l.append(hvalue[con])  #heuristic value of b nd c is appended
	key=l[0] #to find smallest heuristic value
	for i in range(0,len(l)):
		if (l[i]<key):
			key=l[i]
	min=hew[key]
	pc=pc+cost[(n,min)]  #cost(a to b)
	if min not in visited:
		visited.append(min)
		bfs(min,g,visited,c,hvalue,hew,pc)

visited=[]
c={}
hvalue={}
hew={}
cost={}
n=int(input("enter the no.of nodes:"))
for i in range(0,n):
	node=input("enter the value of current node:") #a
	s=int(input("enter the number of child node:"))  #2
	list=[]
	for j in range(0,s):
		a=input("enter connection value:") #for a its b and c
		list.append(a)
		pc=int(input("enter path cost:"))  #cost between a and b
		cost[(node,a)]=pc
	c[node]=list
	h=int(input("enter the heuristic value:"))
	hvalue[node]=h
	hew[h]=node
start=input("enter the start node:")
g=input("enter the goal node:")
pc=0
visited.append(start)
bfs(start,g,visited,c,hvalue,hew,pc)


#output

enter the no.of nodes:6
enter the value of current node:'a'
enter the number of child node:2
enter connection value:'b'
enter path cost:1
enter connection value:'c'
enter path cost:2
enter the heuristic value:2
enter the value of current node:'b'
enter the number of child node:1
enter connection value:'d'
enter path cost:3
enter the heuristic value:3
enter the value of current node:'c'
enter the number of child node:1
enter connection value:'e'
enter path cost:4
enter the heuristic value:5
enter the value of current node:'d'
enter the number of child node:1
enter connection value:'g'
enter path cost:5 
enter the heuristic value:1
enter the value of current node:'e'
enter the number of child node:1
enter connection value:'g'
enter path cost:8
enter the heuristic value:4
enter the value of current node:'g'
enter the number of child node:0
enter the heuristic value:8
enter the start node:'a'
enter the goal node:'g'
a
b
d
g
goal node reached
('path cost is ', 9)
