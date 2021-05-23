import sys

from binary_search_tree import Node


def add_one(node, n):
    if node is None:
        # this will change node from same reference to a new var with another id address
        # no more by reference
        node = Node(1)
    print(f'1 node id : {id(node)}, number id: {id(n)}')
    print(f'1 node: {node.val}, number: {n}')
    node.val += 1
    n += 1
    print(f'2 node id : {id(node)}, number id: {id(n)}')
    print(f'2 node: {node.val}, number: {n}')
    node = Node(node.val)
    print(f'3 node id : {id(node)}, number id: {id(n)}')
    print(f'3 node: {node.val}, number: {n}')
    node.val += 1
    n += 1
    print(f'4 node id : {id(node)}, number id: {id(n)}')
    print(f'4 node: {node.val}, number: {n}')


def one_and_node_one():
    try:
        n = 1
        node = None
        print(f'node id : {id(node)}, number id: {id(n)}')
        add_one(node, n)
        print(f'node id : {id(node)}, number id: {id(n)}')
        print(f'node: {node.val}, number: {n}')
        # Result: node stays None, 1 stays 1.

        # throw error
        raise NameError("Test a NameError")
    except AttributeError:
        # catch specific type of error
        print("Error: ", sys.exc_info()[1])
    except NameError:
        print("Error: ", sys.exc_info()[1])
    except:
        # catch universal type of error
        print("Unknown error!", sys.exc_info()[0])


def one_and_none():
    node = Node(1)
    n = 1
    print(f'node id : {id(node)}, number id: {id(n)}')
    add_one(node, n)
    print(f'node id : {id(node)}, number id: {id(n)}')
    print(f'node: {node.val}, number: {n}')
    # Result: only node will change its value, 1 stays 1.
