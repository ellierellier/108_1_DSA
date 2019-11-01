# Linked Structure for Binary Tree

## 想法
- 先建立節點，節點的屬性有:`index`, `left`, `right`, `val`
- 節點可以執行的動作: `count_len`算長度(也可以視為 `find_height` ), `add_left` or `add_right`新增左右節點, `insert`在指定位置插入節點, `del`刪除節點, `replace`覆蓋節點原本的值
  
## Practice
```python
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def replace_left(self, new_node):
    self.left. = 

  def add_left(self, node):
    if self.left == None:
      self.left = node
    elif:
      self.replace_left(node)
# class BinaryTree:
```
