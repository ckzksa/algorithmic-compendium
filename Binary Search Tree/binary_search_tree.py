class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.left = None
        self.right = None
        self.value = value
    
    def __str__(self) -> str:
        parent_value = self.parent.value if self.parent else None
        left_value = self.left.value if self.left else None
        right_value = self.right.value if self.right else None
        return f"Parent={parent_value}[{id(self.parent)}]   Self={self.value}[{id(self)}]   Left={left_value}[{id(self.left)}]   Right={right_value}[{id(self.right)}]"

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value, duplicates=False, recursive=False):
        if recursive:
            return self.recursive_insert(self.root, value)
        
        parent = None
        child = self.root
        
        while child is not None:
            parent = child
            if not duplicates and value == child.value:
                return child
            elif value < child.value:
                child = child.left
            else:
                child = child.right
                
        node = Node(parent, value)
        if parent is None:
            self.root = node
        elif value < parent.value:
            parent.left = node
        else:
            parent.right = node
        return node
    
    def recursive_insert(self, node, value, duplicates=False):
        if node is None:
            return Node(value)

        if not duplicates and value == node.value:
            return node
        elif value < node.value:
            node.left = self.recursive_insert(node.left, value)
        elif value > node.value:
            node.right = self.recursive_insert(node.right, value)
        return node
    
    def search(self, value, recursive=False):
        if recursive:
            return self.recursive_search(self.root, value)
        
        node = self.root
        while node is not None and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node
    
    def recursive_search(self, node, value):
        if node is None or node.value == value:
            return node

        if node.value < value:
            return self.recursive_search(node.right, value)
        return self.recursive_search(node.left, value)

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(2)
    bt.insert(4)
    bt.insert(6)
    bt.insert(8)
    
    print(bt.search(6))
    print(bt.search(9))
    print(bt.search(5))
    print(bt.search(7))