class Node():
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Insertion

def insertKey(node, key):
    if node==None:
        root = Node(key)
        return
    q = []
    q.append(node)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        if temp.left==None:
            temp.left = Node(key)
            return 
        else:
            q.append(temp.left)
        if temp.right==None:
            temp.right = Node(key)
            return 
        else:
            q.append(temp.right)

# Deletion

def deleteDeepest(root, node):
    q=[]
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp==node:
            temp=None
            return
        if temp.right:
            if temp.right==node:
                temp.right=None
                return
            q.append(temp.right)
        if temp.left:
            if temp.left==node:
                temp.left==None
                return
            q.append(temp.left)
            

def delete_node(root, key):
    key_node =  None
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.data==key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        key_node.data = temp.data
        deleteDeepest(root, temp)
    return root

def level_order_traversal(root):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        print(temp.data)
        
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    
    

# Inorder traversal

def inorder(node):
 
    if (not node):
        return
 
    inorder(node.left)
    print(node.data,end = " ")
    inorder(node.right)    

# Postorder

def postOrder(node):
    if not node:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=" ")

# Preorder

def preOrder(node):
    if not node:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)

# Sum Tree

def sum_tree(node):
    if not node:
        return 0
    node.data = sum_tree(node.left) + node.data + sum_tree(node.right)
    return node.data

# Depth of tree

def depth_tree(node):
    if not node:
        return 0
    
    return max(depth_tree(node.left), depth_tree(node.right))+1

# Depth of node

def depth_node(node, key):
    if not node:
        return -1
    
    depth = -1

    if node.data==key:
        print("keyyyy")
        return depth+1
    
    depth = depth_node(node.left, key) 
    if depth>=0:
        return depth+1
    # depth = -1
    depth = depth_node(node.right, key) 
    if depth>=0:
        return depth+1
    return -1



# Check if cousins or siblings

def is_sibling(root, n1, n2):
    print("if sibling")
    if not root:
        return 
    temp = root
    q=[]
    q.append(temp)

    while len(q):
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        if temp.left.data==n1 and temp.right.data==n2:
            return True
        if temp.left.data==n2 and temp.right.data==n1:
            return True
    return False

def check_cousins(root, n1, n2):
    print("checking cousins ", n1, n2)
    d1 = depth_node(root, n1)
    d2 = depth_node(root, n2)
    print(d1, d2)
    if d1 != d2:
        print("depth not equal", depth_node(root,n1), depth_node(root, n2))
        return False
    return not is_sibling(root, n1, n2)
    

# Divide into equal trees

def equal_divide(root):
    if not root:
        return 
    temp = root
    q=[]
    q.append(temp)

    while len(q):
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

        print(depth_tree(temp), depth_tree(temp.left), depth_tree(temp.right))

        if depth_tree(temp.right)+1==depth_tree(temp.left):
            print("Cutting along {} and {}".format(temp.data, temp.left.data))
            return True
        
        if depth_tree(temp.left)+1==depth_tree(temp.right):
            print("Cutting along {} and {}".format(temp.data, temp.right.data))
            return True
    return False



# root = Node(10)
# root.left = Node(11)
# root.left.left = Node(7)
# root.right = Node(9)
# root.right.left = Node(15)
# root.right.right = Node(8)

# sum_tree(root)
# print("\n")
# inorder(root)
# print("*")
# print(check_cousins(root, 8, 7))

root = Node(5)
root.left = Node(1)
root.right = Node(6)
root.left.left = Node(3)
root.left.left = Node(3)
root.right.left = Node(7)
root.left.left.right = Node(0)
root.right.right = Node(4)


print("****", depth_node(root, 15))
print(check_cousins(root, 5, 4))
print(equal_divide(root))
