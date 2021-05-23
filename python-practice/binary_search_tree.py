class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        print(f'val: {self.val}, left: "{self.left}, right: {self.right}')


def build_binary_search_tree(nums):
    root = None
    for i in nums:
        root = build_tree_node(root, i)
    return root


def build_tree_node(root, i):
    if root is None:
        return Node(i)

    if i >= root.val:
        if root.right is None:
            root.right = Node(i)
        else:
            root.right = build_tree_node(root.right, i)
    else:
        if root.left is None:
            root.left = Node(i)
        else:
            root.left = build_tree_node(root.left, i)
    return root


def traversal(root):
    if root is None:
        return
    traversal(root.left)
    root.print()
    traversal(root.right)

#
# def self_then_children(root):
#     if root is None:
#         return
#     root.print()
#     self_then_children(root.left)
#     self_then_children(root.right)


def binary_search_in_sorted_list(nums, target, i = None, j = None):
    if i is None:
        i = 0
    if j is None:
        j = len(nums)

    if i == j:
        print(f"Cannot find {target}!")
        return

    center = int((i+j) / 2)
    if target == nums[center]:
        print(f"{target} found!")
    elif target > nums[center]:
        binary_search_in_sorted_list(nums, target, center+1, j)
    else:
        binary_search_in_sorted_list(nums, target, i, center)

"""

                0
        1               2
    3       4       5       6
    
    left: i*2 +1
    right (i+1)*2


"""