class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root):
    def dfs(node, depth):
        if not node:
            return
        
        if depth > dfs.max_depth:
            dfs.max_depth = depth
            dfs.leftmost_value = node.val
        
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs.max_depth = -1
    dfs.leftmost_value = None
    
    dfs(root, 0)
    
    return dfs.leftmost_value

## descomente a classe que roda no leetcode.
##class Solution:
##    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
##        return findBottomLeftValue(root)