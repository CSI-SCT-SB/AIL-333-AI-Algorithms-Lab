class path:
    def __init__(self,path):
        self.path=path
        self.pathCost(g)

    def pathCost(self, g):
        cost = 0
        for i, val in enumerate(self.path[1:]):
            cost += g.graph[self.path[i]][val]
        cost += g.h(self.path[-1])
        self.cost=cost

class graph:
    def __init__(self):
        self.graph = dict()
        self.hur = {}

    def addEdge(self, v, u):
        self.graph[v] = u

    def h(self, a):
        return self.hur[a]

    def aStar(self, s, g):
        pQueue = [[path([s])]]
        finPath=None
        while True: # generation 
            i=pQueue[-1]
            print(i)
            if len(i)==1:
                k=i[0]
                pQueue.remove(i)
            else:
                tmList=[a.cost for a in i]
                k=i[tmList.index(min(tmList))]
                i.remove(k)
            tpList=[]
            for j in self.graph[k.path[-1]]:
                print(k.path+[j])
                tmPath=path(k.path+[j])
                if j==g:
                    if finPath==None or finPath.cost>tmPath.cost:
                        finPath=tmPath
                    elif finPath.cost<tmPath.cost:
                        return finPath
                else:
                    tpList.append(tmPath)
            if tpList!=[]:
                pQueue.append(tpList)
            if pQueue==[]:
                return finPath

g = graph()
for i in range(int(input("No of edges : "))):
	name=input('Name : ')
	childe={}
	for j in range(int(input("No of Children : "))):
		tname=input('Name : ')
		childe[tname]=int(input('Cost : '))
	g.addEdge(name,childe)
	g.hur[name]=int(input('Huristics : '))
	print("###")
s=input("Start node : ")
gol=input("Goal node : ")

finPath=g.aStar(s, gol)
print("A* path from",s,"to",gol,":"," -> ".join(finPath.path),"\nCost :",finPath.cost)
