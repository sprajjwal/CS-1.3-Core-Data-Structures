#!python
from queue import Queue


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return not self.is_leaf()

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best: O(1) if the node is a leag
        Worst: O(log n) if there are n items and node is root"""
        if self.is_leaf() :
            return 0
        else:
            if self.left is None:
                return 1 + self.right.height()
            elif self.right is None:
                return 1 + self.left.height()
            else:
                return 1 + max(self.left.height(), self.right.height())


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best: O(1) if root is a leaf
        Worst:O(logn) if root is not a leaf"""
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(1) if item at root
        Worst case running time: O(logn) if item not in tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(1) if item at root
        Worst case running time: O(logn) if item is not in tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time:  O(1) if inserting at root
        Worst case running time: O(log n) if inserting anywhere else"""
        # Handle the case where the tree is empty
        new_node = BinaryTreeNode(item)
        if self.is_empty():
            self.root = new_node
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # Check if the given item should be inserted left of parent node
        if item < parent.data and parent.left is None:
            # Create a new node and set the parent's left child
            parent.left = new_node
            self.size += 1
        # Check if the given item should be inserted right of parent node
        elif item > parent.data and parent.right is None:
            # TODO: Create a new node and set the parent's right child
            parent.right = new_node
            self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(1) item at root
        Worst case running time: O(logn) item not in tree"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            #  Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            #  Check if the given item is less than the node's data
            elif node.data > item:
                #  Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif node.data < item:
                #  Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(1) if item at root
        Worst case running time: O(logn) if item is not in the tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif node.data == item:
            # Return the found node
            return node
        #  Check if the given item is less than the node's data
        elif node.data > item:
            return self._find_node_recursive(item, node.left)
        #  Check if the given item is greater than the node's data
        elif node.data < item:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(1) if item at root
        Worst case running time: O(logn) if item is not in tree"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            #  Check if the given item is less than the node's data
            elif node.data > item:
                #  Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif node.data < item:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        if node.data == item:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif node.data > item:
            # Recursively descend to the node's left child, if it exists
            return node if node.left is None else self._find_parent_node_recursive(item, node.left, node)  # Hint: Remember to update the parent parameter
        # Check if the given item is greater than the node's data
        elif node.data < item:
            return node if node.right is None else self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since there are n nodes
        Memory usage: O(h) since item from every node at the same height is being added to call stack"""
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)
            # Visit this node's data with given function
            visit(node.data)
            # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)
        # node = self.root
        
        # while node != None:


    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since there are n nodes
        Memory usage: O(h) since item from every node at the same height is being added to call stack"""
        #  Visit this node's data with given function
        if node is not None:
            visit(node.data)
            #  Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
            #  Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since there are n nodes
        Memory usage: O(h) since item from every node at the same height is being added to call stack"""
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # Visit this node's data with given function
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since there are n nodes
        Memory usage: O(2^depth) since item from every node is being added to queue"""
        # Create queue to store nodes not yet traversed in level-order
        queue = Queue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            #  Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
