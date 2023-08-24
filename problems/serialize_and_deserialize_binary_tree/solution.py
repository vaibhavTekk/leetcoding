# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        s = ''
        while queue:
            curr = queue.pop(0)
            if not curr:
                s += '#,'
            else:
                s += str(curr.val)+','
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
        return s[:-1]
        
    def deserialize(self, data):
        if len(data) == 0:
            return None
        vals = data.split(',')
        if vals[0] == '#':
            vals.pop(0)
            return None
        root = TreeNode(int(vals[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if vals[i] != '#':
                left = TreeNode(int(vals[i]))
                node.left = left
                queue.append(left)
            i += 1
            if vals[i] != '#':
                right = TreeNode(int(vals[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root

        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))