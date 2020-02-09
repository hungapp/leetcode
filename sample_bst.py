class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:  # self.data == data
                self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=' ')
        if self.right:
            self.right.printTree()

# t = bintrees.RBTRee([(19, 'A'), (7, 'B'), (3, 'C'), (2, 'D'),
#                      (5, 'E'), (11, 'F'), (17, 'G'), (13, 'H'),
#                      (43, 'I'), (23, 'J'), (37, 'K'), (29, 'L'),
#                      (31, 'M'), (41, 'N'), (43, 'I'), (47, 'O'),
#                      (53, 'P')])


root = Node(19)
root.insert(2)
root.insert(3)
root.insert(7)
root.insert(5)
root.insert(11)
root.insert(47)
root.insert(53)
root.insert(43)
root.insert(41)
root.insert(31)
root.insert(37)
root.insert(23)
root.insert(17)
