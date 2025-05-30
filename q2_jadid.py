CONST=1e-9
parents=[]
class Bst:
    class Node:
        def __init__(self, data,left_child,right_child,parent):
            self.data = data
            self.left_child = left_child
            self.right_child = right_child
            self.parent = parent

    def __init__(self):
        self.root=self.Node(CONST,None,None,None)
        self.list_nodes = []

    def insert(self, key):
        if self.root.data == CONST:
            self.root = self.Node(key,None,None,None)
            self.list_nodes.append(self.root)
        else:
            current= self.root
            while(True):
                if  current.data>key:
                    if current.left_child != None:
                        current = current.left_child
                    else :
                        new_node=self.Node(key,None,None,current)
                        current.left_child=new_node
                        parents.append(current.data)
                        break
                else:
                    if current.right_child != None:
                        current = current.right_child
                    else :
                        new_node=self.Node(key,None,None,current)
                        current.right_child=new_node
                        parents.append(current.data)
                        break
            self.list_nodes.append(new_node)


                
    def find_depth(self, node):
        if node is None:
            return -1  
        depth = 0
        while node.parent is not None:
            node = node.parent
            depth += 1
        return depth


    def find_ancestor(self, index1, index2):
        cur1 = self.list_nodes[index1]
        cur2 = self.list_nodes[index2]
        depth_cur1 = self.find_depth(cur1)
        depth_cur2 = self.find_depth(cur2)

        if depth_cur1 > depth_cur2:
            for i in range(depth_cur1 - depth_cur2):
                cur1 = cur1.parent
            while cur1 != cur2:
                cur1 = cur1.parent
                cur2 = cur2.parent
            return self.list_nodes.index(cur1) + 1
        else:
            for i in range(depth_cur2 - depth_cur1):
                cur2 = cur2.parent
            while cur1 != cur2:
                cur1 = cur1.parent
                cur2 = cur2.parent
            return self.list_nodes.index(cur2) + 1

x = input()
lst = []
lst=input()
lst=lst.split()
bst = Bst()
for  i in range(len(lst)):
   bst.insert(int(lst[i]))
#list_parent=bst.print_parents()
'''for i in range(len(list_parent)):
    print(list_parent[i],end = " ")'''
line2=input()

a = int(line2.split()[0]) -1
b = int(line2.split()[1]) -1
for i in range(len(parents)):
    print(parents[i], end = " ")
print()
print(bst.find_ancestor(a,b))