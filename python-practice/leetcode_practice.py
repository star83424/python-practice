class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0, 1, 2]
        for i in range(3, n+1):
            count.append(count[i-2] + count[i-1])
        return count

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev_prev = 0
        result = 0
        for i in range(1, n+1):
            result = prev + prev_prev
            prev_prev = prev
            prev = result
        return result

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            max_wealth = max(max_wealth, sum(customer))
        return max_wealth


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(customer) for customer in accounts])

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, root_path):
            path_list = []

            if root_path is None:
                root_path = str(root.val)
            else:
                root_path = root_path + "->" + str(root.val)

            # It’s a leaf, stop here
            if root.left is None and root.right is None:
                path_list.append(root_path)
                return path_list
            # It's not a leaf
            if root.left is not None:
                path_list.extend(dfs(root.left, root_path))
            if root.right is not None:
                path_list.extend(dfs(root.right, root_path))
            return path_list
        return dfs(root, None)


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        sol = []
        def dfs(root, path):
            path.append(str(root.val))
            # It’s a leaf, stop here
            if root.left is None and root.right is None:
                sol.append("->".join(path))
                return
            if root.left is not None:
                dfs(root.left, path[:])
            if root.right is not None:
                dfs(root.right, path[:])
        dfs(root, [])
        return sol

