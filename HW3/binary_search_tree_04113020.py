#練習用測資 5, 3, 3, -5, 8, 7, 10, 6
result = []

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def insert(self, root, val):
        if root == None:
            new_node = TreeNode(val)
            root = new_node
            return root
        
        new_node = TreeNode(val)
        
        if new_node.val <= root.val:
            if root.left == None:
                root.left = new_node
                return root.left
            else:
                self.insert(root.left, new_node.val)
                
        if new_node.val > root.val:
            if root.right == None:
                root.right = new_node
                return root.right
            else:
                self.insert(root.right, new_node.val)
            
    def preorder_traversal(self, root):
        if root.val:
            print(root.val)
        
        if root.left:
            left = self.preorder_traversal(root.left)
            
        if root.right:
            right = self.preorder_traversal(root.right)
            
    def preorder_traversal_2(self, root):
        if root.val:
            print(root.val)
            result.append(root.val)
        
        if root.left:
            self.preorder_traversal(root.left)
            
        if root.right:
            self.preorder_traversal(root.right)

    def is_no_child(self, node):
        if node.left == None and node.right == None:
            print('no child')
            return True
        else:
            return False
        
    def is_a_child(self, node):
        if (node.left == None) and node.right:
            print('left(X), right(O)')
            return True
        if node.left and (node.right == None):
            print('left(O), right(X)')
            return True
        else:
            return False
    
    def is_two_children(self, node):
        if node.left and node.right:
            print('left(O), right(O)')
            return True #發現這裡原本少寫返回布林值
        else:
            return False
    
    def root_right_min_val(self, root):
        if root:
            count = 1
            cur_root = root
            if cur_root.right and count <=1:
                cur_root = root.right
                count+=1
            while cur_root.left:
                cur_root = root.left
        return cur_root
            
    def delete(self, root, target):
        if root == None:
            return None
        
        if target > root.val:
            self.delete(root.right, target)
            
        if target < root.val:
            self.delete(root.left, target)
        else:
        
        #如果整個tree就只有root一個元素的話，直接把該元素改成None
            if self.is_no_child(root) == True:
                root = None

            #如果root有某一邊有子節點，用該節點取代原本的root，這樣原本的root就消失了，然後繼續往下檢查看有沒有符合target的元素
            elif self.is_a_child(root) == True:
                if root.left:
                    root = root.left
                    self.delete(root, target)
                if root.right:
                    root = root.right
                    self.delete(root, target)

            #如果root兩邊都有子節點，先找到在root右子樹中最小的值，用該值取代root，刪除該值原本的節點後，再檢查新的節點是不是target
            elif self.is_two_children(root) == True:
                root.val = self.root_right_min_val(root).val
                root.right = self.delete(root.right, target)
                
        return root
        
    def search(self, root, target):
        if root.val == target:
            print('search root:', root.val)
            return root
        
        if target < root.val:
            self.search(root.left, target)
        
        if target > root.val:
            print('target > root.val')
            print(root.right.val)
            self.search(root.right, target)
            
    def modify(self, root, target, new_val):
        if root:
            if root.val == target:
                root.val = new_val
        
        if root.left:
            self.modify(root.left, target, new_val)
        
        if root.right:
            self.modify(root.right, target, new_val)
            
        return root
 
# Reference: Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson | Former Spotify Engineer | https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/9520088?start=195#content
