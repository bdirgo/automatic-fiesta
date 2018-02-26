class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent

class Tree:
    def __init__(self, root, parent=None):
        self.root = Node(root, parent)
        self.child = []

    def __str__(self):
        rv = []
        rv.append(self.root.val)
        for i,v in enumerate(self.child):
            rv.append(self.child[i].parent)
        return str(rv)

    def getRoot(self):
        return self.root.val

    def addChild(self, val, parent):
        self.child.append(Node(val, parent))


def rootOf(parent):
    for i in parent:
        if parent[i] == i:
            return i

def changeRoot(parent, newRoot):

    t = Tree(parent[rootOf(parent)])
    t.addChild(1, 0)
    t.addChild(2, 0)
    t.addChild(3, 1)

    print(t)

changeRoot([0, 0, 0, 1], 1) # [1, 1, 0, 1]
changeRoot([0, 0, 0, 1, 1, 1, 2, 2, 7], 7) # [2, 0, 7, 1, 1, 1, 2, 7, 7]
changeRoot([0, 0, 0, 1, 1, 1, 2, 2, 7, 7], 2) # [2, 0, 2, 1, 1, 1, 2, 2, 7, 7]
changeRoot([3, 3, 2, 2, 0], 0) # [0, 3, 3, 0, 0]

changeRoot([8, 6, 8, 8, 7, 6, 8, 8, 8, 7], 7) # [8, 6, 8, 8, 7, 6, 8, 7, 7, 7]
changeRoot([5, 3, 0, 5, 10, 5, 5, 0, 10, 10, 0, 13, 3, 3, 2], 8) # [10, 3, 0, 5, 10, 0, 5, 0, 8, 10, 8, 13, 3, 3, 2]
changeRoot([5, 18, 18, 1, 19, 19, 0, 2, 4, 2, 11, 11, 1, 1, 5, 2, 18, 4, 4, 11], 2) # [5, 18, 2, 1, 18, 19, 0, 2, 4, 2, 11, 19, 1, 1, 5, 2, 18, 4, 2, 4]
changeRoot([21, 20, 24, 7, 1, 13, 0, 13, 20, 12, 2, 20, 20, 12, 12, 0, 24, 10, 12, 1, 20, 20, 1, 7, 12], 10) # [21, 20, 10, 7, 1, 13, 0, 13, 20, 12, 10, 20, 24, 12, 12, 0, 24, 10, 12, 1, 12, 20, 1, 7, 2]




