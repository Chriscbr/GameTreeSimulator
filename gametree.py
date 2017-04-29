class GameTree:
    """Class that represents a game tree for any given type of game state."""

    def __init__(self, initial_state=None, tree=None):
        if (initial_state is not None and tree is not None)\
                or (initial_state is None and tree is None):
            raise Exception('Invalid arguments to GameTree constructor.')
        elif initial_state is not None:
            self._root = self.generate_tree(initial_state)
        else:
            self._root = tree

    # returns the root
    def get_root(self):
        return self._root

    # generates a tree given an initial state
    @staticmethod
    def generate_tree(initial_state):
        def generate_subtree(tree_node):
            next_states = tree_node.data.get_next_states()
            children = []
            for state in next_states:
                if state.is_goal_state():
                    children.append(TreeNode(state))
                else:
                    children.append(generate_subtree(TreeNode(state)))
            new_tree = TreeNode(tree_node.data, children)
            return new_tree

        tree = generate_subtree(TreeNode(initial_state))
        return tree

    def __repr__(self):
        return 'GameTree({r})'.format(r=self._root.data)

    def __str__(self):
        return str(self._root)

    def __eq__(self, other):
        return self._root == other.get_root()


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

    def __eq__(self, other):
        return self.data == other.data and set(self.children) == set(other.children)

    def __hash__(self):
        return hash((self.data,) + tuple(self.children))
