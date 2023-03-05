# python3

import sys
import threading



# Node class for tree
class Node:
    def __init__(self, key):
        self.child_nodes = []
        self.val = key


def compute_height(n, parents):
    # n is the number of nodes
    # parents is a list of parent nodes with -1 for root and n-1 for leaf
    # create a list of nodes
    nodes = [Node(i) for i in range(n)]
    # create a list of child nodes
    for i in range(n):
        if parents[i] == -1:
            root = nodes[i]
        else:
            nodes[parents[i]].child_nodes.append(nodes[i])
    # compute the height of the tree
    max_height = 0
    stack = [(root, 1)]
    while stack:
        node, height = stack.pop()
        if height > max_height:
            max_height = height
        for child in node.child_nodes:
            stack.append((child, height+1))

    return max_height


def main():
    # check test cases from test folder and compare with expected output
    for i in range(1,10):
        with open('test/0{}'.format(i)) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            print(compute_height(n, parents))
            # print answer from .a file
            with open('test/0{}.a'.format(i)) as f:
                print(f.readline())
    for i in range(10, 25):
        with open('test/{}'.format(i)) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            print(compute_height(n, parents))
            # print answer from .a file
            with open('test/{}.a'.format(i)) as f:
                print(f.readline())
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))