# HW4: Hash Table & Hash Function原理/流程圖/學習歷程
陳汶穗｜巨資四B｜04113020


# Hash Table & Hash Function原理
## What is a Hash table?
> 先從了解字典概念開始理解hash table。
### Dictionary
- 字典($Dictionary$)是一種由`key`和`value`組成的資料結構。
    - `key`可以理解成區別/識別資料的唯一值，
    - `value`可理解為某種/組資料。
    - 若想找到某組特定的資料`value`，找出資料`value`對應的`key`即可，可以用相對簡單的方式找到想要的資料(設定簡單的`key`來代替直接找尋複雜的資料)
    
### Hash Table
- 如果每個資料`value`都要用一個`key`來存，那麼資料一多的時候就會有非常龐大的記憶體需求，而Hash Table的出現解決了此問題、是讓我們可以在減少記憶體使用的情況下達成有效率的搜尋或儲存資料的演算法。

- Hash Table的核心精神是<font color=41D3BD>把資料分類儲存</font>：假設現在有n筆資料(n個`key`搭配n個`value`)，Hash Table的想法是可以把這些資料分類依照某種<font color=41D3BD>**分類規則**</font>存在m個箱子中，要找某筆資料的時候只要知道`key`被分在哪個箱子，就可以直接去該箱子取得資料。如下圖：
    ![](https://i.imgur.com/FmykKu1.png)
    -[Hash Table From Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
    圖中我們可以看到3個`key`分別被裝入三個箱子內(但wiki用籃子)。注意到3個`key`分別被裝入箱子前中間的`hash function`，這裡的`hash function`就是前面說的<font color=41D3BD>**分類規則**</font>。
    
### Hash Function
> 什麼是hash function?

- 定義：`hash function`用數學的方式決定把資料分到哪一個箱子裡，來解決前述說的占用記憶體的問題。
- 以上圖為例：我們可先把文字形式的`key`透過編碼轉成數字，然後用此編碼數字$mod$箱子的數量(在此例中箱子數量是15，所以用編碼後的數字除以15取其餘數)，就可以得知該把哪一組`key`對應的資料`value`一起放入餘數號碼的箱子。
- 一個好的`hash function`要滿足2個條件：
    1. 速度夠快。盡可能讓`key`經過`hash function`運算後可以平均地分布在不同的箱子內，是一種確保資料可以被更有效率的使用的方式。
    2. `hash function`算出來的值不能多過箱子的數量，否則有的資料沒有箱子放。

### Collision
> 可能會出現把不同的東西要放在同一個箱子而產生衝突($Collision$)的情況，有兩種基本方式可以解決。

- Chaining：把箱子內的元素串起來，如linked-list概念!把同個箱子內第一個之後的元素以linked-list的方式連接起來就可以避免掉覆蓋的問題，就可以避免查找時發生要找A結果是B的衝突情況發生。
- Open Addressing: 找出下一個空的箱子，來避免同一個箱子內要放兩個資料的情況。

### Hash Table搜尋的時間複雜度
- 最快只要$O(1+\alpha)$ -> $O(1)$：$\alpha$是箱子平均的資料長度，意思是只要經過`hash function`一個步驟後，只要查詢平均箱子的長度就可以找到想要的資料。幸運的話，經過`hash function`一個步驟加上查詢箱子的第一個值就是目標值，時間複雜度是$O(1+1)$ = $O(2)$ -> $O(1)$
- 最慢需要$O(n)$: 很不巧所有的資料都被分到同一個箱子，搜尋效果跟搜尋陣列差不多。

## Hash & MD5 
- Hash, 雜湊: 是一種把資料編碼成一段固定長度數字加符號(通常是英文文字)的技術。基本特性有幾點：
    - 無論輸入資料的原文長短，得出的編碼值(又被稱為雜湊值)都會是一樣的長度
    - 不同的演算法得到的固定長度可能不相同
    - 相同的輸入值會得到相同的雜湊值
    - 不同的輸入值可能得到相同雜湊值
    - 相似的輸入值很大機率得到完全不同的雜湊值
    - 雜湊是單向的編碼運算，無法逆推
    - 破解雜湊值常用方法：暴力法，嘗試各種input另外建構包含輸入/輸出/演算法的output表(一般稱為彩虹表)，表的資料夠多就可以找到原始的輸入值。
    - 防止暴力破解的方法：加鹽。在進行雜湊運算之前把資料任意地方插入字串(此時插入的字串被稱為鹽)，確保彩虹表對應出來的值還是無法還原成原本輸入值。
- MD5, Message digest 5 algorithm: 是一種雜湊演算法，並非加密技術而屬於編碼的一種，常用於驗證資料或訊息的更動。因為雜湊常和加密一起討論所以常有誤用，更多資料參考自[加密和雜湊有什麼不一樣？](https://blog.m157q.tw/posts/2017/12/25/differences-between-encryption-and-hashing/)

### 雜湊、加密、壓縮、編碼
- 雜湊: 單向把資料輸出成另類形式的編碼，無法直接逆推原始資料
- 加密: 有密鑰的皆可視為加密，可透過密鑰直接逆推回原始資料
- 壓縮: 讓輸出資料的資料量比輸入資料小
- 編碼: 只要是把原始資料有邏輯規律地轉換成另種文數字的形式都稱作編碼，雜湊/加密/壓縮都可視為編碼的一種，只是目的和形式依照演算法有所不同。

## 流程圖
![](https://i.imgur.com/QdTNXrZ.jpg)

# 作業格式
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
```

## 測資
```python
MyHashSet().add('測資str')
MyHashSet().remove('測資str')
outcome = MyHashSet().contains('測資str')
print(outcome) #True or False
```

## 測試結果範例
```python
# from Crypto.Hash import MD5
# h = MD5.new()
# h.update('dog'.encode('utf-8')) #把文字以utf-8編碼
# print(h.hexdigest()) #把資料轉成16進制雜湊值
# print(int(h.hexdigest(), 16)) #16進位制轉成10進位制雜湊值

hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
rel  = hashSet.contains('pig')
print(rel) #True
rel  = hashSet.contains('dog')
print(rel) #True
rel = hashSet.contains('cat')
print(rel) #False
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel) #True
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel) #False
```

![](https://i.imgur.com/eyTMHwy.png)

👇**從雜湊開始寫起**  
※因老師上課講解概念使用放入抽屜的想法，因此以下命名不用自己理解的箱子而是抽屜，但概念相同。


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def encode(self, key):
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('-------------------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
        
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print('-------------------------')
        
                  
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        
# MyHashSet().add('測資str')
# MyHashSet().remove('測資str')
# outcome = MyHashSet().contains('測資str')
# print(outcome) #True or False

hashSet = MyHashSet()
hashSet.add('dog')
# hashSet.add('pig')
hashSet.add('ogd') #自己的測資
# rel  = hashSet.contains('pig')
# print(rel) #True
# rel  = hashSet.contains('dog')
# print(rel) #True
# rel = hashSet.contains('cat')
# print(rel) #False
# hashSet.add('bird')
# rel = hashSet.contains('bird')
# print(rel) #True
# hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    -------------------------
    drawer_index: 0
    find_drawer: None
    -------------------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    -------------------------
    drawer_index: 0
    find_drawer: None
    -------------------------
    

👆編碼順利  
👇接續寫`add()`


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def encode(self, key):
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('-------------------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        if head:
            cur = head
            print('cur.next', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('-------------------------')
        return cur
        
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print('-------------------------')
        
        if find_drawer == None:
            new_node = ListNode(int_key_before_hash)
            print('new_node.val:', new_node.val)
            print('new_node.next:', new_node.next)
            self.data[drawer_index] = new_node
            print('new_node.val:', self.data[drawer_index].val)
            print('-------------------------')
        else:
            head = self.data[drawer_index]
            print('head.val:', head.val, 'head.next:', head.next)
            new_node = ListNode(int_key_before_hash)
            self.traversal_to_last(head).next = new_node
            print(self.traversal_to_last(head).next.val)
            print('-------------------------')
        
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        
# MyHashSet().add('測資str')
# MyHashSet().remove('測資str')
# outcome = MyHashSet().contains('測資str')
# print(outcome) #True or False

hashSet = MyHashSet()
hashSet.add('dog')
# hashSet.add('pig')
hashSet.add('ogd') #自己的測資
# rel  = hashSet.contains('pig')
# print(rel) #True
# rel  = hashSet.contains('dog')
# print(rel) #True
# rel = hashSet.contains('cat')
# print(rel) #False
# hashSet.add('bird')
# rel = hashSet.contains('bird')
# print(rel) #True
# hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    -------------------------
    drawer_index: 0
    find_drawer: None
    -------------------------
    new_node.val: 9097202055026264535080901219663267845
    new_node.next: None
    new_node.val: 9097202055026264535080901219663267845
    -------------------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    -------------------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x00000248869BE208>
    -------------------------
    head.val: 9097202055026264535080901219663267845 head.next: None
    cur.next None
    cur.next <__main__.ListNode object at 0x0000024886B746C8>
    cur: <__main__.ListNode object at 0x0000024886B746C8>
    -------------------------
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-48-7d654d9da48a> in <module>
         93 hashSet.add('dog')
         94 # hashSet.add('pig')
    ---> 95 hashSet.add('ogd') #自己的測資
         96 # rel  = hashSet.contains('pig')
         97 # print(rel) #True
    

    <ipython-input-48-7d654d9da48a> in add(self, key)
         68             new_node = ListNode(int_key_before_hash)
         69             self.traversal_to_last(head).next = new_node
    ---> 70             print(self.traversal_to_last(head).next.val)
         71             print('-------------------------')
         72 
    

    AttributeError: 'NoneType' object has no attribute 'val'


👆卡關，先寫`contains()`


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print('============traversal============')
        if head:
            cur = head
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('============traversal_end============')
        return cur
        
    def add(self, key):
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print('------------------------')
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
        else:
            head = self.data[drawer_index]
            print('head.val:', head.val, 'head.next:', head.next)
            new_node = ListNode(int_key_before_hash)
            self.traversal_to_last(head).next = new_node
            print(self.traversal_to_last(head).next)
            print('============add_end============')
            
        
#     def remove(self, key):
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur)
        return False
            
    def contains(self, key):
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        return true_or_false
        
        
# MyHashSet().add('測資str')
# MyHashSet().remove('測資str')
# outcome = MyHashSet().contains('測資str')
# print(outcome) #True or False

hashSet = MyHashSet()
hashSet.add('dog')
# hashSet.add('pig')
# hashSet.add('ogd') #自己的測資
# rel  = hashSet.contains('pig')
# print(rel) #True
# rel  = hashSet.contains('dog')
# print(rel) #True
rel = hashSet.contains('cat')
print(rel) #False
# hashSet.add('bird')
# rel = hashSet.contains('bird')
# print(rel) #True
# hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    ------------------------
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    ============contains============
    ------------encode------------
    hexi_key_before_hash: d077f244def8a70e5ea758bd8352fcd8
    int_key_before_hash: 277102220249073555409885156483852860632
    ------------encode_end------------
    drawer_index: 2
    ============contains_end============
    False
    


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print()
        print('------------traversal------------')
        if head:
            cur = head
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('------------traversal_end------------')
                print()
        return cur
        
    def add(self, key):
        print()
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print()
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
            print()
        else:
#             head = self.data[drawer_index] #錯誤點
#             print('head.val:', head.val, 'head.next:', head.next)
            new_node = ListNode(int_key_before_hash)
            print(new_node)
            self.traversal_to_last(self.data[drawer_index]).next = new_node
            node = self.traversal_to_last(self.data[drawer_index]).next
            print(node.val)
            print('============add_end============')
            print()
            
        
#     def remove(self, key):
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur)
        return False
            
    def contains(self, key):
        print
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        print
        return true_or_false
        
        
# MyHashSet().add('測資str')
# MyHashSet().remove('測資str')
# outcome = MyHashSet().contains('測資str')
# print(outcome) #True or False

hashSet = MyHashSet()
hashSet.add('dog')
# hashSet.add('pig')
hashSet.add('ogd') #自己的測資
# rel  = hashSet.contains('pig')
# print(rel) #True
# rel  = hashSet.contains('dog')
# print(rel) #True
# rel = hashSet.contains('cat')
# print(rel) #False
# hashSet.add('bird')
# rel = hashSet.contains('bird')
# print(rel) #True
# hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024887C19988>
    
    <__main__.ListNode object at 0x0000024887C19D48>
    
    ------------traversal------------
    cur.next: None
    
    ------------traversal------------
    cur.next: <__main__.ListNode object at 0x0000024887C19D48>
    cur: <__main__.ListNode object at 0x0000024887C19D48>
    ------------traversal_end------------
    
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-100-42bc8ddbf4d9> in <module>
        106 hashSet.add('dog')
        107 # hashSet.add('pig')
    --> 108 hashSet.add('ogd') #自己的測資
        109 # rel  = hashSet.contains('pig')
        110 # print(rel) #True
    

    <ipython-input-100-42bc8ddbf4d9> in add(self, key)
         65             self.traversal_to_last(self.data[drawer_index]).next = new_node
         66             node = self.traversal_to_last(self.data[drawer_index]).next
    ---> 67             print(node.val)
         68             print('============add_end============')
         69             print()
    

    AttributeError: 'NoneType' object has no attribute 'val'


👆👆👆
```python
            head = self.data[drawer_index] #錯誤點
            print('head.val:', head.val, 'head.next:', head.next) #錯誤點
```
發現這一段沒有改到linked-list內的資料，而是改到head


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print()
        print('------------traversal------------')
        if head:
            cur = head
            print('cur.val:', cur.val)
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('------------traversal_end------------')
                print()
        return cur
        
    def add(self, key):
        print()
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print()
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
            print()
        else:
            new_node = ListNode(int_key_before_hash)
            print(new_node)
            self.traversal_to_last(self.data[drawer_index]).next = new_node
            print('============add_end============')
            print()
              
#     def remove(self, key):
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur)
        return False
            
    def contains(self, key):
        print
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        print
        return true_or_false
        
        
# MyHashSet().add('測資str')
# MyHashSet().remove('測資str')
# outcome = MyHashSet().contains('測資str')
# print(outcome) #True or False

hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('ogd') #自己的測資
hashSet.add('salt') #自己的測資
rel  = hashSet.contains('pig')
print(rel) #True
rel  = hashSet.contains('dog')
print(rel) #True
rel = hashSet.contains('cat')
print(rel) #False
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel) #True
# hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    find_drawer: None
    
    head_node.val: 328716098820163891201703637637140404312
    head_node.next: None
    head_node.val: 328716098820163891201703637637140404312
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024886B7C308>
    
    <__main__.ListNode object at 0x0000024887C32188>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: None
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: ceb20772e0c9d240c75eb26b0e37abee
    int_key_before_hash: 274745347050958250505533111294722812910
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024886B7C308>
    
    <__main__.ListNode object at 0x0000024887C32788>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x0000024887C32188>
    cur: <__main__.ListNode object at 0x0000024887C32188>
    ------------traversal_end------------
    
    ============add_end============
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    true!
    ============contains_end============
    True
    ============contains============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    true!
    ============contains_end============
    True
    ============contains============
    ------------encode------------
    hexi_key_before_hash: d077f244def8a70e5ea758bd8352fcd8
    int_key_before_hash: 277102220249073555409885156483852860632
    ------------encode_end------------
    drawer_index: 2
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-114-71d074bd91c5> in <module>
        108 rel  = hashSet.contains('dog')
        109 print(rel) #True
    --> 110 rel = hashSet.contains('cat')
        111 print(rel) #False
        112 hashSet.add('bird')
    

    <ipython-input-114-71d074bd91c5> in contains(self, key)
         88 
         89         head = self.data[drawer_index]
    ---> 90         true_or_false = self.find_val(head, int_key_before_hash)
         91         print('============contains_end============')
         92         print
    

    <ipython-input-114-71d074bd91c5> in find_val(self, head, int_key_before_hash)
         77         else:
         78             cur = head.next
    ---> 79             self.find_val(cur)
         80         return False
         81 
    

    TypeError: find_val() missing 1 required positional argument: 'int_key_before_hash'


👆發現`find_val()`少加`int_key_before_hash`


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print()
        print('------------traversal------------')
        if head:
            cur = head
            print('cur.val:', cur.val)
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('------------traversal_end------------')
                print()
        return cur
        
    def add(self, key):
        print()
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print()
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
            print()
        else:
            new_node = ListNode(int_key_before_hash)
            print(new_node)
            self.traversal_to_last(self.data[drawer_index]).next = new_node
            print('============add_end============')
            print()
              
#     def remove(self, key):
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        print
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        print
        return true_or_false
        
# MyHashSet().add('測資str')
# MyHashSet().remove('測資str')
# outcome = MyHashSet().contains('測資str')
# print(outcome) #True or False

hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('ogd') #自己的測資
hashSet.add('salt') #自己的測資
rel  = hashSet.contains('pig')
print(rel) #True
rel  = hashSet.contains('dog')
print(rel) #True
rel = hashSet.contains('cat')
print(rel) #False
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel) #True
# hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    find_drawer: None
    
    head_node.val: 328716098820163891201703637637140404312
    head_node.next: None
    head_node.val: 328716098820163891201703637637140404312
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024886ADCC48>
    
    <__main__.ListNode object at 0x0000024887C30D08>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: None
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: ceb20772e0c9d240c75eb26b0e37abee
    int_key_before_hash: 274745347050958250505533111294722812910
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024886ADCC48>
    
    <__main__.ListNode object at 0x0000024887C30DC8>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x0000024887C30D08>
    cur: <__main__.ListNode object at 0x0000024887C30D08>
    ------------traversal_end------------
    
    ============add_end============
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    true!
    ============contains_end============
    True
    ============contains============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    true!
    ============contains_end============
    True
    ============contains============
    ------------encode------------
    hexi_key_before_hash: d077f244def8a70e5ea758bd8352fcd8
    int_key_before_hash: 277102220249073555409885156483852860632
    ------------encode_end------------
    drawer_index: 2
    ============contains_end============
    False
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    find_drawer: None
    
    head_node.val: 228205656534084130715094099373997216749
    head_node.next: None
    head_node.val: 228205656534084130715094099373997216749
    ============add_end============
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    true!
    ============contains_end============
    True
    

👆看起來可以跑，續寫`remove()`


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print()
        print('------------traversal------------')
        if head:
            cur = head
            print('cur.val:', cur.val)
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('------------traversal_end------------')
                print()
        return cur
        
    def add(self, key):
        print()
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print()
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
            print()
        else:
            new_node = ListNode(int_key_before_hash)
            print(new_node)
            self.traversal_to_last(self.data[drawer_index]).next = new_node
            print('============add_end============')
            print()
              
#     def remove(self, key):
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        print
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        print
        return true_or_false

hashSet = MyHashSet()
print('dog')
hashSet.add('dog')
print('pig')
hashSet.add('pig')
print('ogd')
hashSet.add('ogd') #自己的測資
print('salt')
hashSet.add('salt') #自己的測資
print('bird')
hashSet.add('bird')
print()
print('pig?')
rel  = hashSet.contains('pig')
print(rel) #True
print()
print('dog?')
rel  = hashSet.contains('dog')
print(rel) #True
print()
print('cat?')
rel = hashSet.contains('cat')
print(rel) #False
print()
print('bird?')
rel = hashSet.contains('bird')
print(rel) #True
# hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    dog
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    
    pig
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    find_drawer: None
    
    head_node.val: 328716098820163891201703637637140404312
    head_node.next: None
    head_node.val: 328716098820163891201703637637140404312
    ============add_end============
    
    ogd
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024887C4F4C8>
    
    <__main__.ListNode object at 0x0000024887C48BC8>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: None
    ============add_end============
    
    salt
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: ceb20772e0c9d240c75eb26b0e37abee
    int_key_before_hash: 274745347050958250505533111294722812910
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024887C4F4C8>
    
    <__main__.ListNode object at 0x0000024887C48C48>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x0000024887C48BC8>
    cur: <__main__.ListNode object at 0x0000024887C48BC8>
    ------------traversal_end------------
    
    ============add_end============
    
    bird
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    find_drawer: None
    
    head_node.val: 228205656534084130715094099373997216749
    head_node.next: None
    head_node.val: 228205656534084130715094099373997216749
    ============add_end============
    
    
    pig?
    ============contains============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    true!
    ============contains_end============
    True
    
    dog?
    ============contains============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    true!
    ============contains_end============
    True
    
    cat?
    ============contains============
    ------------encode------------
    hexi_key_before_hash: d077f244def8a70e5ea758bd8352fcd8
    int_key_before_hash: 277102220249073555409885156483852860632
    ------------encode_end------------
    drawer_index: 2
    ============contains_end============
    False
    
    bird?
    ============contains============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    true!
    ============contains_end============
    True
    


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print()
        print('------------traversal------------')
        if head:
            cur = head
            print('cur.val:', cur.val)
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('------------traversal_end------------')
                print()
        return cur
        
    def add(self, key):
        print()
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print()
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
            print()
        else:
            new_node = ListNode(int_key_before_hash)
            print(new_node)
            self.traversal_to_last(self.data[drawer_index]).next = new_node
            print('============add_end============')
            print()
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        print()
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        print()
        return true_or_false
    
    def remove(self, key):
        print()
        print('============remove============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        if head:
            if head.val == int_key_before_hash:
                self.data[drawer_index] = head.next
                self.remove(key)
            else:
                prev = head
                cur = head.next
                if cur.val == int_key_before_hash:
                    self.data[drawer_index].next = self.data[drawer_index].next.next
                    self.remove(key)
                else:
                    cur = head.next.next

hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('ogd') #自己的測資
hashSet.add('salt') #自己的測資
hashSet.add('bird')
# rel  = hashSet.contains('pig')
# print(rel) #True
# rel  = hashSet.contains('dog')
# print(rel) #True
# rel = hashSet.contains('cat')
# print(rel) #False
# rel = hashSet.contains('bird')
# print(rel) #True
hashSet.remove('pig')
# rel = hashSet.contains('pig')
# print(rel) #False
```

    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    find_drawer: None
    
    head_node.val: 328716098820163891201703637637140404312
    head_node.next: None
    head_node.val: 328716098820163891201703637637140404312
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024887C94E08>
    
    <__main__.ListNode object at 0x0000024887C94848>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: None
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: ceb20772e0c9d240c75eb26b0e37abee
    int_key_before_hash: 274745347050958250505533111294722812910
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x0000024887C94E08>
    
    <__main__.ListNode object at 0x0000024887C94E88>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x0000024887C94848>
    cur: <__main__.ListNode object at 0x0000024887C94848>
    ------------traversal_end------------
    
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    find_drawer: None
    
    head_node.val: 228205656534084130715094099373997216749
    head_node.next: None
    head_node.val: 228205656534084130715094099373997216749
    ============add_end============
    
    
    ============remove============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    
    ============remove============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    

在紙上來回演練把刪除了邏輯搞清楚後重寫`remove()`


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print()
        print('------------traversal------------')
        if head:
            cur = head
            print('cur.val:', cur.val)
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('------------traversal_end------------')
                print()
        return cur
        
    def add(self, key):
        print()
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print()
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
            print()
        else:
            new_node = ListNode(int_key_before_hash)
            print(new_node)
            self.traversal_to_last(self.data[drawer_index]).next = new_node
            print('============add_end============')
            print()
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        print()
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        print()
        return true_or_false
    
    def find_target(self, head, int_key_before_hash):
        if head:
            prev = head
            cur = head.next
            if cur:
                while cur.val != int_key_before_hash and cur.next!= None:
                    cur = cur.next
                    prev = prev.next
                if cur.val == int_key_before_hash:
                    return prev
        return False
    
    def edit_list(self, head, int_key_before_hash):
        if self.find_target(head, int_key_before_hash) == False:
            pass
        else:
            self.find_target(head, int_key_before_hash).next = self.find_target(head, int_key_before_hash).next.next
            self.edit_list(head, int_key_before_hash)
    
    def remove(self, key):
        print()
        print('============remove============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        self.edit_list(head, int_key_before_hash)
        if head.val == int_key_before_hash:
            self.data[drawer_index] = head.next
        print('============remove_end============')

hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('ogd') #自己的測資
hashSet.add('salt') #自己的測資
hashSet.add('bird')
rel  = hashSet.contains('pig')
print(rel) #True
rel  = hashSet.contains('dog')
print(rel) #True
rel = hashSet.contains('cat')
print(rel) #False
rel = hashSet.contains('bird')
print(rel) #True
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel) #False
```

    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    find_drawer: None
    
    head_node.val: 328716098820163891201703637637140404312
    head_node.next: None
    head_node.val: 328716098820163891201703637637140404312
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x000001C9951D7FC8>
    
    <__main__.ListNode object at 0x000001C9951D6148>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: None
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: ceb20772e0c9d240c75eb26b0e37abee
    int_key_before_hash: 274745347050958250505533111294722812910
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x000001C9951D7FC8>
    
    <__main__.ListNode object at 0x000001C9951D6108>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x000001C9951D6148>
    cur: <__main__.ListNode object at 0x000001C9951D6148>
    ------------traversal_end------------
    
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    find_drawer: None
    
    head_node.val: 228205656534084130715094099373997216749
    head_node.next: None
    head_node.val: 228205656534084130715094099373997216749
    ============add_end============
    
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    true!
    ============contains_end============
    
    True
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    true!
    ============contains_end============
    
    True
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: d077f244def8a70e5ea758bd8352fcd8
    int_key_before_hash: 277102220249073555409885156483852860632
    ------------encode_end------------
    drawer_index: 2
    ============contains_end============
    
    False
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    true!
    ============contains_end============
    
    True
    
    ============remove============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    ============remove_end============
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    ============contains_end============
    
    False
    

🌞成功，多加幾個測資試試


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        print('------------encode------------')
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        print('hexi_key_before_hash:', hexi_key_before_hash)
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        print('int_key_before_hash:', int_key_before_hash)
        print('------------encode_end------------')
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        print()
        print('------------traversal------------')
        if head:
            cur = head
            print('cur.val:', cur.val)
            print('cur.next:', cur.next)
            if cur.next != None:
                cur = cur.next
                print('cur:', cur)
                print('------------traversal_end------------')
                print()
        return cur
        
    def add(self, key):
        print()
        print('============add============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        find_drawer = self.data[drawer_index]
        print('find_drawer:',find_drawer)
        print()
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            print('head_node.val:', head_node.val)
            print('head_node.next:', head_node.next)
            self.data[drawer_index] = head_node
            print('head_node.val:', self.data[drawer_index].val)
            print('============add_end============')
            print()
        else:
            new_node = ListNode(int_key_before_hash)
            print(new_node)
            self.traversal_to_last(self.data[drawer_index]).next = new_node
            print('============add_end============')
            print()
    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            print('true!')
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        print()
        print('============contains============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        print('============contains_end============')
        print()
        return true_or_false
    
    def find_target(self, head, int_key_before_hash):
        if head:
            prev = head
            cur = head.next
            if cur:
                while cur.val != int_key_before_hash and cur.next!= None:
                    cur = cur.next
                    prev = prev.next
                if cur.val == int_key_before_hash:
                    return prev
        return False
    
    def edit_list(self, head, int_key_before_hash):
        if self.find_target(head, int_key_before_hash) == False:
            pass
        else:
            self.find_target(head, int_key_before_hash).next = self.find_target(head, int_key_before_hash).next.next
            self.edit_list(head, int_key_before_hash)
    
    def remove(self, key):
        print()
        print('============remove============')
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        print('drawer_index:', drawer_index)
        
        head = self.data[drawer_index]
        self.edit_list(head, int_key_before_hash)
        if head.val == int_key_before_hash:
            self.data[drawer_index] = head.next
        print('============remove_end============')

hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('ogd') #自己的測資
hashSet.add('salt') #自己的測資
hashSet.add('bird')
rel  = hashSet.contains('pig')
print(rel) #True
rel  = hashSet.contains('dog')
print(rel) #True
rel = hashSet.contains('cat')
print(rel) #False
rel = hashSet.contains('bird')
print(rel) #True
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel) #False
hashSet.add('dog')
hashSet.add('salt')
hashSet.remove('dog')
rel  = hashSet.contains('dog')
print(rel) #False
```

    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: None
    
    head_node.val: 9097202055026264535080901219663267845
    head_node.next: None
    head_node.val: 9097202055026264535080901219663267845
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    find_drawer: None
    
    head_node.val: 328716098820163891201703637637140404312
    head_node.next: None
    head_node.val: 328716098820163891201703637637140404312
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 043f334c7f494be53a0fd5e6e0af9bca
    int_key_before_hash: 5645067148850701189611025456136428490
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x000001C9951D62C8>
    
    <__main__.ListNode object at 0x000001C9951D5C48>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: None
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: ceb20772e0c9d240c75eb26b0e37abee
    int_key_before_hash: 274745347050958250505533111294722812910
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x000001C9951D62C8>
    
    <__main__.ListNode object at 0x000001C9951D5BC8>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x000001C9951D5C48>
    cur: <__main__.ListNode object at 0x000001C9951D5C48>
    ------------traversal_end------------
    
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    find_drawer: None
    
    head_node.val: 228205656534084130715094099373997216749
    head_node.next: None
    head_node.val: 228205656534084130715094099373997216749
    ============add_end============
    
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    true!
    ============contains_end============
    
    True
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    true!
    ============contains_end============
    
    True
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: d077f244def8a70e5ea758bd8352fcd8
    int_key_before_hash: 277102220249073555409885156483852860632
    ------------encode_end------------
    drawer_index: 2
    ============contains_end============
    
    False
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: abaecf8ca3f98dc13eeecbac263cd3ed
    int_key_before_hash: 228205656534084130715094099373997216749
    ------------encode_end------------
    drawer_index: 4
    true!
    ============contains_end============
    
    True
    
    ============remove============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    ============remove_end============
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: f74c6af46a78becb2f1bd3f95bbd5858
    int_key_before_hash: 328716098820163891201703637637140404312
    ------------encode_end------------
    drawer_index: 2
    ============contains_end============
    
    False
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x000001C9951D62C8>
    
    <__main__.ListNode object at 0x000001C9951D5C88>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x000001C9951D5C48>
    cur: <__main__.ListNode object at 0x000001C9951D5C48>
    ------------traversal_end------------
    
    ============add_end============
    
    
    ============add============
    ------------encode------------
    hexi_key_before_hash: ceb20772e0c9d240c75eb26b0e37abee
    int_key_before_hash: 274745347050958250505533111294722812910
    ------------encode_end------------
    drawer_index: 0
    find_drawer: <__main__.ListNode object at 0x000001C9951D62C8>
    
    <__main__.ListNode object at 0x000001C9951D5548>
    
    ------------traversal------------
    cur.val: 9097202055026264535080901219663267845
    cur.next: <__main__.ListNode object at 0x000001C9951D5C48>
    cur: <__main__.ListNode object at 0x000001C9951D5C48>
    ------------traversal_end------------
    
    ============add_end============
    
    
    ============remove============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    ============remove_end============
    
    ============contains============
    ------------encode------------
    hexi_key_before_hash: 06d80eb0c50b49a509b49f2424e8c805
    int_key_before_hash: 9097202055026264535080901219663267845
    ------------encode_end------------
    drawer_index: 0
    ============contains_end============
    
    False
    

👇把程式修改乾淨


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        if head:
            cur = head
            if cur.next != None:
                cur = cur.next
        return cur
        
    def add(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        find_drawer = self.data[drawer_index]
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            self.data[drawer_index] = head_node
        else:
            new_node = ListNode(int_key_before_hash)
            self.traversal_to_last(self.data[drawer_index]).next = new_node

    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        return true_or_false
    
    def find_target(self, head, int_key_before_hash):
        if head:
            prev = head
            cur = head.next
            if cur:
                while cur.val != int_key_before_hash and cur.next!= None:
                    cur = cur.next
                    prev = prev.next
                if cur.val == int_key_before_hash:
                    return prev
        return False
    
    def edit_list(self, head, int_key_before_hash):
        if self.find_target(head, int_key_before_hash) == False:
            pass
        else:
            self.find_target(head, int_key_before_hash).next = self.find_target(head, int_key_before_hash).next.next
            self.edit_list(head, int_key_before_hash)
    
    def remove(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        head = self.data[drawer_index]
        self.edit_list(head, int_key_before_hash)
        if head.val == int_key_before_hash:
            self.data[drawer_index] = head.next

hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('ogd') #自己的測資
hashSet.add('salt') #自己的測資
hashSet.add('bird')
rel  = hashSet.contains('pig')
print(rel) #True
rel  = hashSet.contains('dog')
print(rel) #True
rel = hashSet.contains('cat')
print(rel) #False
rel = hashSet.contains('bird')
print(rel) #True
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel) #False
hashSet.add('dog')
hashSet.add('salt')
hashSet.add('ogd') 
hashSet.remove('dog')
rel = hashSet.contains('dog')
print(rel) #False
```

    True
    True
    False
    True
    False
    False
    

## 作業繳交版本


```python
# author :汶穗

from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        if head:
            cur = head
            if cur.next != None:
                cur = cur.next
        return cur
        
    def add(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        find_drawer = self.data[drawer_index]
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            self.data[drawer_index] = head_node
        else:
            new_node = ListNode(int_key_before_hash)
            self.traversal_to_last(self.data[drawer_index]).next = new_node

    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        return true_or_false
    
    def find_target(self, head, int_key_before_hash):
        if head:
            prev = head
            cur = head.next
            if cur:
                while cur.val != int_key_before_hash and cur.next!= None:
                    cur = cur.next
                    prev = prev.next
                if cur.val == int_key_before_hash:
                    return prev
        return False
    
    def edit_list(self, head, int_key_before_hash):
        if self.find_target(head, int_key_before_hash) == False:
            pass
        else:
            self.find_target(head, int_key_before_hash).next = self.find_target(head, int_key_before_hash).next.next
            self.edit_list(head, int_key_before_hash)
    
    def remove(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        head = self.data[drawer_index]
        self.edit_list(head, int_key_before_hash)
        if head.val == int_key_before_hash:
            self.data[drawer_index] = head.next

## Reference
# - [Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/9512548#overview)
# - [目錄：演算法與資料結構](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)
# - [Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)
# - [Hash Table：Chaining](http://alrightchiu.github.io/SecondRound/hash-tablechaining.html)
# - [白話的 Hash Table 簡介](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)
# - [Hash Table From Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
# - [加密和雜湊有什麼不一樣？](https://blog.m157q.tw/posts/2017/12/25/differences-between-encryption-and-hashing/)
# - [如何區分加密、壓縮、編碼](https://blog.m157q.tw/posts/2017/12/23/differences-between-encryption-compression-and-encoding/)
# - [從刪除 linked-list node 看程式設計的品味](https://medium.com/fcamels-notes/%E5%BE%9E%E5%88%AA%E9%99%A4-linked-list-node-%E7%9C%8B%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E7%9A%84%E5%93%81%E5%91%B3-b597cc5af785)
```

## 功能說明
> 以免日後忘記自己的想法所做的紀錄

※main function分別有`add()`, `contains()`, `remove()`
※撰寫邏輯：side funciton都會位在main function前面。  
※main function底下的side funciton:
1. `add()`: `encode()`, `hash_function()`, `traversal_to_last()`  
2. `contains()`:`encode()`, `hash_function()`,`find_val()`
3. `remove()`:`encode()`, `hash_function()`, `find_target()`, `edit_list()`

```python
from Crypto.Hash import MD5 #import MD5套件以進行編碼

# hash table 不同抽屜會用到linked list的概念，因此建置一個class創造節點物件讓他們可以相連
class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity # hashset的抽屜數量，把不同的資料分進不同的抽屜加快搜尋修改速度
        self.data = [None] * capacity #初始化抽屜的內容物為None
    
    # 把文字進行編碼
    def encode(self, key):
        key_before_hash = MD5.new() #創建一個MD5新物件
        key_before_hash.update(key.encode('utf-8')) #使用utf-8編碼
        hexi_key_before_hash = key_before_hash.hexdigest() #轉成16進位的雜湊值
        int_key_before_hash = int(key_before_hash.hexdigest(), 16) #轉成10進位的雜湊值
        return int_key_before_hash #回傳編碼後的物件
    
    # 計算不同key編碼後應該放入的箱子編號
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    # 走訪到該抽屜的最後一個元素以進行新增
    def traversal_to_last(self, head):
        if head:
            cur = head
            if cur.next != None:
                cur = cur.next
        return cur
    
    ## Main funcion: add()
    def add(self, key):
        int_key_before_hash = self.encode(key) #先把新增的key文字轉成編碼
        drawer_index = self.hash_function(int_key_before_hash) #找到該key的箱子編號
        
        find_drawer = self.data[drawer_index] #找到該箱子的頭
        
        if find_drawer == None: #當頭沒有東西，直接新增該節點於頭
            head_node = ListNode(int_key_before_hash)
            self.data[drawer_index] = head_node
        else:
            new_node = ListNode(int_key_before_hash)　#當頭有東西，新增該節點後
            self.traversal_to_last(self.data[drawer_index]).next = new_node #走訪到該list最後一個元素，把最後一個元素的next設為新的元素

    # 尋找是否含有某個值，因為用recursive寫法所以分成兩個function
    def find_val(self, head, int_key_before_hash):
        if head == None: #如果該箱子沒有東西，直接return False，沒有東西一定沒有我們要找的值
            return False
        
        if head.val == int_key_before_hash:　#如果head直接是我們要找的東西，return True
            return True
        else:
            cur = head.next #如果head不是我們要找的東西，從下一個開始找起
            self.find_val(cur, int_key_before_hash)
        return False
    
    ## Main funcion: contains()
    def contains(self, key):
        int_key_before_hash = self.encode(key) #先把新增的key文字轉成編碼
        drawer_index = self.hash_function(int_key_before_hash) #找到該key的箱子編號
        
        head = self.data[drawer_index] #找到該箱子的頭
        true_or_false = self.find_val(head, int_key_before_hash) #尋找是否含有目標值
        return true_or_false #回傳結果
    
    def find_target(self, head, int_key_before_hash):#尋找目標值
        if head: #如果head存在
            prev = head #把head設為previous元素
            cur = head.next #把current設為previous的下一個
            if cur: #如果下一個存在
                while cur.val != int_key_before_hash and cur.next!= None: #當下一個的值不是目標值，而且下一個的下一個不是None
                    cur = cur.next #把current移動到下一個繼續找
                    prev = prev.next #把previous移動到下一個繼續找
                if cur.val == int_key_before_hash: #如果current值是目標元素，回傳該目標的前一個值，在main function就可以直接把該目標的前一個值的next設為下下個元素，就跳過了目標值重接了linked-list
                    return prev 
        return False # 如果都找不到就回傳False
    
    def edit_list(self, head, int_key_before_hash):
        if self.find_target(head, int_key_before_hash) == False: #如果要移除的元素都找不到就甚麼都不做
            pass
        else:#找到移除的元素後
            self.find_target(head, int_key_before_hash).next = self.find_target(head, int_key_before_hash).next.next #把該目標的前一個值的next設為下下個元素，跳過了目標值重接了linked-list
            self.edit_list(head, int_key_before_hash) #繼續從頭開始搜尋是否有需要remove的元素
    
    ## Main funcion: remove()
    def remove(self, key):
        int_key_before_hash = self.encode(key) #先把新增的key文字轉成編碼
        drawer_index = self.hash_function(int_key_before_hash) #找到該key的箱子編號
        
        head = self.data[drawer_index] #找到該箱子的頭
        self.edit_list(head, int_key_before_hash) #尋找是否有要移除的元素
        if head.val == int_key_before_hash: #最後檢查頭是不是target，因為上面的寫法沒有check頭
            self.data[drawer_index] = head.next
```

## Reference
- [Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/9512548#overview)
- [目錄：演算法與資料結構](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)
- [Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)
- [Hash Table：Chaining](http://alrightchiu.github.io/SecondRound/hash-tablechaining.html)
- [白話的 Hash Table 簡介](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)
- [Hash Table From Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [加密和雜湊有什麼不一樣？](https://blog.m157q.tw/posts/2017/12/25/differences-between-encryption-and-hashing/)
- [如何區分加密、壓縮、編碼](https://blog.m157q.tw/posts/2017/12/23/differences-between-encryption-compression-and-encoding/)
- [從刪除 linked-list node 看程式設計的品味](https://medium.com/fcamels-notes/%E5%BE%9E%E5%88%AA%E9%99%A4-linked-list-node-%E7%9C%8B%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E7%9A%84%E5%93%81%E5%91%B3-b597cc5af785)


```python

```
