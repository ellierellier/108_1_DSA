# 108_1_Data Structure and Algorithm
I'm 汶穗。Here is my weekly learning notes. :)
  * My [Learning check😀](https://hackmd.io/PFMjkciiRYuTuaYk77Be8Q?both)(Other related topics also put there.)
  * My [CS50 notes🖋](https://github.com/okpersist/CS50/tree/master/2013fall)

# [Week 6🤯](#week6)

# Content
- [week 2](#week-2)
  - [reference](#reference)
- [week 3](#week-3)
  - [Key takeaway](#key-takeaway)
  - [reference](#reference-1)
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
 - [Week6](#week6)
   - [Heap Sort](#heap-sort)
     - [What is Heap?](#what-is-heap)
     - [When do we need Heap Sort？](#when-do-we-need-heap-sort)
     - [Strengths and Weakness of heap sort](#strengths-and-weakness-of-heap-sort)
     - [Make a heap sort algorithm!](#make-a-heap-sort-algorithm)
  - [Reference](#reference)

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
# Week6
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
### Reference
1. [初學者學演算法｜從時間複雜度認識常見演算法（一）](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E8%AA%8D%E8%AD%98%E5%B8%B8%E8%A6%8B%E6%BC%94%E7%AE%97%E6%B3%95-%E4%B8%80-b46fece65ba5)
2. [Comparison Sort: Merge Sort(合併排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)
3. [合併排序-維基百科](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)

## Heap sort v.s Merge sort
## 如何讀懂別人的程式?
> 寫作業用debug mode研究別的人code時候常常遇到不解的程式邏輯，或者自己寫的時候常遇到難解的語法問題，可能問題太低級助教們也希望我可以自己多想想QQ，所以做了功課筆記在這！TIAN JU TZ JU JE! 🙋🏽

[🔗](#108_1_data-structure-and-algorithm)
