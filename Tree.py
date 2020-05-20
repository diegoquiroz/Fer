"""
@created_by: Diego Quiroz
			 diego00aq@gmail.com
@created: 05-21-2020
@modified: 05-21-2020
"""

class Node: 
	"""Constructor of Node Class, the main component of a tree.

	:param val: any type of data to store inside the node
	:var left: reference to Nodes left child
	:var right: reference to Nodes right child
	"""
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val 


"""Function to insert values as child of a node.

:param root: Node instance to take as the root.
:param node: Node instance to take as the node to evaluate.
:return: if value is already in the tree, return None
"""
def insert(root, node):
	if root.val == node.val:
		return None
	if root is None: 
		root = node
	else: 
		if root.val < node.val: 
			if root.right is None: 
				root.right = node 
			else: 
				insert(root.right, node) 
		else: 
			if root.left is None: 
				root.left = node 
			else: 
				insert(root.left, node)   

"""Function to get the Tree as inorder traversal.

:param root: root Node instance.
"""
def inorder(root):
    if root:
        inorder(root.left) 
        print(root.val)
        inorder(root.right)

"""Function to search a node value.

:param root: root Node instance.
:param 
"""
def search(root, value): 
    if root is None or root.val == value: 
        return root 
    if root.val < value: 
        return search(root.right,value) 
    return search(root.left,value)
