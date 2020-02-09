class BSTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def printBST(self):
        if self.left:
            self.left.printBST()
        print(self.data, end=' ')
        if self.right:
            self.right.printBST()


def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        return max(lDepth, rDepth) + 1


def build_min_height_bst_from_sorted_array(A):
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return BSTNode(A[mid], build_min_height_bst_from_sorted_subarray(start, mid), build_min_height_bst_from_sorted_subarray(mid + 1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(A))


a = [9, 2, 3, 7, 5, 11, 47, 53, 43, 41, 31, 37, 23, 17]

# build_min_height_bst_from_sorted_array(sorted(a)).printBST()
tree = build_min_height_bst_from_sorted_array(sorted(a))
print(maxDepth(tree))
print(tree.data)
