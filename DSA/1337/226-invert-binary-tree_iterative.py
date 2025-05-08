# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(node):
    if node == None: return None
    result = node
    stack = []
    stack.append(node)
    while len(stack) > 0:
        node = stack.pop()
        temp = node.left
        node.left = node.right
        node.right = temp
        if node.right != None: stack.append(node.right)
        if node.left != None: stack.append(node.left)

    return result


def bfs_verify(node, correct_order):
    if node == None: return True if correct_order == tuple() else False
    stack = []
    stack.append(node)
    for ptr in range(len(correct_order)):
        stack.append(stack[ptr].left)
        stack.append(stack[ptr].right)
        if stack[ptr].val != correct_order[ptr]:
            return False

    #for n in stack: print(n.val, end=' ') if n != None else print('None')
    return True


assert bfs_verify(invert_binary_tree(
        TreeNode(4,
                 TreeNode(2,
                          TreeNode(1),
                          TreeNode(3)),
                 TreeNode(7,
                          TreeNode(6),
                          TreeNode(9))
        )), (4,7,2,9,6,3,1))

assert bfs_verify(invert_binary_tree(
        TreeNode(2,
                 TreeNode(1),
                 TreeNode(3)
        )), (2,3,1))

assert bfs_verify(invert_binary_tree(None), tuple())
