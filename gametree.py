class GameTree:
    """Class that represents a game tree for any given type of gamestate."""

    def __init__(self, initial_state=None):
        if initial_state is None:
            self._initial_state = None
            self._tree = None
        else:
            self._initial_state = initial_state
            self._tree = self.generate_tree(initial_state)

    @staticmethod
    def generate_tree(initial_state):
        tree = GameTree.generate_subtree(TreeNode(initial_state))
        return tree

    @staticmethod
    def generate_subtree(tree_node):
        next_states = tree_node.data.get_next_states()
        children = []
        for state in next_states:
            children.append(GameTree.generate_subtree(TreeNode(state)))
        new_tree = TreeNode(tree_node.data, children)
        return new_tree

    def __repr__(self):
        return 'gametree.GameTree({i})'.format(i=self._initial_state)

    def __str__(self):
        return str(self._tree)


class TreeNode:
    """Class that represents a tree node.

    A tree node is a data object associated with 0 or more children
    which are defined recursively as tree nodes."""

    def __init__(self, data=None, children=None):
        self.data = data
        if children is None:
            self.children = []
        else:
            self.children = children

    def __str__(self):
        """code adapted from http://stackoverflow.com/questions/1649027/"""

        def indent_premade_string(string, prefix):
            parts = string.split('\n')
            new_parts = [parts[0]] + list(map(lambda x: prefix + x, parts[1:]))
            new_string = '\n'.join(new_parts)
            return new_string

        output = ''
        stack = [[self]]
        while len(stack) > 0:
            child_stack = stack[-1]
            if len(child_stack) == 0:
                stack.pop()
            else:
                tree = child_stack.pop(0)
                indent = ''
                for i in range(0, len(stack) - 1):
                    indent += '| ' if len(stack[i]) > 0 else '  '
                output += indent + '+-' + indent_premade_string(str(tree.data), indent + ' -') + '\n'
                if len(tree.children) > 0:
                    stack.append(tree.children)
        return output
