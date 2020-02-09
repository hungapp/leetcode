from sample_bst import root


def find_k_largest_in_bst(tree, k):
    def find_k_largest_in_bst_helper(tree):
        # perform reverse inorder traversal

        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)

    return k_largest_elements


print(*find_k_largest_in_bst(root, 3))
