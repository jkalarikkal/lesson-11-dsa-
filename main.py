class Tree:
    def __init__(self, h):
        self.data = h
        self.left = None
        self.right = None

def Inorder(root):
    if root is not None:
        if root.left is not None:
            Inorder(root.left)
        print(root.data)
        if root.right is not None:
            Inorder(root.right)

def Inserty(root, x):
    if root == None:
        return Tree(x)
    if root.data > x:
        root.left = Inserty(root.left, x)
    else:
        root.right = Inserty(root.right, x)
    return root

def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    if key > root.data:
        root.right = delete(root.right, key)
    else:
        #case1 - no child
        if root.right is None and root.left is None:
            return None
        #case2- 1 child
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #case3 - 2 child

        temp = MinValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def MinValueNode():
    current = node
    while current.left is not None:
        current = current.left
    return current


userin = int(input("How many elements do you want in your tree: "))
root = None
for i in range(userin):
    num = int(input("What number do you want: "))
    root = Inserty(root,num)

what = input("What would you like to do: ")
if what == "Inorder":
    Inorder(root)
elif what == "Delete":
    userin2 = int(input("What number would you like to delete: "))
    root = delete(root, userin2)
    

'''
print("BST before deletion")
Inorder(root)

userin2 = int(input("What number would you like to delete: "))
root = delete(root, userin2)

print("BST after deletion:")
Inorder(root)
'''
