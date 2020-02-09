def find_first_equal_k(tree, k):
    subtree, first = tree, None
    while subtree:
        if subtree.data == 0:
            return subtree
        elif subtree.data > k:
            subtree = subtree.left
        else:
            subtree = subtree.right
    return None
