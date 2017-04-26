class GameTree:
    """Class that represents a game tree for any given type of gamestate."""

    def __init__(self, initial_state):
        self.tree = self.generate_tree(initial_state)

    @staticmethod
    def generate_tree(initial_state):
        tree = TreeNode(initial_state)
        return tree

    @staticmethod
    def generate_substree(tree_node):
        pass


class TreeNode:
    """Class that represents a tree."""

    def __init__(self, data=None, children=None):
        self.data = data
        if children is None:
            self.children = []
        else:
            self.children = children
