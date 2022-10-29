import sys

class node:
    def __init__(self,data):
        self.data=data
        self.child=[]

# n8=node(8)
# n9=node(9)
# n1=node(1)
# n6=node(6)
# n10=node(10)
# root.child=[n8,n9]
# n8.child=[n1,n6]
# n9.child=[n10]
# n1.child=[node(12)]
# n6.child=[node(99)]
# n10.child=[node(44),node(2)]

def dfs(root,goal):
    child=[root]
    while child!=[]:
        inode=child[0]
        # print(inode.data)
        if(inode.data==goal):
            return 1
        else:
            child=inode.child+child
            child.remove(inode)
    return 0

def insert(root):
    newDat=int(input("Node Value : "))
    flag=dfs(root,newDat)
    if flag:
        print("Duplicate node")
    else:
        childOf=int(input("Child of : "))
        child=[root]
        while child!=[]:
            inode=child[0]
            if(inode.data==childOf):
                inode.child.append(node(newDat))
                print("New node inserted")
                return
            else:
                child=child+inode.child
                child.remove(inode)
        print("Parent node not found")

def main():
    root=node(5)
    while 1:
        choice=int(input("\tMenu\n1 Insert\n2 DFS\n3 Exit\n your choice : "))
        if(choice==1):
            insert(root)
        elif(choice==2):
            flag=dfs(root,int(input("Enter goal node : ")))
            if flag:
                print("Goal node found")
            else:
                print("Goal node not found")
        else:
            sys.exit()

if __name__=="__main__":
    main()