# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from none_zero_relative_order import solve_relative_order
from sorting import SortUtils
from binary_search_tree import *
from call_by_sharing_practice import *
from args_kwargs import *


def add(a, b):
    return a + b


def multiple(a, b):
    return a * b


def operate(a, b, operation):
    print(type(a))
    print(type(b))
    print(type(operation))
    return operation(a, b)


if __name__ == '__main__':
    """ Main """
    # 2021/05/09
    # print_hi('PyCharm')
    # print_list()

    # 2021/05/09
    # solve_relative_order()
    case1 = [3, 1, 5, 3, 4, 2, 1, 6, 7, 8, 4, 10, 12, 8, 9, 0, 11]

    # 2021/05/09
    # print(SortUtils.bubble_sort(case1[:]))
    # print("----")
    # print(SortUtils.selection_sort(case1[:]))
    # print("----")
    # print(SortUtils.insertion_sort(case1[:]))
    # print("----")
    # print(SortUtils.quick_sort(case1[:]))
    # print("----")
    # print(SortUtils.merge_sort(case1[:]))
    # ----------------------------------------------------------

    # 2021/05/10
    # print(operate(1.0, 3, add))
    # print(operate(1, 3.0, multiple))

    # for i in range(20 - 1, -1, -1):
    #     print(i)

    # print("----")
    # print(SortUtils.heap_sort(case1[:]))

    # 2021/05/15
    # root = build_binary_search_tree(case1)
    # traversal(root)

    # Binary search
    # test = [8, 2, 4, 1, 3]
    # print(test)
    # SortUtils.heap_sort(test)
    # print(test)
    # binary_search_in_sorted_list(test, 5)

    # one_and_node_one()

    #2021/05/23
    kw = {'k1': 10, 'k2': 11}
    # print("------------")
    # fun(1, kw)
    # print("------------")
    # fun(1, *kw)
    # print("------------")
    # fun(1, **kw)
    # print("------------")
    # fun(1, *kw.values())

    # fun_sep_kws_with_star(1, 2, kw2=4, kw1=3, kw3=5)  # 1 2 3 4
    # fun_sep_kws_with_args_and_then_kwargs(1, 2, 3, 4, 5, kw1=6, kw2=7, kw3=8, kw4=9)
    # fun_sep_kws_with_args_and_then_kwargs(1, 2, 3, 4, 5, kw1=6, kw3=7, kw2=8, kw4=9)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
