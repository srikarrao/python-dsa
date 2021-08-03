class Node:

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_value(self, value):
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


root = Node(None, None, -1)


class BST:

    def insert(self, value):
        global root

        if root.get_value() == -1:
            root.set_value(value)
        else:
            self.__insert_node(root, Node(None, None, value))
        return root

    def __insert_node(self, parent, node):
        if parent.get_value() > node.get_value():
            if parent.get_left() is None:
                parent.set_left(node)
            else:
                self.__insert_node(parent.get_left(), node)
        else:
            if parent.get_right() is None:
                parent.set_right(node)
            else:
                self.__insert_node(parent.get_right(), node)

    def get_tree(self):
        return root
