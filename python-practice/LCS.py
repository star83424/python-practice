
def print_array(array):
    for row in array:
        print(row)
    print("\n")


def longest_common_substring(l1, l2):
    lcs = [[0 for i in range(len(l2))] for j in range(len(l1))]
    print_array(lcs)
    max_length = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                if i == 0 or j == 0:
                    lcs[i][j] = 1
                else:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                max_length = max(max_length, lcs[i][j])
            else:
                lcs[i][j] = 0
    print_array(lcs)
    print(f"max LCS:{max_length}")


def longest_common_subsequence(l1, l2):
    lcs = [[0 for j in range(len(l2))] for i in range(len(l1))]

    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                if i == 0 or j == 0:
                    lcs[i][j] = 1
                else:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                if i == 0 and j == 0:
                    lcs[i][j] = 0
                elif i == 0:
                    lcs[i][j] = lcs[i][j - 1]
                elif j == 0:
                    lcs[i][j] = lcs[i - 1][j]
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    print_array(lcs)
    print(f"LCS max length:{lcs[-1][-1]}")


def longest_palindromic_substring(l):
    seq = ["."]
    for ch in l:
        seq.append(ch)
        seq.append(".")
    print(seq)

    index = 0
    max_len = 0

    for i in range(len(seq)):
        if len(seq) - i <= max_len:
            break

        length = 1
        while i - length >= 0 and i + length < len(seq):
            if seq[i - length] == seq[i + length]:
                length += 1
            else:
                break
        if length > max_len:
            index = i
            max_len = length

    print(index, max_len)
    print("".join(ch for ch in seq[index-max_len+1: index+max_len] if ch != "."))


class LCS:
    @staticmethod
    def main():
        x = "GeeksforGeeks"
        y = "GeeksQuiz"

        s1 = [2, 5, 7, 9, 3, 1, 2]
        s2 = [3, 5, 3, 2, 8]
        # longest_common_substring(x, y)

        # longest_common_subsequence(x, y)
        # longest_common_subsequence(s1, s2)

        longest_palindromic_substring("a")

        longest_palindromic_substring("abbs")

        longest_palindromic_substring("aaaaaa")


# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if root is None:
#             return True
#         return traversal(root, None, True)[1]
#
#     def traversal(self, root: TreeNode, cur_max, is_BST):
#         # left hand
#         if root.left is not None:
#             (cur_max, is_BST) = traversal(root.left, cur_max, is_BST)
#             if not is_BST:
#                 return (cur_max, is_BST)
#
#         # self val
#         if cur_max is None:
#             cur_max = root.val
#         elif root.val >= cur_max:
#             cur_max = root.val
#         else:
#             is_BST = False
#             return (cur_max, is_BST)
#
#         # right hand
#         if root.right is not None:
#             (cur_max, is_BST) = traversal(root.right, cur_max, is_BST)
#         return (cur_max, is_BST)


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        col_sum = sum(i for i in range(1, 10))/3
        print(col_sum)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 5:
                    continue

                pass = True

                # horizontal sum
                for x in range(i-1, i+2):
                    if sum(grid[x][j-1:j+2]) != col_sum:
                        pass = False
                        break
                if not pass:
                    continue

                # check vertical sum
                for y in range(j-1, j+2):class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        col_sum = sum(i for i in range(1, 10))/3
        print(col_sum)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 5:
                    continue

                pass = True

                # horizontal sum
                for x in range(i-1, i+2):
                    if sum(grid[x][j-1:j+2]) != col_sum:
                        pass = False
                        break
                if not pass:
                    continue

                # check vertical sum
                for y in range(j-1, j+2):
                    if sum(grid[i-1:i+2][y]) != col_sum:
                        pass = False
                        break
                if not pass:
                    continue

                # check cross sum
                if sum(grid[i-1][j-1], grid[i][j], grid[i+1][j+1])  != col_sum:
                    continue
                if sum(grid[i-1][j+1], grid[i][j], grid[i+1][j-1])  != col_sum:
                    continue

                count += 1

        return count
                    if sum(grid[i-1:i+2][y]) != col_sum:
                        pass = False
                        break
                if not pass:
                    continue

                # check cross sum
                if sum(grid[i-1][j-1], grid[i][j], grid[i+1][j+1])  != col_sum:
                    continue
                if sum(grid[i-1][j+1], grid[i][j], grid[i+1][j-1])  != col_sum:
                    continue

                count += 1

        return count

