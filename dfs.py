#331_gadha lekshmi
#DFS
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
# Check for the visisted and unvisited nodes
flag=0
def dfs(graph, start, goal, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    if start==goal:
    	flag=1
    	print("goal found")
        exit(1)
        return visited
    else:
        for next in graph[start] - visited:
            dfs(graph, next, goal, visited)
        return visited
    if flag==0 :
    	print("goal not found")

gdict={}
n=int(input("Enter number of vertices:"))
for i in range(n):
    print("Enter vertice",i+1)
    x=input()
    st=set()
    print("Enter number of adjacent nodes for",x)
    n1=int(input())
    for j in range(n1):
        print("Enter adjacent node",j+1)
        str=input()
        st.add(str)
    gdict[x]=st
    
goal=input("Enter goal node:")
start=input("Enter starting node:")
print(gdict)
dfs(gdict, start, goal)
