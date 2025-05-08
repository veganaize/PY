# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert(node):
    if node == None: return node
    temp = node.left
    node.left = node.right
    node.right = temp
    invert(node.left)
    invert(node.right)
    return node


def verify(tree, correct_order):
    if tree == None: return True if correct_order == tuple() else False

    def bfs(actual_order, i):
        if i == len(correct_order): return True
        if actual_order[i].val != correct_order[i]: return False
        if actual_order[i].left != None: actual_order += actual_order[i].left,
        if actual_order[i].right != None: actual_order += actual_order[i].right,
        return bfs(actual_order, i+1)

    return bfs((tree,), 0)


assert verify(invert(
        TreeNode(4,
                 TreeNode(2,
                          TreeNode(1),
                          TreeNode(3)),
                 TreeNode(7,
                          TreeNode(6),
                          TreeNode(9))
        )), (4,7,2,9,6,3,1))

assert verify(invert(
        TreeNode(2,
                 TreeNode(1),
                 TreeNode(3)
        )), (2,3,1))

assert verify(invert(None), tuple())
