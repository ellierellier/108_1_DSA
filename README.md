# 108_1_Data Structure and Algorithm
I'm 汶穗。Here is my weekly learning notes. :)
  * My [Learning check😀](https://hackmd.io/PFMjkciiRYuTuaYk77Be8Q?both)(Other related topics also put there.)
  * My [CS50 notes🖋](https://github.com/okpersist/CS50/tree/master/2013fall)

# HW
🖋

HW | WK | TOPIC | 🔗
-- | -- | :--- | --
1 | 4 | Quicksort | [Notes](#what-is-quicksort)/[HW code](#%e4%bd%9c%e6%a5%adcode)/[流程圖](#%e4%bd%9c%e6%a5%ad%e6%b5%81%e7%a8%8b%e5%9c%96)
2 | 6 | Heapsort | [Notes](#heap-sort)/[HW code](https://nbviewer.jupyter.org/github/okpersist/108_1_DSA/blob/master/HW2/Heapsort_04113020_learning.ipynb)/[流程圖](https://github.com/okpersist/108_1_DSA/blob/master/week6/heapsort_flow_chart.md)
2 | 6 | Mergesort | [Notes](#merge-sort)/[HW code](https://nbviewer.jupyter.org/github/okpersist/108_1_DSA/blob/master/HW2/Mergesort_04113020_learning.ipynb)/[流程圖](https://github.com/okpersist/108_1_DSA/blob/master/week6/mergesort_flow_chart.md)
3 | 9 | Binary Search Tree |  [Notes](#binary-search-tree)/[HW code](https://github.com/okpersist/108_1_DSA/blob/master/HW3/binary_search_tree_04113020.py)/[學習歷程](https://nbviewer.jupyter.org/github/okpersist/108_1_DSA/blob/master/HW3/binary_search_tree_learning_04113020.ipynb)/[圖](https://github.com/okpersist/108_1_DSA/blob/master/week9/BST_flowchart.jpg)
4 | 11 | Hash Table | [Notes](#hash-table)/[HW code](https://github.com/okpersist/108_1_DSA/blob/master/HW4/hash_table_04113020.py)/[學習歷程](https://github.com/okpersist/108_1_DSA/blob/master/HW4/hash_table_04113020_learning.md)/[圖](https://github.com/okpersist/108_1_DSA/blob/master/week11/hash_table_flowchart.jpg)
5 | 13 | Breadth Frist Search & Depth Frist Search | [Notes](#week-13)/[HW code](https://github.com/okpersist/108_1_DSA/blob/master/HW5/BFS_04113020.py)/[學習歷程](https://github.com/okpersist/108_1_DSA/blob/master/HW5/BFS_DFS_04113020_learning.md)/[圖](https://github.com/okpersist/108_1_DSA/blob/master/week13/BFS%20%26%20DFS_flowchart.jpg)
6 | 15 | Minimum Spanning Tree & Shortest Path | [Notes](#week-1)/[HW code](https://github.com/okpersist/108_1_DSA/blob/master/HW6/Dijkstra_04113020.py)/[學習歷程](https://github.com/okpersist/108_1_DSA/blob/master/HW6/Dijkstra_04113020_learning.md)/[圖](https://github.com/okpersist/108_1_DSA/tree/master/week15)

# Content
> 這裡紀錄每周上課的內容

- [week 2](#week-2)
  - [reference](#reference)
- [week 3](#week-3)
  - [Key takeaway](#key-takeaway)
  - [reference](#reference-1)
- [week 4](#week-4)
  - [setmatch](#setmatch)
  - [Insertion Sort](#insertion-sort)
  - [QuickSort + HW1📝](#quicksort)
  - [Object Oriented Programming](#object-oriented-programming)
- [Week6](#week6)
  - [Heap Sort + HW2📝](#heap-sort)
  - [Merge Sort + HW2📝](#merge-sort)
  - [Heap sort v.s Merge sort](#heap-sort-vs-merge-sort)
  - [如何讀懂別人的code?](#%e5%a6%82%e4%bd%95%e8%ae%80%e6%87%82%e5%88%a5%e4%ba%ba%e7%9a%84code)
- [Week8](#week8)
  - [recursive concept](#recursion)
  - [Linked Structure for Binary Tree](#linked-structure-for-binary-tree)
- [Week9](#week9)
  - [What is BST?](#what-is-bst?)
  - [Depth First Traversal](#Depth-First-Traversal)
- [Week11](#week11)
  - [What is a Hash table?](#what-is-a-hash-table)
  - [Hash Function](#hash-function)
  - [Collision](#collision)
  - [Hash & MD5](#hash--md5)
- [Week13](#week-13)
  - [Graph](#graph)
  - [What is BFS?](#bfs-%e5%8e%9f%e7%90%86)
  - [What is DFS?](#dfs-%e5%8e%9f%e7%90%86)
  - [BFS v.s DFS](#bfs-vs-dfs)
- [Week15](#week-15)
  - [Dijkstra algorithm](#dijkstra-%e5%8e%9f%e7%90%86%e8%aa%aa%e6%98%8e)
  - [Shortest Path concept](#%e6%9c%80%e7%9f%ad%e8%b7%af%e5%be%91%e5%95%8f%e9%a1%8c%e5%ae%9a%e7%be%a9%e8%88%87%e5%88%86%e9%a1%9e)
  - [Kruskal algorithm](#kruskal-%e5%8e%9f%e7%90%86%e8%aa%aa%e6%98%8e)
  - [Minimum Spanning Tree concept](#%e6%9c%80%e5%b0%8f%e7%94%9f%e6%88%90%e6%a8%b9%e5%8e%9f%e7%90%86)

---
---
# week 2
 > Topic: Design a linked list

1. What's class?
    * Class，中文常稱類別，可視為創造物件的藍圖或模板。
    * Class描述了目標物件的屬性和方法。舉例來說，我們可以創建一個叫做**狗**的類別，在這個類別中設定屬性比如說品種、名字、年齡。如此一來，每個透過**狗**類別設定的個體，都會具有這兩個屬性。
    * 當我們想創造一隻2歲、名為可可的柴犬，可以在類別設定品種名、名字、年齡三個屬性，使系統自動幫我們創造一隻品種為柴犬、名為可可、年齡兩歲的狗狗。
    * 我們也可以在class設定方法，指定狗狗可以做出的動作，比如裝死、坐下，這樣用前述步驟創造完一個狗狗實體後，我們可以用`名稱.坐下`的方式讓狗狗在系統裡執行坐下。這樣每次在創造一隻新狗狗，或請狗狗執行動作的時候，就不用大費周章重新寫程式，傳入參數或在名稱後加上屬性的方式即可簡單的讓程式運作。

2. What's a linked-list?
   * linked-list由節點`node`與指南`pointer`組成，節點是資料實際存放的點，可散落在記憶體的不同位置，透過指南可以從第一個節點走訪到下一個節點，達成有效利用記憶體空間的目的。
   * 不同於array，array在記憶體中佔去連續的位置，但無法活用零碎的記憶體位置進行連結。
 
3. > My ideas about design a linked-list:
   >> 目前已經寫出想法，但跑出的值是錯誤的，還在找尋邏輯上不對或缺失的地方。
   * 創造`Mylinkedlist`和`node`兩個類別，在`Mylinkedlist`的`def __init__()`中定義自動創立一節點node.val=None以及有走訪功能的node.next來在後續方便找出第一個節點
   * 實際在`addAtHead(val)`從*頭*加入第一個節點，自動把節點值令為傳入的數值，以及建立好該節點的指南指到`None`
   * 透過`addAtTail(val)`從*尾端*加入第二個節點，並且把第二個節點的前一個元素指南到這個節點。
   * 透過`addAtIndex(val)`從*指定的位置*加入節點，並且把該位置的前一個位置的節點指南到此節點，並把此節點指南到下個節點。
   * 透過`get(index)`找到指定位置對應的值
   * 透過`deleteAtIndex(index)`刪除指定位置對應的值
   * 再次透過`get(index)`找到更新linked-list指定位置對應的值

## reference
1. [Python Data Structures #2: Linked List](https://www.youtube.com/watch?v=JlMyYuY1aXU&t=610s)
2. [Data Structures in Python: Singly Linked Lists -- Deletion](https://www.youtube.com/watch?v=gXY_2wsQf3A)
3. [Linked List: Intro(簡介)](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
4. [Linked List: 新增資料、刪除資料、反轉](http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html#series)

[🔗](#108_1_data-structure-and-algorithm)

---
---
# week 3
 > Topic : Stack and Queue

1. stack and queue 都是一種儲存資料的方式
2. Why stack?
   * 復原(undo)/回上一頁功能的需求
3. Why Queue?
   * 
4. 記法
   * stack 疊盤，後進先出
   * queue 排隊不能插隊，先進先出

> My ideas about making a mini stack?
   * `top()`:先確認是否至少有一個stack，沒有的話，把傳入的數值令成第一個stack。有的話，把最後一個傳入的令成top。
   * `push()`: 建立往上順序性的堆疊stacks。一樣先確認是否至少有一個stack，沒有的話建立第一個stack同時令為top，有的話把stack建立在第一個stack上面，並把最後一個傳入的值令為top。
   * `pop()`:刪除指定的stack。先找到top stack，回溯到指定的index，刪除該stack。
   * `getMin()`:傳回總共stack的個數。先找到top，往下數到最底層的stack。

## Key takeaway
1. 學習程式的兩個階段
   * 熟悉語法
   * 想法轉成程式碼的流程

## reference
1. [CS50 2017 - Lecture 5 - Data Structures](https://www.youtube.com/watch?v=eZQBx8YJ6Zs)
2. [CS50.tv](http://cs50.tv/2017/fall/)

[🔗](#108_1_data-structure-and-algorithm)

---
---
# week 4
- [week 4](#week-4)
  - [setmatch](#setmatch)
    - [ideas](#ideas)
    - [setMatch code](#setmatch-code)
  - [Insertion Sort](#insertion-sort)
  - [QuickSort](#quicksort)
    - [What is quicksort?](#what-is-quicksort)
    - [作業code](#%e4%bd%9c%e6%a5%adcode)
    - [作業流程圖](#%e4%bd%9c%e6%a5%ad%e6%b5%81%e7%a8%8b%e5%9c%96)
  - [Object Oriented Programming](#object-oriented-programming)
    - [What is class?](#what-is-class)
    - [How to change states of object by a line of code?](#how-to-change-states-of-object-by-a-line-of-code)
    - [What if we want to create all the other objects?](#what-if-we-want-to-create-all-the-other-objects)
    - [Time Complexity & Space Complexity](#time-complexity--space-complexity)
      - [Time Complexity](#time-complexity)
      - [Space Complexity](#space-complexity)
  - [References](#references)
## setmatch
### ideas
* 下面例對應的index [0,1,2,3,4,5,6]    [0,1,2,3,4,5,6]
* 假設一 array: a = [2,3,1,4,4,6,4] or [2,1,2,4,4,3,6] or [4,2,1,3,7,11,12]
* 排序後:sorted(a)= [1,2,3,4,4,4,6] or [1,2,2,3,4,4,6] or [1,2,3,4,7,11,12]
* 理想中 array: b = [1,2,3,4,5,6,7]
* 觀察: 
    * 每個位置的數值數值 = 對應的index+1
    * 下一個位置的值等於前一個+1

1. 先把list由小到大排列
2. 從1開始檢查，若下一個不是前一個+1，可能出現的情況：
    * 下一個值比前一個值+2以上 -> 該index有缺失值=index+1
    * 下一個等於前一個 -> 該index有缺失值=index+1，而且此index的值重複了
    > 找到缺失值和重複值可以先存在一個變數內最後一起回傳  

### [setMatch code](https://github.com/okpersist/108_1_DSA/blob/master/week4/SetMismatch.py)
[🔗](#108_1_data-structure-and-algorithm)

---
## Insertion Sort(會努力還債QQ)
## QuickSort
### What is quicksort?
1. 一種快速排序的方式。舉一串隨機排列的數字[99,3,1,5,11,8,52]來說，可以隨機挑選一個基準點，以基準點為中心，比基準點小的放到左邊，比基準點大的放到右邊，全部放好後在原基準點兩邊各選另一個基準點，重複上述的動作，直到所有數字被排整齊為止。
### [作業code](https://nbviewer.jupyter.org/github/okpersist/108_1_DSA/blob/master/week4/quicksort_04113020.ipynb)
### [code 網頁版](https://nbviewer.jupyter.org/github/okpersist/108_1_DSA/blob/master/week4/quicksort_04113020.ipynb)，時間複雜度O(nlogn)
### [作業流程圖](https://github.com/okpersist/108_1_DSA/blob/master/week4/quicksort.svg)

[🔗](#108_1_data-structure-and-algorithm)

---
## Object Oriented Programming
> why I'm learning this: 寫class一直遇到錯誤，所以來學更多Object Oriented Programming  
> [教材: The Python Bible™ | Everything You Need to Program in Python](https://www.udemy.com/course/the-python-bible/) 

### What is class?
1.	我們可以用物件導向程式設計(Object Oriented Programming)來模擬真實世界的東西
2.	`類別class`: 在OOP中創造真實物件的模板或藍圖
3.	`狀態State` & `方法Method`: 前者是在OOP中真實物件的狀態，後者指該真實物件涉及的相關動作，此動作可能會改變物件本身的狀態
4.	影片的例子：造幣工廠。
    * 想像一個造幣工廠，裡面有印新台幣的機器，像是有1元硬幣、100元紙鈔的機器。
    * `類別class`: 在這個例子中指的就是印新台幣的機器本身，他可以創造非常多一模一樣的硬幣或紙鈔，比如1000個1元硬幣或2張100元。
    * `狀態State`: 此例中可把state想成硬幣本身的屬性，比如硬幣的面額、重量、正反面、邊的數量、厚度等等。
    * `方法Method`: 此例中method可想成硬幣可表現的動作，比如翻硬幣，此動作可能改變硬幣的狀態如正反面
5.	每一個`變數類型variable type`在python中都有自己的`特殊類別unique class`
    * eg. class for strings, class for list, and so on.
6.	我們可用`類別變數class variable` 定義`物件的狀態State of object`。`類別變數class variable`就像是一般的變數但只是被我們放在類別裡面
7.	我們可用`方法Method`定義`物件的行為Behavior of object`
8.	我們可以'實體化'一個類別來'創造'個別的物件

#### Example 1
```python
class ntd1:
    value = 1.00
    color = 'gold'
    num_edges = 1
    diameter = 20.0 #mm
    weight = 3.8 #g
    head = True #True代表人頭面，False代表數字面

coin1 = ntd1()
print(type(coin1)) #<class '__main__.ntd'>
print(coin1.value) #1.0

coin1.color = 'green'
print(coin1.color) #green
coin2 = ntd1()
print(coin2.color) #gold
```
藉由這個例子可以了解:
1. 我們可以利用`類別class`創造很多個一樣屬性的物件，但可以在隨後更改物件的性質而不影響到其他物件

### How to change states of object by a line of code?
> Why we need to know this: 我們可以藉由定義`方法Method`更有效率地改變物件的狀態或是對物件執行動作(or物件自己做出動作)
> 此環節將學到類別的 `建構子Constructor` & `解構子Destructor`

#### Example 2
```python
class ntd1:
    def __init__(self,rare=False): #建構子的寫法
        if rare:
        	self.value = 1.25
        else:
        	self.value = 1.00
        self.color = 'gold'
        self.num_edges = 1
        self.diameter = 20.0 
        self.weight = 3.8 
        self.head = True 

coin1 = ntd1(rare=True)
coin2 = ntd1()
print(coin1.value)
print(coin2.value)
```
藉由這個例子可以了解:
1. 我們可以藉由建構子傳入參數有效率的更改物件的狀態
2. `self`指涉某個類別中的實體物件，`self.`接在`.`後面的文字串表現了該實體的屬性
3. `建構子Constructor`方法不會回傳值

#### Example 3
```python
class ntd1:
    def __init__(self,rare=False): #建構子的寫法
        if rare:
        	self.value = 1.25
        else:
        	self.value = 1.00
        self.color = 'gold'
        self.num_edges = 1
        self.diameter = 20.0 
        self.weight = 3.8 
        self.head = True 
       　
    def rust(self):
        self.color = 'green'

coin1 = ntd1()
coin2 = ntd1()
print(coin1.color)
print(coin2.color)

coin1.rust()
print(coin1.color)
print(coin2.color)
```
藉由這個例子可以了解:
1. 任何方法的第一個參數都一定有self，也就是實體本身(也可以定義其他的名字來替代實體，但一般人大都使用self)

#### Example 4
```python
class ntd1:
    def __init__(self,rare=False): #
        if rare:
        	self.value = 1.25
        else:
        	self.value = 1.00
        self.color = 'gold'
        self.num_edges = 1
        self.diameter = 20.0 
        self.weight = 3.8 
        self.head = True 
     　
    def __del__(self):
        print('Coin Spent!!')
        
coin1 = ntd1()
print(coin1)
del coin1
print(coin1)
```
藉由這個例子可以了解:
1. `解構子Destructor` 的定義方式是 'def __del__():'
2. `解構子Destructor`的呼叫方式是輸入 `del 變數名`

[🔗](#108_1_data-structure-and-algorithm)
---
### What if we want to create all the other objects? 
> class `inheritance` and `polymorphism` can help us solve this problem. (繼承與多型)
> 使用`繼承inheritance`可以幫助我們讓子類別輕鬆地複製原類別定義的屬性和方法而不用重新寫一次

#### Example 1 
```python
import random

class coin: #創建一個主類別
	def __init__(self, rare= False, clean=True, Heads= True, **kwargs): #除了傳入預設參數外，也用`**kwargs`傳入多個不一樣的參數並打包成字典輸出

		for key,value in kwargs.items(): #對於多個不特定參數
			setattr(self,key,value) 

		self.is_rare = rare
		self.is_clean = clean
		self.heads = heads

		if self.is_rare:
			self.value = self.original_value * 1.25
		else:
			self.value = self.original_value

		if self.is_clean:
			self.color = self.clean_color
		else:
			self.color = self.rusty_color

	def rust(self):
		self.color = self.rusty_color

	def clean(self):
		self.color = self.clean_color

	def __del__(self):
		print('Coin Spent!')

	def flip(self):
		heads_options = [True,False]
		choice = random.choice(heads_options)
		self.heads = choice

class onedollar(coin):
	def __init__(self):
		data = {
		'original_value': 1.00,
		'clean_color': 'gold',
		'rusty_color': 'green',
		'num_edges': 1,
		'diameter': 20.0, #mm
		'mass': 3.8
		}
	super().__init__(**data) 
```
藉由這個例子可以了解:
1. `super().__init__` : 用於呼叫主類別init的function。
    - `super`表示的就是主類別
    - `*`或`**`在python內有打包(pack)和取出(unpack)的用途，如`**data`此處的`**`意思是pack，把onedollar定義的data字典打包成一個參數傳入主類別的init內。(加上主類別有定義`**kwargs`因此可以傳入未知數量的參數)。`*`用於tuple而`**`用於dictionary。
    > 更多可以參考[Packing and Unpacking Arguments in Python](https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/)
2. 使用可變參數`*args`和`**kwargs`可幫助繼承有效率地被使用。
3. `setattr(self,key,value)`的loop意同於個別設置 `self.key = value`，在此例中就是 `self.original_value = 1.00`、`self.clean_color = 'gold'`...等。

#### Example 2
```python
class fivedollar(coin):
	def __init__(self):
		data = {
		'original_value': 5.00,
		'clean_color': 'sliver',
		'rusty_color': None,
		'num_edges': 1,
		'diameter': 22.0, #mm
		'mass': 4.4
		}
	super().__init__(**data) 
	    def rust(self): #跟母類別重複的function，但此子類有自己的特殊性質因此另外定義
	        self.color = self.clean_color
```
藉由這個例子可以了解:
1. 多型：覆寫母類別已經定義的方法，意即同一個名字的function有多種不同型態，此時只要在子類別的`__init__()`定義即可。


[🔗](#108_1_data-structure-and-algorithm)

---
### Time Complexity & Space Complexity
> Why we need to know time complexity and space complexity: 因為我們希望程式可以高效地幫助我們解決問題，而時間和空間複雜度是一個衡量效能程式的指標。

#### Time Complexity
1. def: 時間複雜度是一種粗略看出程式執行效能的表達式。通常以希臘字母`Ｏ()`表達。
2. 時間複雜度以個別執行步驟作為一單元計算：不用秒數定義時間，而以步驟定義時間是為了在不同的硬體裝置或作業系統都能用相同的標準衡量程式的效能．讓不同的系統在同樣情況下可以被視為同樣的時間複雜度。
3. 通常我們以 **最糟的情況** 來表達時間複雜度，讓人類可以直觀快速地判斷某個程式碼至少可以在`常數倍的__步驟`執行完畢。這樣的表現方式忽略了常數或是係數這種算式上細微的性質，因為我們的目標是大略地掌握`數據的增長趨勢`來判斷程式效能，也因此時間複雜度又稱為`漸進時間複雜度`。
關於時間複雜度一個簡單的例子：
```python
def sayhi():
    print('hi!')
```
上面這個程式碼片段無論n為多少，都只會執行一次，因此時間複雜度紀錄為`O(1)`，意思是這個程式只要一個步驟的執行時間。  
4. 表達的三原則：
    * 只表示最高階的項式 #eg. 若一個程式所需要執行的步驟是 `5n^2+3n`，忽略 `3n` 此項
    * 忽略係數對變數的影響，因為當數據往無限大逼近的時候，係數的影響非常小。#eg. 延續上例，去除`5n^2`的`5`，因此`5t^2+3t`的時間複雜度可表達為`O(n^2)`
    * 若複雜度只有常數，用１取代該常數。


#### Space Complexity
1. def: 程式碼執行所占用的記憶體量，通常以變數量來計算。
2. 用`O()`表達，跟時間複雜度的表達方式相同
3. 時間和記憶體在效能上可以互補：程式可以重複運算更多時間但讓電腦占用比較少的記憶體，或者花比較多的記憶體讓程式重複運算比較少跑的比較快
4. 空間複雜度呈現的概念也是數據的增長趨勢，只是此處用以衡量的是記憶體占用空間的增長趨勢

---
## References
1. [Day5：演算法｜如何衡量程式的效率？——論時間複雜度Time Complexity](https://ithelp.ithome.com.tw/articles/10203082)
2. [初學者學演算法｜從時間複雜度認識常見演算法（一)](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E8%AA%8D%E8%AD%98%E5%B8%B8%E8%A6%8B%E6%BC%94%E7%AE%97%E6%B3%95-%E4%B8%80-b46fece65ba5)
3. [時間複雜度wiki](https://zh.wikipedia.org/wiki/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6)  
4. [`*args` 和 `**kwargs` 是什麼？一次搞懂它們!](https://skylinelimit.blogspot.com/2018/04/python-args-kwargs.html)

[🔗](#108_1_data-structure-and-algorithm)

---
---
# Week6
- [Week6](#week6)
  - [Heap Sort](#heap-sort)
    - [What is a Heap?](#what-is-a-heap)
    - [When do we need Heap Sort？](#when-do-we-need-heap-sort)
    - [Strengths and Weakness of heap sort](#strengths-and-weakness-of-heap-sort)
    - [Make a heap sort algorithm!](#make-a-heap-sort-algorithm)
    - [Reference](#reference)
  - [Merge Sort](#merge-sort)
    - [What is the merge sort?](#what-is-the-merge-sort)
    - [Strengths and Weakness of the merge sort](#strengths-and-weakness-of-the-merge-sort)
    - [Make a merge sort algorithm!](#make-a-merge-sort-algorithm)
    - [Reference](#reference-1)
  - [Heap sort v.s Merge sort](#heap-sort-vs-merge-sort)
  - [如何讀懂別人的code?](#%e5%a6%82%e4%bd%95%e8%ae%80%e6%87%82%e5%88%a5%e4%ba%ba%e7%9a%84code)
    - [為什麼我們需要嘗試讀別人的code?](#%e7%82%ba%e4%bb%80%e9%ba%bc%e6%88%91%e5%80%91%e9%9c%80%e8%a6%81%e5%98%97%e8%a9%a6%e8%ae%80%e5%88%a5%e4%ba%ba%e7%9a%84code)
    - [讀懂別人code的技巧?](#%e8%ae%80%e6%87%82%e5%88%a5%e4%ba%bacode%e7%9a%84%e6%8a%80%e5%b7%a7)
    - [Reference](#reference-2)
- Spyder debug mode
	- 用debug mode除錯可以加速開發效率
	- 功能可分四大區塊，如下圖，可以在`View`的`Panes`內設定
	![](https://i.imgur.com/FAMZtl2.png)
	- 可以透過設定break point 一步一步執行程式除錯或理解程式
	- 下圖是debug mode的按鈕，亦可用命令執行，由左到右分別是：開始測試、執行一個部分（如果是一個函式就執行完該函式）、進入函數、退出函數、執行到下一個中斷點、結束除錯模式
	-![](https://i.imgur.com/JfSBAx6.png)

- quicksort - recursive pseudocode
- `eval`: 把字串形式的function集合併執行的方法

## Heap Sort
### What is Heap?
- 要了解 **堆積排序(Heap Sort)** 演算法，必須先了解 **二元樹(Binary Tree)** 的概念。
    ![堆積樹的圖]()
    - 沒有嚴格定義的 **二元樹(Binary Tree)** 由節點組成，每個節點有0-2個不等的節點，最多不能超過2個，節點之間由上而下一定要有連結。
- 而堆積排序會用到的概念叫做**完全二元樹**。完全二元樹一樣由節點組成，也包含上述的定義，但有個限制：**除了最後一層的節點外**，其餘節點都必須**完全有左右節點**。
- 堆積排序的基本結構就是上述所說的**完全二元樹**，下面我們以**堆積樹**稱呼。堆積樹分成兩種類型：
    - 最大堆積樹(`MaxHeap Tree`)：樹的由上到下每個主節點的值都大於其分支之子節點的值。
    - 最小堆積樹(`MinHeap Tree`)：樹的由上到下每個主節點的值都小於其分支之子節點的值。
    - 補充：推積樹內若有相同值在上下節點關係是可以被接受的!
    - ==**特別注意**==：堆積樹並不保證每個分支的左右互比之大小順序。意思是，有時離底層比較近的元素依然可能比其他分支的偏上元素的值還大。如下圖:
        ![](https://i.imgur.com/aCEXBMK.png)
        -- [name=Jonathan Rasmusson / Former Spotify Engineer, The Agile Samurai]
        - 以此概念我們區分**二元搜尋樹**和**二元堆積**的不同。**二元搜尋樹**指的是限定不論有無同分支，凡上面階層的節點值必定大於下面之節點；**二元堆積**則無此限制。也可以[看其他人的解釋](https://cs.stackexchange.com/questions/27860/whats-the-difference-between-a-binary-search-tree-and-a-binary-heap)。

### When do we need Heap Sort？
- Priority Schedule: 需要排序優先級時常用，比如作業系統或router的優先級排序，或是找最短路徑的演算法！

### Strengths and Weakness of heap sort
- Strengths:
    1. 快：時間複雜度最快 $O(1)$，最慢也只有 $O(nlogn)$。
    2. 節省空間：你只需要一個陣列
    3. 簡潔：短短程式碼就可以實現排序
- Weakness:
    1. 不穩定：可能會改變原本數列中相對的排序（[維基百科說穩定的算法不會出現這種事🤯](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95#%E4%B8%8D%E7%A9%A9%E5%AE%9A%E7%9A%84%E6%8E%92%E5%BA%8F)）

### Make a heap sort algorithm!
> 以最大堆積樹為例
- 為陣列內每個值的index建立二元樹的關係：
    - 主節點index: $(i-1)/2$ -- 以`index`=1的29為例，它的主節點是$(1-1)/2=0$ -> `index #0` ，在圖上確實顯示了這點。
    - 左邊子節點index: $2i+1$ --  以`index`=1的29為例，它的左邊節點是$(2*1)+1=3$ -> `index #3`，在圖上確實顯示了這點。
    - 右邊子節點index: $2i+2$ -- 以`index`=1的29為例，它的左邊節點是$(2*1)+2=4$ -> `index #4`，在圖上確實顯示了這點。
![](https://i.imgur.com/N7VBeYi.png)
-- [name=Jonathan Rasmusson / Former Spotify Engineer, The Agile Samurai]
- Heapify-up：由下而上檢查，讓最大值跑到最上面
    - 從最後一個元素、分回合由下往上比較主節點與子節點大小。在每一回合中，比到子節點的值大於主節點的值就交換兩個值的位置，一路往同個分支的子節點比，沒有更大的就維持原本的排序，然後下一回合從這個元素的主節點元素再往其子節點比較。
- Extract-down：全部比完後，最大值`maxi`會在最上面，把最後一個元素`last`跟最大值交換，並且對被換到頂端的值`last`進行heapify，把第二大的值換到最上面，而且讓`last`可以一路往下比大小放入正確的位置，確保分支在交換後可以保持由上而下由大而小的順序。
- Insert-Up：如果需要插入，把值插入最後一個，再一路Heapify-up跟主節點比大小，遇到比自己小的就交換位置，直到無法交換停止。

### Reference
1. [排序之堆積排序法(Heap Sort)](http://marklin-blog.logdown.com/posts/1910116)
2. [Data Structures and Algorithms Bootcamp](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/)
3. [堆排序維基百科](https://reurl.cc/XXmDxg)
4. [Comparison Sort: Heap Sort(堆積排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)
5. [spyder編輯器](http://epaper.gotop.com.tw/PDFSample/ACL052031.pdf)
6. [Spyder调试python函数](http://www.ishenping.com/ArtInfo/2121767.html)

[🔗](#108_1_data-structure-and-algorithm)

---
## Merge Sort
### What is the merge sort?
- 定義：先分割list至最小單位，進行兩兩元素排序，再不斷合併為原本長度的list的過程
![](https://i.imgur.com/k4NCFtP.png)
-- [name=Jonathan Rasmusson / Former Spotify Engineer, The Agile Samurai]
- MergeSort的排序會歷經三個階段：分割、排序、合併
    - 分割: 每次以`len(list)//2`的方式分割列表
    - 排序: 兩兩單位元素比大小後排序儲存
    - 合併: 合併後重複上述步驟
- $n(1/2)^x =1$ -> 可推得時間複雜度 $O(nlogn)$

### Strengths and Weakness of the merge sort
- Strengths:
    1. 快：時間複雜度最快與最慢都只需 $O(nlogn)$。
    2. 穩定：相較於Heap，不同的狀況中數列的相對位置不會被改變
- Weakness:
    1. 某些情況下比quick sort慢
    2. 某些情況下所需的空間比heap sort多
  
### Make a merge sort algorithm!
- [HW2: Mergesort 網頁版](https://nbviewer.jupyter.org/github/okpersist/108_1_DSA/blob/master/week6/Mergesort_04113020.ipynb)

### Reference
1. [初學者學演算法｜從時間複雜度認識常見演算法（一）](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E8%AA%8D%E8%AD%98%E5%B8%B8%E8%A6%8B%E6%BC%94%E7%AE%97%E6%B3%95-%E4%B8%80-b46fece65ba5)
2. [Comparison Sort: Merge Sort(合併排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)
3. [合併排序-維基百科](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)

[🔗](#108_1_data-structure-and-algorithm)

## Heap sort v.s Merge sort

[🔗](#108_1_data-structure-and-algorithm)

---
## 如何讀懂別人的code?
> 寫作業用debug mode研究別的人code時候常常遇到不解的程式邏輯，或者自己寫的時候常遇到畫流程圖也難想通的語法問題，所以做了功課筆記在這！**TIAN** **JU** **TZ** **JU** **JE** !🙋🏽

### 為什麼我們需要嘗試讀別人的code?
- 這是一個優秀工程師的必備技能：當你需要參與一個大型開源專案、當你在工作上需要被交接新的工作都會需要去理解別人的邏輯並且修正和優化它。
> [面對糟糕的舊代程式碼 Keep Calm & Carry On!](https://www.inside.com.tw/article/4818-rework) 在大型商業專案中，打掉重來是非常危險的行為。當然，如果你是在做實驗，想到新算法可以隨時重寫。如果你跳槽、或剛接手一個新專案，面對看上去異常混亂的舊程式碼，請冷靜下來，忍住打掉重寫的衝動，想想上面這些經驗之談。[name=周萌萌Betty/虎嗅寫作者]
- 站在巨人肩膀上看世界，更有效率地學習：可以了解高手使用的寫扣技巧和邏輯架構，幫助自己日後在思考程式碼更靈活，提高生產力

---
### 讀懂別人code的技巧?
- 基本語法要熟練：初學常撞牆的地方(It's me🥺)搞不懂迴圈/判斷式在稍微微微複雜的程式裡是怎麼演算的，請靠跌倒撞來撞去學起乃，請有耐心，請練習自學不要偷懶。(寫下來提醒自己!讓別人也來督促你!)
- 邊作註解邊改成熟悉的語法格式：寫下來可以確認自己的理解程度，改成自己熟悉的語法格式可以減少陌生引發的挫折感
- 畫流程圖:確認自己理解變數如何在邏輯裡表演
- 了解該專案/程式的目的：若是特定領域可能會需要了解該領域的理論知識、若是算法首先需要了解運算邏輯，讀code才會事半功倍。
- 當專案很大：
    - 先了解系統架構與行為模式，再進行細節的研究
    - 確認程式碼的命名慣例(可以去確認相關的說明文件)
    > 這命名慣例涵蓋的範圍通常包括了變數的名稱、函式的名稱、類別（如果是物件導向的話）的名稱、原始碼檔案、甚至是專案建構目錄的名稱。倘若使用了像設計模式之類的方法，這些名稱更有一些具體的表述方式。
    > ......
    > 對程式碼閱讀來說，熟悉這個做法之所以重要，是因為當你了解整個系統所採用的慣例時，你便能試著以他們所共同操用的語彙來進行理解。[name=王建興 / 清華大學資訊工程博士研究生]
   
-  心情上的技巧: 基礎不好補點基礎再回來看code，研究到煩時想想更艱難不想做的事。
    > 雖然我有時還是會陷入卡殼，想修復一個 bug 卻怎麼也辦不到，但是了解了生產力低谷週期後，我放輕鬆了。
    > 
    > 如果此時狀態不佳，不如接受它，和周圍的伙伴交流一下，做一些簡單的活兒。這樣總比恐慌、錯過 deadline 要好。
    > 
    > 如果你真的什麼都做不了，告訴你一個小技巧 ：想想那些你完全不想碰的事情。再做手邊的事情就舒服多了。[name=Lan Langworth/ 前google工程師，Artillery cofounder and CTO]
- ~~按住page down~~

### Reference
- [讀別人的Code，去讀別人的程式，去看懂它。](http://scratch.gdps.ntpc.edu.tw/home/du-bie-ren-decode-qu-du-bie-ren-de-cheng-shi-qu-kan-dong-ta)
- [閱讀他人的程式碼(1)─讀懂程式碼，使心法皆為我所用](https://www.ithome.com.tw/node/47717)
- [要如何快速地看別人寫的code啊](http://www.programmer-club.com.tw/ShowSameTitleN/c/24364.html)
- [好文: 如何閱讀他人的程式碼](https://blog.longwin.com.tw/2009/05/paper-how-to-read-program-source-code-2009/)
- [寫碼容易，讀碼難](https://www.inside.com.tw/article/4818-rework)
- [一個平庸工程師的自白](https://www.inside.com.tw/article/4690-i-am-a-mediocre-programmer)

[🔗](#108_1_data-structure-and-algorithm)

---
---
# Week8
- [Week 8](#week-8)
  - [recursive concept](#recursive-concept)
  - [Linked Structure for Binary Tree](#linked-structure-for-binary-tree)
    - [Ideas](#%e6%83%b3%e6%b3%95)
    - [Practice](#practice)
## Recursion
> 源自於自己的debug問題所以回來補。從前面的QuickSort, HeapSort, MergeSort, 其實都有運用到遞迴的概念。

### Key Concept
- 一句話解釋遞迴 -- `Divide and Conquer(又名分治法)` : 遞迴就是把一個大問題拆分成小問題，用一個或一組方法解決完小問題，大問題也隨之解決的重複過程。
- <font color=#41D3BD>**呼叫自己**</font>: 只要某個函式會重複呼叫自己本身，即可視為一種遞迴。
- 遞迴的組成：
    - 自我呼叫的方式
    - 終止條件
- 遞迴相關的電腦底層運作:
> 電腦必須要利用記憶體先替你記住這一層的中間值，然後去下一層繼續進行計算，直到終止條件被滿足。[name=Yu-Hsuan Chou @Medium]
::: warning
🎆這就是我debug mode無法理解別人code的部分!
:::

### Reference
- [x][Python 初學第八講 — 遞迴](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-11ed5d300d3d)
- [x][Python 初學第七講 — 函式](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-244862d98c18) 

## Linked Structure for Binary Tree
### ideas
- 先建立節點，節點的屬性有:`index`, `left`, `right`, `val`
- 節點可以執行的動作: `count_len`算長度(也可以視為 `find_height` ), `add_left` or `add_right`新增左右節點, `insert`在指定位置插入節點, `del`刪除節點, `replace`覆蓋節點原本的值
  
### Practice
```python
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def is_left(self):
    return self.left if self.left != None

  def is_right(self):
    return self.right if self.right != None

  def replace(self, node):
    
  def add_left(self, node):
    if self.left == None:
      self.left = node
    elif:
      self.replace(node)
# class BinaryTree:
```
[🔗](#108_1_data-structure-and-algorithm)

---
---
# Week9
## Binary Search Tree
## What is BST?
- $BST$全名是$Binary$ $Search$ $Tree$是一種基於二元樹的樹狀結構，用以效率的尋找所需的資料，時間複雜度為$O(logn)$。
- 一棵合理的BST滿足以下條件:
    - 每個節點都要有顏色
    - 根節點要是黑色
    - 每個葉節點底下都預設有`null`節點，且`null`節點必須是黑色
    - 每個分支的黑色節點數量要一致

:::info
🖋**保持平衡並非二元搜尋樹的必要條件**:
　　無論新增或刪除值，不一定要讓樹一直保持在平衡的狀態(平衡的狀態代表子樹的最大長度差距不超過一，在原本最深層所有葉節點尚未被填滿之前不能把節點放到下層，此時要透過旋轉來滿足此條件)在紅黑樹中才要求樹要保持平衡。
:::

- BST可執行的function:
    - Traversal | 走訪:
        - 走訪是一種拜訪節點的系統化方式，不同的走訪方式可以幫助我們快速從節點找到我們要的資料（許多資料庫的原型就是建基於二元搜尋樹，把節點內儲存的東西換成各式資料而已）
        - Depth First | 以深度優先的搜尋: 分成inorder/preorder/postorder三種
        - Breathe First | 以廣度為優先的搜尋: 以某個節點為搜尋起點，從該起點同一深度的節點走訪完到下層，直到走訪到目標節點。
    - `insert()`新增: 新增節點，讓所有節點依照二元搜尋樹的規則排列好。
    - `modify()`修改: 把所有具有相同值得節點改成另一個值，並讓更新後的所有節點依照二元搜尋樹的規則排列好。
    - `delete()`刪除: 刪除指定的節點，並讓剩下的節點依照二元搜尋樹的規則排列好。
    - `search()`查詢: 搜尋某個節點的值

## Depth First Traversal 
- inorder: Top-down的走訪方式，由下而上從 `left` 開始走訪，依照 `left`->`root`->`right` 的方式走訪節點。左邊下面的子樹走訪完到`root`後再由上而下依照`left`->`root`->`right` 的方式走放右邊的子樹。
- preorder: Top-down的走訪方式，從最上面的 `root` 開始走訪，依照 `root`->`left`->`right` 的方式走訪節點。一樣從左邊的子樹開始，先把所有的`left`走完，再所有左子樹都走完的情況下開始走右子樹。
- postorder: bottom-up的走訪方式，從最後一個 `left` 開始走訪，依照 `left`->`right`->`root` 的方式走訪節點。每個子樹走訪完遇到`null`才回到上一層依照`left`->`right`->`root` 的方式繼續走訪節點

## 如何畫程式流程圖
> 之前只會畫變數流程圖，想開始練習程式流程圖。
- 建構程式流程圖的基本符號，最常用到的是最左邊那行
![](https://i.imgur.com/dVCMHaf.png)
- [name=[Flowchart design. @ concept draw](https://www.conceptdraw.com/How-To-Guide/flowchart-design)]
- 使用標準符號把程式流程與邏輯表達出來即可！
![](https://i.imgur.com/CmKsw0b.jpg)

## Practice
> Ideas
nums = [5, -5, 1, -10, 3]
- `insert()`:把第一個插入的值設成head，其他依照大小放到二元分類樹規則下的地方

### HW
- `modify()`: 要求讓更改後的樹最大長度不超過原本樹深度，且所有相同的值都要被修改到(比如今天原本的BST中有三個3，今天`update()`3改成10，所有BST中的3都要改成10)
- `search()`: 要求在找尋值的時候，若遇到相同的值，返回離`root`最近的一個值就好。
- [HW link](https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.g73e451e679_0_18)
- [How to download ppt by link](https://www.free-power-point-templates.com/articles/how-to-generate-a-link-to-download-a-google-slides-presentation-as-powerpoint/)

[🔗](#108_1_data-structure-and-algorithm)

---
---
# Week11
- [Hash Table & Hash Function原理](#hash-table--hash-function%e5%8e%9f%e7%90%86)
- [What is a Hash table?](#what-is-a-hash-table)
  - [Dictionary](#dictionary)
  - [Hash Table](#hash-table)
  - [Hash Table搜尋的時間複雜度](#hash-table%e6%90%9c%e5%b0%8b%e7%9a%84%e6%99%82%e9%96%93%e8%a4%87%e9%9b%9c%e5%ba%a6)
- [Hash Function](#hash-function)
- [Collision](#collision)
- [Hash & MD5](#hash--md5)
  - [雜湊、加密、壓縮、編碼](#%e9%9b%9c%e6%b9%8a%e5%8a%a0%e5%af%86%e5%a3%93%e7%b8%ae%e7%b7%a8%e7%a2%bc)

## Hash Table & Hash Function原理
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
    
### Hash Table搜尋的時間複雜度
- 最快只要$O(1+\alpha)$ -> $O(1)$：$\alpha$是箱子平均的資料長度，意思是只要經過`hash function`一個步驟後，只要查詢平均箱子的長度就可以找到想要的資料。幸運的話，經過`hash function`一個步驟加上查詢箱子的第一個值就是目標值，時間複雜度是$O(1+1)$ = $O(2)$ -> $O(1)$
- 最慢需要$O(n)$: 很不巧所有的資料都被分到同一個箱子，搜尋效果跟搜尋陣列差不多。
    
[🔗](#108_1_data-structure-and-algorithm)

## Hash Function
> 什麼是hash function?

- 定義：`hash function`用數學的方式決定把資料分到哪一個箱子裡，來解決前述說的占用記憶體的問題。
- 以上圖為例：我們可先把文字形式的`key`透過編碼轉成數字，然後用此編碼數字$mod$箱子的數量(在此例中箱子數量是15，所以用編碼後的數字除以15取其餘數)，就可以得知該把哪一組`key`對應的資料`value`一起放入餘數號碼的箱子。
- 一個好的`hash function`要滿足2個條件：
    1. 速度夠快。盡可能讓`key`經過`hash function`運算後可以平均地分布在不同的箱子內，是一種確保資料可以被更有效率的使用的方式。
    2. `hash function`算出來的值不能多過箱子的數量，否則有的資料沒有箱子放。

## Collision
> 可能會出現把不同的東西要放在同一個箱子而產生衝突($Collision$)的情況，有兩種基本方式可以解決。

- Chaining：把箱子內的元素串起來，如linked-list概念!把同個箱子內第一個之後的元素以linked-list的方式連接起來就可以避免掉覆蓋的問題，就可以避免查找時發生要找A結果是B的衝突情況發生。
- Open Addressing: 找出下一個空的箱子，來避免同一個箱子內要放兩個資料的情況。

[🔗](#108_1_data-structure-and-algorithm)

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

[🔗](#108_1_data-structure-and-algorithm)

---
---
# Week 13
# Graph & BFS & DFS
- [Graph](#graph)
  - [Graph的定義](#graph%e7%9a%84%e5%ae%9a%e7%be%a9)
  - [Graph的Edge的分類](#graph%e7%9a%84edge%e7%9a%84%e5%88%86%e9%a1%9e)
  - [描述Graph的方式](#%e6%8f%8f%e8%bf%b0graph%e7%9a%84%e6%96%b9%e5%bc%8f)
    - [Edge lists | 邊表](#edge-lists--%e9%82%8a%e8%a1%a8)
    - [Adjacency Matrix | 相鄰/伴隨矩陣](#adjacency-matrix--%e7%9b%b8%e9%84%b0%e4%bc%b4%e9%9a%a8%e7%9f%a9%e9%99%a3)
    - [Adjacency List | 相鄰串列:](#adjacency-list--%e7%9b%b8%e9%84%b0%e4%b8%b2%e5%88%97)
  - [Graph的用途範例](#graph%e7%9a%84%e7%94%a8%e9%80%94%e7%af%84%e4%be%8b)
  - [Graph補充](#graph%e8%a3%9c%e5%85%85)
- [BFS 原理](#bfs-%e5%8e%9f%e7%90%86)
  - [從樹狀圖理解BFS](#%e5%be%9e%e6%a8%b9%e7%8b%80%e5%9c%96%e7%90%86%e8%a7%a3bfs)
  - [從Graph理解BFS](#%e5%be%9egraph%e7%90%86%e8%a7%a3bfs)
  - [BFS的特性](#bfs%e7%9a%84%e7%89%b9%e6%80%a7)
- [DFS 原理](#dfs-%e5%8e%9f%e7%90%86)
  - [從樹狀圖理解DFS](#%e5%be%9e%e6%a8%b9%e7%8b%80%e5%9c%96%e7%90%86%e8%a7%a3dfs)
  - [DFS的特性](#dfs%e7%9a%84%e7%89%b9%e6%80%a7)
- [BFS v.s DFS](#bfs-vs-dfs)

[🔗](#108_1_data-structure-and-algorithm)

---
# Graph
> BFS (Breadth First Search) & DFS (Depth First Search) 是Graph資料結構下基本搜尋的方法，所以先提及Graph的概念，再帶到BFS & DFS走訪本身的原理。

- 演算法中的「圖(Graph)」是一種用來表達資料關係的架構，由點(vertex)和邊(edge)組成，如下面兩張圖：
![](https://i.imgur.com/BbtOXyX.png)  
圖一-- [Graph from Wikipedia](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)  
![](https://i.imgur.com/iibdz5n.png)  
圖二-- [Graph by Chiu CC](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)  
其中圖一表示了數值資料間的樹狀關係，圖二表示文字資料間的先後關係(以某大學的CS必修課程為例，此圖表達了修課的順序關係)

## Graph的定義
- def: $G(V+E)$，意指點與線的集合
- V: Vertices，意指點的集合
- E: Edges，意指線的集合

## Graph的Edge的分類
- 有向: 圖之間的邊有方向性，由一邊指向另一邊．或是有雙向的箭頭，如原本的圖二
- 無向: 圖之間的邊沒有方向性，如原本的圖一
    
## 描述Graph的方式
> 共有三種：Edge lists邊表, Adjacency Matrix相鄰/伴隨矩陣, Adjacency List相鄰串列

### Edge lists | 邊表
- def：把所有點之前的邊用一個一個的list表示，組成一個邊表。比如說上面的圖一用Edge lists來表示就是[[1,2],[1,3],[1,4],[2,5],[2,6],[5,9],[5,10],[4,7],[4,8],[7,11],[7,12]]。
- 優點：是個易於理解的資料結構
- 缺點：不易搜尋，想要快速找到一個點連接的線就最差的情況需要$O(n)$才能找到，而其他兩種表達Graph方式就可以解決這個問題。

### Adjacency Matrix | 相鄰/伴隨矩陣
- def：由所有的點組成的二維矩陣，用數字表達兩點有無邊連接，或表達邊的權重。若圖的邊是無權重的，相鄰矩陣中會把兩個點在有邊的連結的情況標記成1，若兩點間沒有邊連結則標記成0。
- 優點：查找快速，快速找到矩陣中的某兩點就可以快速地知道這兩點間有沒有一個線。
- 缺點：耗費儲存空間。

### Adjacency List | 相鄰串列: 
- def：這裡列舉兩種實現方式，一是類似上次實作hash table使用的結構，先用一個list(或array)把所有節點存起來，每個節點後面再用linked-list結構把與該點相連結的點連起來；另一種實現方式(這次作業中使用的方式)先新增節點建立成dict中的key，key後面的value以list型態存放資料。
- 優點：查找快速、可以快速找到點的鄰點
- 缺點：較難判斷邊是否存在、在complete graph的情況下較Adjacency Matrix更耗費空間。
> complete graph: n個節點有n-1條邊的圖形就是complete graph。

## Graph的用途範例
- build social network: 建立社群網路的基礎演算法就是graph的概念。
- path finding: 尋找最短路徑，如Google/Apple在地圖尋找路徑的演算法基礎也是graph。
- find nearest neighbor: 遊戲公司供玩家尋找最鄰近玩家，或提供低延遲的遊戲體驗的算法基礎也是graph。
- map worldwide map: Google如何連結各個不同的網站背後的想法也是使用到graph。
- recommendation: Spotify的推薦系統也使用到graph的概念。

## Graph補充
Adjacency Matrix和Adjacency List兩個概念對比就如下圖－－
![](https://i.imgur.com/2MD0S6L.png)- [Graph by Chiu CC](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)

※更多關於Graph的資料可以參考[Graph: Intro(簡介) by Chiu CC](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)或[Graph演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/Graph.html#2)，這兩篇把Graph相關的概念圖文並茂地解釋的非常清楚。

[🔗](#108_1_data-structure-and-algorithm)

---
# BFS 原理
BFS (Breadth First Search) | 廣度優先搜尋法: 意即從起點開始，以資料層級的廣度為優先下去搜尋的走訪方法。

## 從樹狀圖理解BFS
![](https://i.imgur.com/RaT65F9.gif)- [BFS from Wikipedia](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
以上面這個樹狀圖為例，從`a`為起點開始走訪，走訪到下一層級`b`的時候，不是繼續先往`b`下面的`d`,`e`走，而是從`b`同層級的`c`先走，沒了再往下一層繼續走，這樣以同個層級展開搜尋的方式就是廣度優先搜尋法。

## 從Graph理解BFS
![](https://i.imgur.com/sXxP9ot.png)- [Graph by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206538#overview)
BFS通常使用Queue的方式來存放欲走訪的節點。以上圖為例，若從0為起點以BFS方式走訪，整個流程會是：
- 因為起點0還沒走訪過，**標註**0為**visited**後把0**放入Queue**
- 從Queue中**dequeue**拿出元素0**放入**Path。因為Queue儲存的方式是先進先出(FIFO, First In First Out)，所以剛剛先進去的0先被取出。
- 接下來找尋0的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Queue**；若無，直接**dequeue**下一個元素重複以上的步驟。此例中這步驟0有鄰點1,6,3還沒visit，因此把1,6,3放入Queue，又因為點之間的順序並不影響我們描述一個Graph，所以放入Queue的元素不需要排序。
- 從Queue中**dequeue**拿出目前裡面最先放入的元素1**放入**Path。
- 找尋1的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Queue**。此處再把4,5放入Queue。
重複以上步驟後，我們可以得出BFS走訪的結果是Path，且所有點被標黃表示visited，如下圖：
![](https://i.imgur.com/pvQN1JA.png)- [Graph by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206538#overview)

因此我們可以濃縮出BFS所需執行的幾個步驟：
1. 從起點開始，先標註visited，後放入Queue
2. 從Queue中dequeue一個元素，檢查該元素是否有鄰點可以放入Queue。  
    (1)有鄰點放入Queue: 先標註該點visited，後放入Queue接著重複執行步驟2  
    (2)無鄰點放入Queue: 直接重複執行步驟2
3. 直到所有點遍歷就是成功以BFS走訪完畢。

## BFS的特性
- 空間複雜度: $O(V)$，V(Vertices)是節點的數量，因為所有節點都要被儲存所以複雜度為$O(V)$。
- 時間複雜度: $O(V+E)$，E(Edges)是邊的數量，最差情況需要遍歷每個點所以時間複雜度是$O(V+E)$。
- 完全性: 不論圖形大小和種類為何，只要目標存在BFS一定可以找到該目標，除非該目標不存在於圖中。
- 缺點: 當圖無限大的時候會有無限迴圈不會停止搜尋，儲存空間的要求也會非常大。(耗空間的算法)

[🔗](#108_1_data-structure-and-algorithm)

---

# DFS 原理
DFS (Depth First Search) | 深度優先搜尋法: 意即從起點開始，以資料層級的深度為優先下去搜尋的走訪方法。

## 從樹狀圖理解DFS
![](https://i.imgur.com/GDC2zHa.gif)- [DFS from Wikimedia commons](https://commons.wikimedia.org/wiki/File:Depth-First-Search.gif)
以上面這個樹狀圖為例，從`1`為起點開始走訪，接著到數字`2`所在的第二層，接著是往`2`下面的`3`繼續往下走訪，走到最深之後才回到上面層級的點繼續往下遍歷，這樣在同個支線以深度展開搜尋的方式就是深度優先搜尋法。

![](https://i.imgur.com/bRymp3k.png)- [Graph by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206752#overview)
DFS通常使用Stack的方式來存放欲走訪的節點。以上圖為例，若從0為起點以DFS方式走訪，整個流程會是：
- 因為起點0還沒走訪過，**標註**0為**visited**後把0**push**到**Stack**裡面。
- 從Stack中**pop**拿出元素0**放入**Path。因為Stack儲存的方式是後進先出(LIFO, Last In First Out)，剛剛只進去一個的0當然同時是最後一個所以被取出。
- 接下來找尋0的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Stack**；若無，直接**pop**下一個元素重複以上的步驟。此例中這步驟0有鄰點1,6,3還沒visit，因此把1,6,3放入Stack，又因為點之間的順序並不影響我們描述一個Graph，所以放入Stack的元素一樣不需要排序。
- 從Stack中**pop**拿出目前裡面最後放入的元素3**放入**Path。
- 找尋3的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Stack**。此處再把5放入Stack。
重複以上步驟後，我們可以得出DFS走訪的結果顯示在Path，且所有點被標黃表示visited，如下圖：
![](https://i.imgur.com/uw8lTcd.png)

因此我們可以濃縮出DFS所需執行的幾個步驟：
1. 從起點開始，先標註visited，後放入Stack
2. 從Stack尾端pop一個元素，檢查該元素是否有鄰點可以放入Stack。  
    (1)有鄰點放入Stack: 先標註該點visited，後放入Stack接著重複執行步驟2  
    (2)無鄰點放入Stack: 直接重複執行步驟2
3. 直到所有點遍歷就是成功以DFS走訪完畢。

## DFS的特性
- 空間複雜度: $O(V)$，V(Vertices)是節點的數量，因為所有節點都要被儲存所以複雜度為$O(V)$，跟BFS一樣。
- 時間複雜度: $O(V+E)$，E(Edges)是邊的數量，最差情況需要遍歷每個點所以時間複雜度是$O(V+E)$，也跟BFS一樣。

[🔗](#108_1_data-structure-and-algorithm)

---
# BFS v.s DFS

|比較項目| BFS | DFS |
|:-----|:-----|:-----|
|原理|以廣度為優先的搜尋法|以深度為優先的搜尋法|
|空間複雜度|𝑂(𝑉)|𝑂(𝑉)|
|時間複雜度|𝑂(𝑉+𝐸)|𝑂(𝑉+𝐸)|
|儲存方式|Queue: FIFO，先進先出|Stack: LIFO，後進先出|

[🔗](#108_1_data-structure-and-algorithm)

---
---

# Week 15
- [Dijkstra 原理說明](#dijkstra-%e5%8e%9f%e7%90%86%e8%aa%aa%e6%98%8e)
  - [最短路徑問題定義與分類](#%e6%9c%80%e7%9f%ad%e8%b7%af%e5%be%91%e5%95%8f%e9%a1%8c%e5%ae%9a%e7%be%a9%e8%88%87%e5%88%86%e9%a1%9e)
  - [最短路徑特性](#%e6%9c%80%e7%9f%ad%e8%b7%af%e5%be%91%e7%89%b9%e6%80%a7)
  - [重要觀念: Relaxation, Triangle inequality, Upper-Bound property](#%e9%87%8d%e8%a6%81%e8%a7%80%e5%bf%b5-relaxation-triangle-inequality-upper-bound-property)
    - [Relaxation | 鬆弛](#relaxation--%e9%ac%86%e5%bc%9b)
    - [Triangle inequality | 三角不等式](#triangle-inequality--%e4%b8%89%e8%a7%92%e4%b8%8d%e7%ad%89%e5%bc%8f)
    - [Upper-Bound property | 上界性質](#upper-bound-property--%e4%b8%8a%e7%95%8c%e6%80%a7%e8%b3%aa)
  - [Dijkstra演算法核心概念](#dijkstra%e6%bc%94%e7%ae%97%e6%b3%95%e6%a0%b8%e5%bf%83%e6%a6%82%e5%bf%b5)
  - [Dijkstra演算法特性](#dijkstra%e6%bc%94%e7%ae%97%e6%b3%95%e7%89%b9%e6%80%a7)
  - [自己的想法](#%e8%87%aa%e5%b7%b1%e7%9a%84%e6%83%b3%e6%b3%95)
- [Kruskal 原理說明](#kruskal-%e5%8e%9f%e7%90%86%e8%aa%aa%e6%98%8e)
  - [最小生成樹原理](#%e6%9c%80%e5%b0%8f%e7%94%9f%e6%88%90%e6%a8%b9%e5%8e%9f%e7%90%86)
  - [最小生成樹特性](#%e6%9c%80%e5%b0%8f%e7%94%9f%e6%88%90%e6%a8%b9%e7%89%b9%e6%80%a7)
  - [Kruskal 演算法核心概念](#kruskal-%e6%bc%94%e7%ae%97%e6%b3%95%e6%a0%b8%e5%bf%83%e6%a6%82%e5%bf%b5)
  - [Kruskal 演算法特性](#kruskal-%e6%bc%94%e7%ae%97%e6%b3%95%e7%89%b9%e6%80%a7)
  - [自己的想法](#%e8%87%aa%e5%b7%b1%e7%9a%84%e6%83%b3%e6%b3%95-1)
- [Dijkstra v.s Kruskal](#dijkstra-vs-kruskal)

[🔗](#108_1_data-structure-and-algorithm)

# Dijkstra 原理說明
- Def: Dilkstra演算法的目標在於找到一個點到所有點的最短路徑。此算法不適用於有負權重的圖。由於Dijkstra算法用於處理最短路徑問題，因此以下由最短路徑的原理介紹起，最後以Dijkstra的算法過程和自己的想法做結。

## 最短路徑問題定義與分類
Def: 最短路徑問題顧名思義要找到兩個目標之間的最短路徑，又根據不同目標分成以下四種：
- Point-to-Point shortest Path | 點到點最短路徑：求某點到某點的最短路徑
- Single Source Shortest Paths | 單源最短路徑：求某點到所有點的最短路徑(**此次作業!**)
- Single-Destination Shortest Path | 單一目的地最短路徑: 求所有點到某點的最短路徑
- All Pair Shortest Paths | 全點對最短路徑：求圖上所有點任選兩點的最短路徑

## 最短路徑特性
- [每條最短路徑，都是由其他最短路徑的延展而成](http://www.csie.ntnu.edu.tw/~u91029/Path.html)
- [一個最短路徑，截去尾端後還是最短路徑](http://www.csie.ntnu.edu.tw/~u91029/Path.html)
- [不具權重的圖也可以用權重的特性來模擬，如把所有權重設定為相同即可](http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html)
- [適用於有向圖問題的方法可以適用於無向圖問題，但適用無向圖的方法不一定可以適用有向圖。Dilkstra演算法預設處理有向圖，所以也適用於處理無向圖。](http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html)
- 當起點無法到達某個點，則不存在起點到某點的最短路徑，此時權重會維持無限大
- 重要觀念:Relaxation和其衍生的觀念，分別是Triangle inequality，Upper-Bound property，下面分別介紹

## 重要觀念: Relaxation, Triangle inequality, Upper-Bound property

### Relaxation | 鬆弛
- def: 找到兩點間的捷徑以縮小最短路徑的過程，也就是兩點間不同路徑長短的比大小。

### Triangle inequality | 三角不等式
- def: 算出整個圖的最短路徑後，對於圖中任意兩個點x, y，若是(1)圖表示x指向y的關係、(2)起點是S、(3)兩點間的權重用w(x,y)表示，則此兩點必滿足以下三角不等式－－  

$$\delta(S,y) \leqslant \delta(S,x) + w(x,y)$$

### Upper-Bound property | 上界性質
- def: 一旦已經找到兩個點的最短路徑${\delta(x,y)}$，此後計算其他點的時候此兩點的最短路徑將不會再更新。

[🔗](#108_1_data-structure-and-algorithm)

## Dijkstra演算法核心概念
![](https://i.imgur.com/8kXmobC.gif)-[Dijkstra's algorithm from Wikipedia](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
如圖所示，
1. 先從起點開始，走訪鄰點並計算鄰點到起點的值，取最小的距離存起來。然後把起點標示為已經走訪(算法中可以是把起點從未走訪節點的list中移除)
2. 接著選出一個從起點到未走訪過鄰點最小距離的點，更新起點到這個選中點和其鄰點的最短距離值，標記這個選中點已經走訪，重複第二步驟到所有點都走訪完畢

## Dijkstra演算法特性
- 不適用有負權重的圖
- 為Single Source Shortest Paths單源最短路徑問題的一種算法
- 貪婪算法概念：預設區域最佳解可組合成全域最佳解，解決所有拆解後的子問題則原問題就會隨之解決的概念。

## 自己的想法
- 創造一個紀錄最短路徑的Dijkstra_dict，預設Dijkstra_dict內所有值都是無限大
- 創造一個unvisited_vertice的list紀錄未造訪的節點，初始化是圖中所有節點一開始都未造訪
- 紀錄起點，並把起點從unvisited_vertice移出
- 更新Dijkstra_dict內的值，包含起點到起點本身距離為0，還有起點到其鄰點的<font color=#ef5285>最小</font>權重(距離)更新到Dijkstra_dict內
- <font color=#ef5285>選出</font>在unvisited_vertice內而且在Dijkstra_dict距離最小的點<font color=#ef5285>當作</font>下一個進入Dijkstra_dict計算的點，把該點從unvisited_vertice移出
- 更新Dijkstra_dict內的值，把起點到選出點之鄰點的<font color=#ef5285>最小</font>權重(距離)更新到Dijkstra_dict內
- 重複執行紀錄選點/從unvisited_vertice移出選點/更新Dijkstra_dict的過程，直到unvisited_vertice中沒有節點。

從以上想法可以自己濃縮邏輯上的流程是：
> 選點 >>> 記錄選點 >>> 從從unvisited_vertice移出選點 >>> 更新Dijkstra_dict >>> 直到unvisited_vertice中沒有節點停止，回傳紀錄起點到所有點最短路徑的Dijkstra_dict

[🔗](#108_1_data-structure-and-algorithm)

---

# Kruskal 原理說明
- def: Kruskal演算法目的在於找出一個圖的最小生成樹。因為Kruskal演算法用於處理最小生成樹問題，因此以下由最小生成樹的原理介紹起，最後以Kruskal的算法過程和自己的想法做結。

## 最小生成樹原理
- def: 圖中可生成之最小權重總和的樹。一棵合格的最小生成樹(Minimum Spanning Tree)要滿足以下條件：  
  (1)[此最小生成樹必須包含圖中的每個節點](http://alrightchiu.github.io/SecondRound/minimum-spanning-treeintrojian-jie.html)  
  (2)此最小生成樹的邊剛好會等於圖形所有節點(vertice)的個數減一－－MST擁有剛好 $|V|−1$ 條邊。  
  (3)不存在環於圖中。

## 最小生成樹特性
- [最小生成樹可能並不唯一，同個圖內可能有同樣權重的不同最小生成樹。](http://alrightchiu.github.io/SecondRound/minimum-spanning-treeintrojian-jie.html)
- MST只考慮找出擁有最小權重總和的樹，因此不考慮`root`是哪個節點,`tree`是否balance, `height`是否超過某個值等等。
- 當一個圖中<font color=#ef5285>可</font>找到一棵樹連結所有節點的時候，則稱這個圖擁有一棵生成樹；若一個圖中可生成樹但<font color=#ef5285>無法</font>連結所有節點，則沒有生成樹，而是存在生成森林。

[🔗](#108_1_data-structure-and-algorithm)

## Kruskal 演算法核心概念
![](https://i.imgur.com/dXpIrlS.gif)- [Kruskal's algorithm from Wikipedia](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95) 如圖所示，
1. 把所有的邊依照權重從小排到大
2. 由最小權重的邊開始，在維持不導致環情況發生的條件下，把邊加入最小生成樹的集合內。
3. 直到所有邊都被檢查過停止。

## Kruskal 演算法特性
- 為解決最小生成樹問題的一種算法，適用於處理邊少的稀疏圖。
- 雖然用於解決找出一個**連通加權無向圖**的最小權重總和之樹，也**適用於擁有相同權值的邊**的圖。
    - 當圖的權重有所不同時，最小生成樹會有一個或多個。
    - 當圖的權重皆相同時，每個生成樹都是最小生成樹。
- 貪婪算法概念：與Dijkstra演算法相同，預設區域最佳解可組合成全域最佳解，解決所有拆解後的子問題則原問題就會隨之解決的概念。
> 稀疏圖 v.s 稠密圖：稀疏圖指的是圖的邊數接近一個圖所可以連結最少邊的數量；稠密圖指的是圖的邊數接近一個圖所可以連結的最多邊的數量。
> 假設在一個二維平面上有四個不同座標點，可連結四個點的最少邊數是3，最多邊數是6，此時只有3個邊的圖可被視為稀疏圖，6個邊的圖可被視為稠密圖。

## 自己的想法 
- 在`__init__()`建立一個`weight_dict`字典：一個以`u`&`v`組成的key對應的`w`value字典。
- 定義一個function`addEdge()`:把邊加入圖中，儲存到`weight_dict`。
- 建立一個`sorted_weight_list`用來存放排序過後的權重的邊；建立一個`Kruskal_dict`用來存放最小生成樹。
- 定義一個function`sort_edge()`:排序邊的權重。把`weight_dict`比大小後放進`sorted_weight_list`
- 定義一個function`find_MST()`:從`sorted_weight_list`第一個邊開始，檢查加入這個邊會不會構成一個環，不會的話就加入`Kruskal_dict`
- 直到`Kruskal_dict`連結所有點停止。

# Dijkstra v.s Kruskal
| 比較項目 | Dijkstra | Kruskal |
| :------- | :-------- | :------- |
|核心概念區別|單源最短路徑問題：<br>找出一個點到所有點的最短路徑|最小生成樹問題：<br>找出可連結所有點且具最小權重總和的樹|
|適用圖的類型|有無向的圖皆可|有無權重的圖皆可，稀疏圖為佳|
|都使用貪心算法概念|每次都找從起點算起之最短的路徑，組成最終最短路徑|每次都找權重最小的邊，組合成最小生成樹|

[🔗](#108_1_data-structure-and-algorithm)
