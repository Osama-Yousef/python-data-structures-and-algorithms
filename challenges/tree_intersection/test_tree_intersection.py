import pytest
from tree_intersection import tree_intersection, Queue, BinaryTree, _Node, Node

def test_binary_tree():
    tree_one = BinaryTree()
    tree_one.add(12)
    tree_one.add(5)
    tree_one.add(3)
    tree_one.add(15)

    tree_two = BinaryTree()
    tree_two.add(1)
    tree_two.add(5)
    tree_two.add(12)
    tree_two.add(55)

    assert tree_one.root.value == 12
    assert tree_two.root.value == 1
    assert tree_one.root.left.value == 5

def test_tree_intersection():
    tree_one = BinaryTree()
    tree_one.add(12)
    tree_one.add(5)
    tree_one.add(3)
    tree_one.add(15)

    tree_two = BinaryTree()
    tree_two.add(1)
    tree_two.add(5)
    tree_two.add(12)
    tree_two.add(55)

    assert tree_intersection(tree_one, tree_two) == [5, 12]

def test_empty_tree():
    tree_one = BinaryTree()
    tree_one.add(12)
    tree_one.add(5)
    tree_one.add(3)
    tree_one.add(15)

    tree_two = BinaryTree()

    assert tree_intersection(tree_one, tree_two) == []

def test_multiple_matching_values_in_one_tree():
    tree_one = BinaryTree()
    tree_one.add(4)
    tree_one.add(4)
    tree_one.add(4)
    tree_one.add(4)

    tree_two = BinaryTree()
    tree_two.add(12)
    tree_two.add(5)
    tree_two.add(3)
    tree_two.add(15)

    assert tree_intersection(tree_one, tree_two) == []