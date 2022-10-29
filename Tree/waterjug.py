class node:
    def __init__(self,data):
        self.data=data
        self.child=[]

def bfs(root,goal):
    child=[root]
    while child!=[]:
        inode=child[0]
        # print(inode.data)
        if inode.data==goal.data:
            return 1
        else:
            child=child+inode.child
            child.remove(inode)
    return 0

def fillX(inode,X):
    x,y=inode.data
    return node((X,y))

def fillY(inode,Y):
    x,y=inode.data
    return node((x,Y))

def trnsX2Y(inode,X):
    x,y=inode.data
    rCapX=X-x
    prvY=y
    [y]=[prvY-rCapX if prvY-rCapX>0 else 0]
    x+=(prvY-y)
    return node((x,y))

def trnsY2X(inode,Y):
    x,y=inode.data
    rCapY=Y-y
    prvX=x
    [x]=[prvX-rCapY if prvX-rCapY>0 else 0]
    y+=(prvX-x)
    return node((x,y))

def emtX(inode):
    x,y=inode.data
    return node((0,y))

def emtY(inode):
    x,y=inode.data
    return node((x,0))

def wjsol(root,goal,X,Y):
    child=[root]
    while child!=[]:
        inode=child[0]
        print(inode.data)
        for i in range(6):
            if i==0:
                newDat=fillX(inode,X)
            elif i==1:
                newDat=fillY(inode,Y)
            elif i==2:
                newDat=trnsX2Y(inode,X)
            elif i==3:
                newDat=trnsY2X(inode,Y)
            elif i==4:
                newDat=emtX(inode)
            elif i==5:
                newDat=emtY(inode)
            if bfs(root,newDat)==0:
                inode.child.append(newDat)
                if newDat.data == goal[0] or newDat.data == goal[1]:
                    print(newDat.data)
                    return 1
        child=child+inode.child
        child.remove(inode)
    return 0

def main():
    root=node((0,0))
    flag=0
    print("\t\tWelcome to Water jug problem\n\tInputs")
    X=int(input("Capacity of X : "))
    Y=int(input("Capacity of Y : "))
    goal=int(input("Capacity to be obtained : "))
    goalList=[(goal,0),(0,goal)]
    flag=wjsol(root,goalList,X,Y)
    if flag:
        print("Have solution")
    else:
        print("Not have solution")
            

if __name__=="__main__":
    main()