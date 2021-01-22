class Node:
    def __init__(self,name):
        self.children = []
        self.name = name
    def addchild(self,name):
        self.children.append(Node(name))
    def dfsgraph(self,array):
        array.append(self.name)
        for child in self.children:
            child.dfsgraph(array)
        return array
    def bfsgraph(self,array):
        queue=[self]
        
        while len(queue)>0:
            current=queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


new= Node("A")
new.addchild("B")
new.addchild("C")
new.addchild("D")
new.children[0].addchild("E")
new.children[0].addchild("F")
new.children[0].children[1].addchild("I")
new.children[0].children[1].addchild("J")
print(new.dfsgraph([]))
print(new.bfsgraph([]))

