# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

"""
@staticmethod
  Static method does not receive an implicit first argument.

Notice:
    Python doesn’t support method overloading like C++ or Java so we use class methods to create factory methods.
"""


class RelativeOrderSolver:

    @staticmethod
    def relative_order_one_by_one(num_list):
        print(f'relative_order_one_by_one: {num_list}')

        none_zero_index = len(num_list) - 1
        while none_zero_index >= 0:
            if num_list[none_zero_index] != 0:
                break
            none_zero_index -= 1

        while none_zero_index >= 0:
            print("looping")
            zero_index = none_zero_index - 1
            while none_zero_index >= 0:
                if num_list[zero_index] == 0:
                    break
                zero_index -= 1

            if zero_index < 0:
                break

            num_list[zero_index: none_zero_index] = num_list[zero_index + 1: none_zero_index + 1]
            num_list[none_zero_index] = 0
            none_zero_index -= 1

        print(f'result: {num_list}')
        print('-----------------------------------')
        return num_list

    @staticmethod
    def relative_order(num_list):
        print(f'relative_order: {num_list}')

        none_zero_index = len(num_list) - 1
        while none_zero_index >= 0:
            if num_list[none_zero_index] != 0:
                break
            none_zero_index -= 1

        while none_zero_index >= 0:
            print("looping")
            zero_index = none_zero_index - 1
            zero_count = 0
            while zero_index >= 0:
                if num_list[zero_index] == 0:
                    zero_count += 1
                elif zero_count > 0:
                    break
                zero_index -= 1

            if zero_count == 0:
                break
            else:
                if zero_index < 0:
                    zero_index = 0
                else:
                    zero_index += 1

            num_list[zero_index: none_zero_index - zero_count+1] \
                = num_list[zero_index + zero_count: none_zero_index + 1]
            num_list[none_zero_index-zero_count + 1: none_zero_index + 1] = [0]*zero_count
            none_zero_index -= zero_count

        print(f'result: {num_list}')
        print('-----------------------------------')
        return num_list


def solve_relative_order():
    case1 = [0, 1, 0, 3, 2, 0, 4, 0, 7, 0, 0, 5, 8, 0, 9, 0]
    case2 = [0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
    RelativeOrderSolver.relative_order(case1[:])
    RelativeOrderSolver.relative_order_one_by_one(case1[:])

    RelativeOrderSolver.relative_order(case2[:])
    RelativeOrderSolver.relative_order_one_by_one(case2[:])