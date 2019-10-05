# 108_1_Data Structure and Algorithm
I'm 汶穗。Here is my weekly learning notes. :)
  * My [Learning check😀](https://hackmd.io/PFMjkciiRYuTuaYk77Be8Q?both)(Other related topics also put there.)
  * My [CS50 notes🖋](https://github.com/okpersist/CS50/tree/master/2013fall)

# Content
- [week 2](#week-2)
- [week 3](#week-3)
- [week 4](#week-4)

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

###### [🔗CONTENTS](#content)

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

###### [🔗CONTENTS](#content)

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

## Insertion Sort
## QuickSort
### []()

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
```
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

### What if we want to create all the other objects? 
`class inheritance and polymorphism`


## References
###### [🔗CONTENTS](#content)
