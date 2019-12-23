import pytest
from fizz_buzz_tree import BinaryTree, fizz_buzz_func, fizz_buzz_tree, _Node

def test_creating_and_adding_to_BinaryTree():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15

@pytest.fixture()
def ten_tree():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(3)
    tree.add(6)
    tree.add(15)
    tree.add(90)
    tree.add(16)
    tree.add(101)
    tree.add(1)
    tree.add(3000)
    return tree

def test_pytest_fixture(ten_tree):
    assert ten_tree.root.value == 10
    assert ten_tree.root.left.left.value == 3
    assert ten_tree.root.right.right.left.value == 16
    assert ten_tree.root.right.right.right.value == 101
    assert ten_tree.root.right.right.right.right.value == 3000


