# python3

import sys
import threading
import numpy


class Node:
    def ieksa(self, key):
        self.child_nodes = []
        self.val = key


def compute_height(n, parents):
    # Write this function
    nodes = [Node(i) for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            sakne = nodes[i]
        else:
            nodes[parents[i]].child_nodes.append(nodes[i])

    max_height = 0
    stack = [(sakne, 1)]
    while stack:
        node, height = stack.pop()
        if height > max_height:
            max_height = height
        for child in node.child_nodes:
            stack.append((child, height+1))


    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    for i in range(1,10):
        with open('test/0{}'.format(i)) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            print(compute_height(n, parents))

            with open('test/0{}.a'.format(i)) as f:
                print(f.readline())
    for i in range(10,25):
        with open('test/{}'.format(i)) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            print(compute_height(n, parents))

            with open('test/{}.a'.format(i)) as f:
                print(f.readline())
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))