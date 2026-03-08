import sys

n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = (left, right)

def preorder_traverse(tree, root, preorder):
    if root == '.':
        return preorder
    left, right = tree[root]
    preorder.append(root)
    preorder_traverse(tree, left, preorder)
    preorder_traverse(tree, right, preorder)
    return preorder

def inorder_traverse(tree, root, inorder):
    if root == '.':
        return inorder
    left, right = tree[root]
    inorder_traverse(tree, left, inorder)
    inorder.append(root)
    inorder_traverse(tree, right, inorder)
    return inorder

def postorder_traverse(tree, root, postorder):
    if root == '.':
        return postorder
    left, right = tree[root]
    postorder_traverse(tree, left, postorder)
    postorder_traverse(tree, right, postorder)
    postorder.append(root)
    return postorder

preorder = []
preorder_traverse(tree, 'A', preorder)

inorder = []
inorder_traverse(tree, 'A', inorder)

postorder = []
postorder_traverse(tree, 'A', postorder)

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
