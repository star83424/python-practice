# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from none_zero_relative_order import NoneZeroRelativeOrderList
from sorting import Sorting
from binary_search_tree import BST
from call_by_sharing_practice import CallBySharing
from args_kwargs import ArgsKargs


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
    case1 = [3, 1, 5, 3, 4, 2, 1, 6, 7, 8, 4, 10, 12, 8, 9, 0, 11]
    # 2021/05/09
    # print_hi('PyCharm')
    # print_list()

    # 2021/05/09
    # NoneZeroRelativeOrderList.main()

    # 2021/05/09
    # Sorting.main(case1)

    # 2021/05/10
    # print(operate(1.0, 3, add))
    # print(operate(1, 3.0, multiple))
    # Sorting.main(case1)

    # 2021/05/15
    # BST.main(case1)
    # CallBySharing.main()

    # 2021/05/23
    # ArgsKwargs.main()

    vec = [-4, -2, 0, 2, 4]
    gen = (x * 2 for x in vec)
    print(type(gen))
    print(type([gen]))






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
