from ttt_gamestate import TTTGameState
from gametree import TreeNode, GameTree


def test_treenode_str():
    grandchild_d = TreeNode('grandchild_d')
    grandchild_e = TreeNode('grandchild_e')
    child_a = TreeNode('child_a')
    child_b = TreeNode('child_b', [grandchild_d, grandchild_e])
    child_c = TreeNode('child_c')
    root = TreeNode('root', [child_a, child_b, child_c])
    assert str(root) == ('+-root\n'
                         '  +-child_a\n'
                         '  +-child_b\n'
                         '  | +-grandchild_d\n'
                         '  | +-grandchild_e\n'
                         '  +-child_c\n')


def test_gametree_generate():
    root_state = TTTGameState([1, 2, 1, 0, 0, 2, 1, 2, 1], 1)
    gt0 = GameTree(root_state)
    grandchild = TreeNode(TTTGameState([1, 2, 1, 2, 1, 2, 1, 2, 1], 1))
    child1 = TreeNode(TTTGameState([1, 2, 1, 2, 0, 2, 1, 2, 1], 0), [grandchild])
    child2 = TreeNode(TTTGameState([1, 2, 1, 0, 2, 2, 1, 2, 1], 0))
    root = TreeNode(root_state, [child1, child2])
    gt1 = GameTree(tree=root)
    assert gt0 == gt1


def gametree_generate_complete():
    t0 = TTTGameState()
    gt = GameTree(t0)
    f = open('test_output.txt', 'w')
    f.write(str(gt))
    f.close()
