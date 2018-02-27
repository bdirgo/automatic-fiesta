# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def addChild(self, obj):
#         self.children.append(obj)


# Turns out they were NOT asking me to re-implement a N-ary tree
#
# class Tree:
# 	def __init__(self, data, parent=None):
# 		self.data = data
# 		self.children = []

# 	def __str__(self):
# 		return str([x.data for x in self.children])

# 	def __iter__(self):
# 		for child in self.children:
# 			yield child.data

# 	def addChild(self, val):
# 		self.children.append(Tree(val))


def oldRootOf(parent):
	for i in parent:
		if parent[i] == i:
			return i
def findNewRoot(parent, oldRoot, pos, val):
	if val != oldRoot:
		parent[pos], pos, val = val, parent[pos], pos
		findNewRoot(parent, oldRoot, pos, val)

def changeRoot(parent, newRoot):
	oldRoot = oldRootOf(parent)
	findNewRoot(parent, oldRoot, newRoot, newRoot)
	# t = Tree(parent[oldRootOf(parent)])
	# for i, v in enumerate(parent):
		# t.addChild(v)
	# for i in t.children:
	#     print(i.data)

	return parent


changeRoot([0, 0, 0, 1], 1)
# [1, 1, 0, 1]
changeRoot([0, 0, 0, 1, 1, 1, 2, 2, 7], 7)
# [2, 0, 7, 1, 1, 1, 2, 7, 7]
changeRoot([0, 0, 0, 1, 1, 1, 2, 2, 7, 7], 2)
# [2, 0, 2, 1, 1, 1, 2, 2, 7, 7]
changeRoot([3, 3, 2, 2, 0], 0)
# [0, 3, 3, 0, 0]
changeRoot([8, 6, 8, 8, 7, 6, 8, 8, 8, 7], 7)
# [8, 6, 8, 8, 7, 6, 8, 7, 7, 7]
changeRoot([5, 3, 0, 5, 10, 5, 5, 0, 10, 10, 0, 13, 3, 3, 2], 8)
# [10, 3, 0, 5, 10, 0, 5, 0, 8, 10, 8, 13, 3, 3, 2]
changeRoot([5, 18, 18, 1, 19, 19, 0, 2, 4, 2, 11, 11, 1, 1, 5, 2, 18, 4, 4, 11], 2)
# [5, 18, 2, 1, 18, 19, 0, 2, 4, 2, 11, 19, 1, 1, 5, 2, 18, 4, 2, 4]
changeRoot([21, 20, 24, 7, 1, 13, 0, 13, 20, 12, 2, 20, 20, 12, 12, 0, 24, 10, 12, 1, 20, 20, 1, 7, 12], 10)
# [21, 20, 10, 7, 1, 13, 0, 13, 20, 12, 10, 20, 24, 12, 12, 0, 24, 10, 12, 1, 12, 20, 1, 7, 2]


