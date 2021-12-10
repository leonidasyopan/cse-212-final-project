class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    def __contains__(self, data):
        return self._contains(data, self.root)

    def _contains(self, data, node):

        if node.data == data:
            return True
        elif data < node.data:
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)
        else:
            if node.right is None:
                return False
            else:
                return self._contains(data, node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def __reversed__(self):
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _left_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._left_height(node.left)

    def _right_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._right_height(node.right)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._left_height(node)
            right_height = self._right_height(node)
            higher = left_height if left_height > right_height else right_height

            return higher


students = BST()

students.insert("Adam Lavigne")
students.insert("Brandon Rogers")
students.insert("Carl Sagan")
students.insert("Dylan Lennon")

print("Please provide the name of the new student")
new_student = input("Enter new student name: ")

students.insert(new_student)

searched_student = input("Enter student name to check: ")

if searched_student in students:
    print(searched_student + " is already in the list.")
else:
    print(searched_student + " is NOT in the list yet. Please add him/her")
