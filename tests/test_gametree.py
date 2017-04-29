import pytest
import ttt_gamestate
import gametree


def test_treenode_str():
    grandchild_d = gametree.TreeNode('grandchild_d')
    grandchild_e = gametree.TreeNode('grandchild_e')
    child_a = gametree.TreeNode('child_a')
    child_b = gametree.TreeNode('child_b', [grandchild_d, grandchild_e])
    child_c = gametree.TreeNode('child_c')
    root = gametree.TreeNode('root', [child_a, child_b, child_c])
    assert str(root) == ('+-root\n'
                         '  +-child_a\n'
                         '  +-child_b\n'
                         '  | +-grandchild_d\n'
                         '  | +-grandchild_e\n'
                         '  +-child_c\n')


def test_gametree_generate():
    t0 = ttt_gamestate.TTTGameState([1, 2, 1, 0, 0, 2, 1, 2, 1], 1)
    gt = gametree.GameTree(t0)
    print(gt)


def test_gametree_generate_complete():
    t0 = ttt_gamestate.TTTGameState()
    gt = gametree.GameTree(t0)
    f = open('test_output.txt', 'w')
    f.write(str(gt))
    f.close()
