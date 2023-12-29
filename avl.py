# worked
import copy
import json

# working
def rotate_left(root):
    temp = root
    root = root.right
    temp.right = root.left
    root.left = temp
    return root

# working
def rotate_right(root):
    temp = root
    root = root.left
    temp.left = root.right
    root.right = temp
    return root

def do_rotations(root):
    root.compute_bf()
    if root.balance_factor == 2:
        if root.right is not None and root.right.balance_factor == -1:
            root.right = rotate_right(root.right)
        root = rotate_left(root)
    elif root.balance_factor == -2:
        if root.left is not None and root.left.balance_factor == 1:
            root.left = rotate_left(root.left)
        root = rotate_right(root)
    root.compute_bf()
    return root

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.balance_factor = 0

    # I haven't used this yet
    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right

    def obj(self):
        return dict(
            value=self.value,
            # bf=self.balance_factor,
            left=None if self.left is None else self.left.obj(),
            right=None if self.right is None else self.right.obj(),
        )

    def __str__(self):
        return json.dumps(self.obj())

    def insert(self, node):
        # node = Node(value)
        if node.value >= self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        elif node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        self.compute_bf()
        # # check rights
        if self.right is not None:
            self.right = do_rotations(self.right)
            # self.compute_bf()

        # # check lefts
        if self.left is not None:
            self.left = do_rotations(self.left)
            # self.compute_bf()
    
    def compute_bf(self):
        h_left, h_right = 0, 0
        if self.left is not None:
            h_left = self.left.height()
        if self.right is not None:
            h_right = self.right.height()
        
        self.balance_factor = h_right - h_left
        # print(69, self.value, self.balance_factor)

    def height(self):
        h_left, h_right = 0, 0
        if self.left is not None:
            h_left = self.left.height()
        if self.right is not None:
            h_right = self.right.height()
        return max(h_left, h_right) + 1
    
    def rotation(self):
        # to-do: rotation
        pass

class AVLTree:
    def __init__(self, root=None):
        
        self.root = root
        if root is not None:
            if not isinstance(root, Node):
                raise TypeError("Root MUST be Node type.")
            self.root.compute_bf()

    def __del__(self):
        self.root = None

    def is_balanced(self):
        if self.root is None:
            return True
        else:
            self.root.compute_bf()
            return abs(self.root.balance_factor) < 2

    def __str__(self):
        return str(self.root)
    
    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        self.root = do_rotations(self.root)
    
    def height(self):
        if self.root is None:
            return 0
        else:
            return self.root.height()