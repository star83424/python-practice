from collections import deque
def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


class SortUtils:

    @staticmethod
    def bubble_sort(nums):
        print(f'start sorting {nums}')
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j+1]:
                    swap(nums, j, j+1)
        return nums

    @staticmethod
    def selection_sort(nums):
        print(f'start sorting {nums}')
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            swap(nums, i, min_index)
        return nums

    @staticmethod
    def insertion_sort(nums):
        print(f'start sorting {nums}')
        ans = [nums[0]]
        for i in range(1, len(nums)):
            for j in range(len(ans)):
                if nums[i] < ans[j]:
                    ans.insert(j, nums[i])
                    break
                if j == len(ans)-1:
                    ans.append(nums[i])

        return ans

    @staticmethod
    def quick_sort(nums):
        print(f'start sorting {nums}')
        left, right, pivot = 0, len(nums)-2, len(nums)-1

        while True:
            while left < pivot and nums[left] <= nums[pivot]:
                left += 1

            while right > left and nums[right] >= nums[pivot]:
                right -= 1

            # print(nums)
            if left < right:
                # print(f'swap {left}(val:{nums[left]}) with {right}(val:{nums[right]})')
                swap(nums, left, right)
            else:
                swap(nums, pivot, left)
                # print(f"swap pivot {pivot} at {left}: {nums}")
                if left > 0:
                    nums[0: left] = SortUtils.quick_sort(nums[0: left])
                if left < len(nums)-2:
                    nums[left+1:] = SortUtils.quick_sort(nums[left+1:])
                return nums
        return nums

    @staticmethod
    def merge_sort(nums):
        print(f'start sorting {nums}')
        length = len(nums)
        if length < 2:
            return nums

        left = SortUtils.merge_sort(nums[0: int(length/2)])
        right = SortUtils.merge_sort(nums[int(length/2):])

        ans, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        if i < len(left):
            ans.extend(left[i:])
        if j < len(right):
            ans.extend(right[j:])
        return ans

    @classmethod
    def heap_sort(cls, nums):
        print(f'start sorting {nums}')

        # build the heap : n^n
        cls.__build_heap(nums)
        print(f'__build_heap: {nums}')

        # pop out the first one & heapify down to maintain the heap
        for i in range(len(nums)-1, -1, -1):
            cls.__pop(nums, i)
            cls.__heapify(nums, 0, i)

        return nums

    @classmethod
    def __build_heap(cls, nums):
        # Heapify all none leaves nodes from bottom to top
        for i in range(int(len(nums)/2), -1, -1):
            cls.__heapify(nums, i, len(nums))

    @staticmethod
    def __heapify(nums, i, length):
        max_index = i
        left = i*2 + 1
        if left < length and nums[left] > nums[max_index]:
            # left child might be the max
            max_index = left

        right = (i+1) * 2
        if right < length and nums[right] > nums[max_index]:
            # right child is the max
            max_index = right

        # Need swap
        if max_index != i:
            nums[i], nums[max_index] = nums[max_index], nums[i]
            # keep on heapify-ing down
            SortUtils.__heapify(nums, max_index, length)

    @staticmethod
    def __pop(nums, i):
        print(f'pop{nums[0]}')
        # fake pop: swap the popped one with the last one
        nums[i], nums[0] = nums[0], nums[i]


class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

"""
            0
    1               2
3       4       5       6



[3, 1, 5, 3, 4, 2, 1, 6, 7, 8, 4, 10, 12, 8, 9, 0, 11]

                    12
            11              10
        7       8       5        9
      6   1    4  4   3  2      8  1
    0  3


[0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12]
"""


def queue():
    que = deque([1, 2, 3])
    print(que.popleft())