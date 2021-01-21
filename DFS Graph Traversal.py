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

new= Node("A")
new.addchild("B")
new.addchild("C")
new.addchild("D")

new.children[0].addchild("E")
new.children[0].children[0].addchild("I")
new.children[0].children[0].addchild("J")




print(new.dfsgraph([]))
