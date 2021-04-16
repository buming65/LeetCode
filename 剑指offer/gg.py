import sys
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []

class Tree:
    def __init__(self):
        self.x = collections.defaultdict(TreeNode)


def helper(node, arrs, tree):

    for c in arrs:
        # print(c)
        curr = TreeNode(c)
        node.children.append(curr)
        tree.x[c] = curr

def find(root, toFind):
    if not root or len(toFind) == 0:
        return None
    flag = False
    if (root.val in toFind):
        toFind.remove(root.val)
        if (len(toFind) == 0 or not toFind):
            return root
        flag = True

    for c in root.children:
        n = len(toFind)
        node = find(c, toFind)
        if not toFind or len(toFind) == 0:
            if flag:
                return root
            else:
                return node
        elif n != len(toFind):
            flag = True
    return None

def solution(root, virus):
    node = find(root, virus)
    print(node.val)

# def find(root, toFind, k):
#     if not root or root.val in toFind:
#         return root
#     count = 0
#     res = None
#     for c in root.children:
#         node = find(c, toFind, k)
#         if node:
#             count += 1
#             res = node
#     if count == k:
#         return root
#     return res
#
# def solution(root, virus):
#     n = len(virus)
#     node = find(root, virus, n)
#     print(node.val)

if __name__ == '__main__':
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    r = int(line[1])
    virus = sys.stdin.readline().strip().split()
    virus = virus[1:]

    root = TreeNode(0)
    tree = Tree()
    tree.x[0] = root

    for i in range(r):
        line = sys.stdin.readline().strip().split()
        line = [int(num) for num in line]

        # node = TreeNode(line[0])
        arrs = line[2:]
        node = tree.x[line[0]]
        helper(node, arrs, tree)

    virus = [int(num) for num in virus]
    # print(virus)

    solution(root, virus)

