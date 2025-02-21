# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.recovered_values = set()  # Set to store all recovered values
        self.recover(root, 0)  # Start recovery from the root with value 0
    
    def recover(self, node: TreeNode, value: int):
        if not node:
            return
        node.val = value  # Recover the value for the current node
        self.recovered_values.add(value)  # Add the recovered value to the set
        
        # Recursively recover left and right children
        self.recover(node.left, 2 * value + 1)
        self.recover(node.right, 2 * value + 2)
    
    def find(self, target: int) -> bool:
        # Check if the target is present in the set of recovered values
        return target in self.recovered_values

# # Example Usage:
# # Initialize the tree with contaminated values
# root = TreeNode(-1)
# root.left = TreeNode(-1)
# root.right = TreeNode(-1)

# # Recover the tree
# find_elements = FindElements(root)

# # Test the find function
# print(find_elements.find(1))  # Output: False
# print(find_elements.find(2))  # Output: True



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)