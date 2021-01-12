# I'm using binarytree module from PyPI -- pip install binarytree
# But the basic algorithm goes like this:

# ...
# 1. Traverse tree and find the first element, remember this path (as list)
# 2. Traverse tree and find the second element, remember this path
# 3. The lowest common ancestor is the cross-point between the two paths/lists (by comparing the reversed paths of the two).
# ...

from binarytree import tree, get_parent

def find_path(tree, node):
    # assume node exists in tree
    path = []
    current_node = node
    while current_node != None:
        temp = current_node
        path.insert(0, current_node)
        current_node = get_parent(tree, current_node)
        if current_node == None:
            if temp != tree[0]:
                path.pop(0)
            break

    return path


def solve(tree, first, second):
    rs = None
    
    # assume #1 and #2 nodes exist in tree

    path_first = find_path(tree, first)
    print(path_first)
    path_second = find_path(tree, second)
    print(path_second)

    if (len(path_first) == 0 or len(path_second) == 0):
        return rs

    for i in range(len(path_first)-1,0,-1):
        for j in range(len(path_second)-1,0,-1):
            if path_first[i] == path_second[j]:
                rs = path_first[i];

    return rs

