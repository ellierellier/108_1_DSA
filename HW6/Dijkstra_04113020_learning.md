# HW6: Dijkstra & Kruskal 原理說明、流程圖、學習歷程
陳汶穗｜巨資四B｜04113020  
Period: 2019.12.21 - 2019.01.03

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


```python
from IPython.display import display, Math, Latex
```

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
||||

# 流程圖

## Dijkstra
![](https://i.imgur.com/n38Dxj2.jpg)
## Kruskal
![](https://i.imgur.com/NMlyARm.jpg)

# 作業格式
```python
# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected,  
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        """
        :rtype: dict
        """
```

# HW6測試結果範例
```python
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print('Dijkstra', g.Dijkstra(0))

g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
```
## Dijkstra 測資範例圖
![](https://i.imgur.com/0nmaIMc.png)

## Kruskal 鄰邊權重表
![](https://i.imgur.com/reNEwcb.png)

# 整理程式碼
👇整理原格式和測資


```python
from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        """
        :rtype: dict
        """
        
print('--------Dijkstra--------')
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print('Dijkstra', g.Dijkstra(0))
# Result:  Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}

print('--------Kruskal--------')
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    --------Dijkstra--------
    Dijkstra None
    --------Kruskal--------
    Kruskal None
    

---
👇先看下以鄰邊表建構圖的時候`__init__()`內含的東西


```python
from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
        
    def Dijkstra(self, s):
        """
        :type s: int
        :rtype: dict
        """

    def Kruskal(self):
        """
        :rtype: dict
        """

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print('g.V:', g.V)
print()
print('g.graph:', g.graph)
print()
print('type(g.graph):', type(g.graph))
print()
print('g.graph_matrix:', g.graph_matrix)
print()
print('type(g.graph_matrix):', type(g.graph_matrix))
print()
print('g.graph[0]:', g.graph[0])
print('g.graph_matrix[0]', g.graph_matrix[0])
```

    g.V: 9
    
    g.graph: [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    
    type(g.graph): <class 'list'>
    
    g.graph_matrix: [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    type(g.graph_matrix): <class 'list'>
    
    g.graph[0]: [0, 4, 0, 0, 0, 0, 0, 8, 0]
    g.graph_matrix[0] [0, 0, 0, 0, 0, 0, 0, 0, 0]
    

👉🏾由此可知:
- self.V = 節點數
- self.graph 預設為一個空的list，用鄰邊表寫成graph時是一個包含list的list
- self.graph[n]: 當n存在於list的範圍中時，抓出graph中某一列的list
- self.graph_matrix 預設為一個全部數字為0的(且包含list的)list，是令節點數為行列數建成的
- self.graph_matrix[n]: 當n存在於list的範圍中時，抓出graph_matrix中某一列的list
---

👇看下以`addEdge()`表建構圖的時候`__init__()`內含的東西


```python
from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
        
    def Dijkstra(self, s):
        """
        :type s: int
        :rtype: dict
        """

    def Kruskal(self):
        """
        :rtype: dict
        """

g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('g.V:', g.V)
print()
print('g.graph:', g.graph)
print()
print('type(g.graph):', type(g.graph))
print()
print('g.graph_matrix:', g.graph_matrix)
print()
print('type(g.graph_matrix):', type(g.graph_matrix))
```

    g.V: 4
    
    g.graph: []
    
    type(g.graph): <class 'list'>
    
    g.graph_matrix: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    type(g.graph_matrix): <class 'list'>
    

👉🏾由此可知:
- self.V = 節點數
- self.graph 預設為一個空的list，用`addEdge()`寫成graph時是一個空的list
- self.graph_matrix 仍預設為一個全部數字為0的(且包含list的)list，是令節點數為行列數建成的

---

👇測試上週的defaultdict放進去會如何


```python
from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
#         self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
    
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
        self.graph[u].append(v)
        
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    
    def Kruskal(self):
        """
        :rtype: dict
        """

g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.graph
```




    defaultdict(list, {0: [1, 2, 3], 1: [3], 2: [3]})



👉🏾由此可知:
- self.graph 不可同時預設為defaultdict或`[]`，必須選一個實作
---

## 👇從鄰邊表建構圖的Dijkstra演算法開始寫


```python
from collections import defaultdict


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        Dijkstra_dict = {}
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        for n in self.graph_matrix[start]:
            for num in (self.graph[start]):
                if n < num:
                    elem = 0
                    self.graph_matrix[start][elem] = n
                    elem += 1
        print(self.graph_matrix[start])
        
#         for num in (self.graph[start]):
#             print(num)
#             element = 0
#             print(self.graph_matrix[start][element])
#             print(element)
#             if num != 0 and num < self.graph_matrix[start][element]:
#                 self.graph_matrix[start][element] = num
#             element += 1
#         print(self.graph_matrix[start])
                
        return Dijkstra_dict


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], #start
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(7))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 7 
    unvisited_vertice_after_pop: [0, 1, 2, 3, 4, 5, 6, 8] 
    self.graph[start]: [8, 11, 0, 0, 0, 0, 1, 0, 7] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 0, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 0, 9223372036854775807]
    Dijkstra {}
    

👆發現更新的數值是錯的，換種寫法


```python
from collections import defaultdict


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        Dijkstra_dict = {}
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
#         for n in self.graph_matrix[start]:
#             for num in (self.graph[start]):
#                 if n < num:
#                     elem = 0
#                     self.graph_matrix[start][elem] = n
#                     elem += 1
#         print(self.graph_matrix[start])
        
        for num in (self.graph[start]):
            print(num)
            element = 0
            if num != 0 and num < self.graph_matrix[start][element]:
                self.graph_matrix[start][element] = num
            element += 1
        print(self.graph_matrix[start])
                
        return Dijkstra_dict


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], #start
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(7))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 7 
    unvisited_vertice_after_pop: [0, 1, 2, 3, 4, 5, 6, 8] 
    self.graph[start]: [8, 11, 0, 0, 0, 0, 1, 0, 7] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 0, 9223372036854775807]
    8
    11
    0
    0
    0
    0
    1
    0
    7
    [1, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 0, 9223372036854775807]
    Dijkstra {}
    

👆發現更新的數值還是錯的，再想一下邏輯哪裡錯


```python
from collections import defaultdict


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def compare_num(self, start, add_point):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                self.graph_matrix[start][num] = self.graph[add_point][num]
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.compare_num(start, add_point)
        
        while unvisited_vertice != []:
            add_point = unvisited_vertice.pop(0)
            self.graph_matrix[start] = self.compare_num(start, add_point)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        print(str_list)

        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], #start
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    self.graph_matrix[start]: [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    self.graph_matrix[start]: [0, 4, 8, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    self.graph_matrix[start]: [0, 4, 8, 7, 9223372036854775807, 4, 9223372036854775807, 8, 2]
    self.graph_matrix[start]: [0, 4, 7, 7, 9, 4, 9223372036854775807, 8, 2]
    self.graph_matrix[start]: [0, 4, 7, 7, 9, 4, 9223372036854775807, 8, 2]
    self.graph_matrix[start]: [0, 4, 4, 7, 9, 4, 2, 8, 2]
    self.graph_matrix[start]: [0, 4, 4, 7, 9, 2, 2, 1, 2]
    self.graph_matrix[start]: [0, 4, 4, 7, 9, 2, 1, 1, 2]
    self.graph_matrix[start]: [0, 4, 2, 7, 9, 2, 1, 1, 2]
    ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    Dijkstra {'0': 0, '1': 4, '2': 2, '3': 7, '4': 9, '5': 2, '6': 1, '7': 1, '8': 2}
    

👆新增`compare_num()`比較數字大小並更新`self.graph_matrix[start]`的值，卻寫成保留最小值而非累加最短路徑導致`Dijkstra `最終數字錯誤


```python
from collections import defaultdict


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def comp_num(self, start, add_point):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                else:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
    def compare_num(self, start, add_point):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                self.graph_matrix[start][num] = self.graph[add_point][num]
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.compare_num(start, add_point)
        
        while unvisited_vertice != []:
            mini = sys.maxsize
            locate = 0
            for number in self.graph_matrix[start]:
                if number != 0 and number < mini:
                    mini = number
                    locate += 1
            print('mini:', mini, 'locate:', locate)
            if locate in unvisited_vertice:
                unvisited_vertice.remove(locate)
                print(unvisited_vertice)
                self.graph_matrix[start] = self.comp_num(start, locate)
        
#         str_list = []
#         for n in range(self.V):
#             str_list.append(str(n))
#         print(str_list)
        Dijkstra_dict = {}
#         Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], #start
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

👆發現找最小值會導致infinite loop，修改找最小值的邏輯

而我現在想要:
- 找到`self.graph_matrix[start]`中的最小值和其所在的位置
- 紀錄該節點，並把該節點自`unvisited_vertice`移除
- 更新該節點相關的最短路徑值


```python
from collections import defaultdict


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def comp_num(self, start, add_point):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                else:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
    def compare_num(self, start, add_point):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                self.graph_matrix[start][num] = self.graph[add_point][num]
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.compare_num(start, add_point)
        
        while unvisited_vertice != []:
            for number in self.graph_matrix[start]:
                if number != 0:
                    mini = min(self.graph_matrix[start])
                    index = self.graph_matrix[start].index(min(self.graph_matrix[start]))
            
            print('mini:', mini, 'index:', index)
            if index in unvisited_vertice:
                unvisited_vertice.remove(index)
                print(unvisited_vertice)
                self.graph_matrix[start] = self.comp_num(start, index)
        
#         str_list = []
#         for n in range(self.V):
#             str_list.append(str(n))
#         print(str_list)
        Dijkstra_dict = {}
#         Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], #start
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

👆發現錯誤的不是找最小值的function，是下面的if條件。而且這樣寫不能找出大於0的最小值


```python
from collections import defaultdict


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def comp_num(self, start, add_point):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                else:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
    def compare_num(self, start, add_point):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                self.graph_matrix[start][num] = self.graph[add_point][num]
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.compare_num(start, add_point)
        
        while unvisited_vertice != []:
            mini = sys.maxsize
            locate = 0
            for number in self.graph_matrix[start]:
                if number != 0 and number < mini and self.graph_matrix[start].index(number) in unvisited_vertice:
                    mini = number
                    locate = self.graph_matrix[start].index(number)
            print('mini:', mini, 'locate:', locate)

            unvisited_vertice.remove(locate)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, locate)
            print(self.graph_matrix[start])
        
#         str_list = []
#         for n in range(self.V):
#             str_list.append(str(n))
#         print(str_list)
        Dijkstra_dict = {}
#         Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], #start
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    self.graph_matrix[start]: [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    mini: 4 locate: 1
    [2, 3, 4, 5, 6, 7, 8]
    [0, 4, 8, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    mini: 8 locate: 2
    [3, 4, 5, 6, 7, 8]
    [0, 4, 8, 7, 9223372036854775807, 4, 9223372036854775807, 8, 2]
    mini: 2 locate: 8
    [3, 4, 5, 6, 7]
    [0, 4, 4, 7, 9223372036854775807, 4, 6, 8, 2]
    mini: 6 locate: 6
    [3, 4, 5, 7]
    [0, 4, 4, 7, 9223372036854775807, 4, 6, 7, 2]
    mini: 7 locate: 3
    [4, 5, 7]
    [0, 4, 4, 7, 9, 4, 6, 7, 2]
    mini: 9 locate: 4
    [5, 7]
    [0, 4, 4, 7, 9, 4, 6, 7, 2]
    mini: 9223372036854775807 locate: 0
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-211-f0a178bd562d> in <module>
         91 
         92 # print('--------Dijkstra--------')
    ---> 93 print('Dijkstra', g.Dijkstra(0))
         94 # Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
    

    <ipython-input-211-f0a178bd562d> in Dijkstra(self, s)
         64             print('mini:', mini, 'locate:', locate)
         65 
    ---> 66             unvisited_vertice.remove(locate)
         67             print(unvisited_vertice)
         68             self.graph_matrix[start] = self.comp_num(start, locate)
    

    ValueError: list.remove(x): x not in list


👆發現計算最短路徑的方式有誤而且remove的方式也有問題


```python
from collections import defaultdict


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize and num in unvisited_vertice:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
#     def compare_num(self, start, add_point):
#         for num in range(self.V):
#             if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
#                 self.graph_matrix[start][num] = self.graph[add_point][num]
#         print('self.graph_matrix[start]:', self.graph_matrix[start])
#         return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        
        while unvisited_vertice != []:
            mini = sys.maxsize
            locate = 0
            print(unvisited_vertice)
            for number in self.graph_matrix[start]:
                print(self.graph_matrix[start].index(number))
                if number != 0 and number < mini and self.graph_matrix[start].index(number) in unvisited_vertice:
                    mini = number
                    print('mini',str(number),':',mini)
                    locate = self.graph_matrix[start].index(number)
            print('mini:', mini, 'locate:', locate)

            unvisited_vertice.remove(locate)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, locate, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
#         str_list = []
#         for n in range(self.V):
#             str_list.append(str(n))
#         print(str_list)
        Dijkstra_dict = {}
#         Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    [1, 2, 3, 4, 5, 6, 7, 8]
    0
    1
    mini 4 : 4
    2
    2
    2
    2
    2
    7
    2
    mini: 4 locate: 1
    [2, 3, 4, 5, 6, 7, 8]
    [0, 4, 8, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    
    [2, 3, 4, 5, 6, 7, 8]
    0
    1
    2
    mini 8 : 8
    3
    3
    3
    3
    2
    3
    mini: 8 locate: 2
    [3, 4, 5, 6, 7, 8]
    [0, 4, 8, 7, 9223372036854775807, 4, 9223372036854775807, 8, 2]
    
    [3, 4, 5, 6, 7, 8]
    0
    1
    2
    3
    mini 7 : 7
    4
    1
    4
    2
    8
    mini 2 : 2
    mini: 2 locate: 8
    [3, 4, 5, 6, 7]
    [0, 4, 8, 7, 9223372036854775807, 4, 6, 8, 2]
    
    [3, 4, 5, 6, 7]
    0
    1
    2
    3
    mini 7 : 7
    4
    1
    6
    mini 6 : 6
    2
    8
    mini: 6 locate: 6
    [3, 4, 5, 7]
    [0, 4, 8, 7, 9223372036854775807, 4, 6, 7, 2]
    
    [3, 4, 5, 7]
    0
    1
    2
    3
    mini 7 : 7
    4
    1
    6
    3
    8
    mini: 7 locate: 3
    [4, 5, 7]
    [0, 4, 8, 7, 9, 4, 6, 7, 2]
    
    [4, 5, 7]
    0
    1
    2
    3
    4
    mini 9 : 9
    1
    6
    3
    8
    mini: 9 locate: 4
    [5, 7]
    [0, 4, 8, 7, 9, 4, 6, 7, 2]
    
    [5, 7]
    0
    1
    2
    3
    4
    1
    6
    3
    8
    mini: 9223372036854775807 locate: 0
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-221-381b842fa8b0> in <module>
         95 
         96 # print('--------Dijkstra--------')
    ---> 97 print('Dijkstra', g.Dijkstra(0))
         98 # Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
    

    <ipython-input-221-381b842fa8b0> in Dijkstra(self, s)
         68             print('mini:', mini, 'locate:', locate)
         69 
    ---> 70             unvisited_vertice.remove(locate)
         71             print(unvisited_vertice)
         72             self.graph_matrix[start] = self.comp_num(start, locate, unvisited_vertice)
    

    ValueError: list.remove(x): x not in list


👆發現不能直接用`self.graph_matrix[start].index(number)`取index，若有同樣的數字就會取到錯的index


```python
from collections import defaultdict
import sys

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize and num in unvisited_vertice:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
#     def compare_num(self, start, add_point):
#         for num in range(self.V):
#             if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
#                 self.graph_matrix[start][num] = self.graph[add_point][num]
#         print('self.graph_matrix[start]:', self.graph_matrix[start])
#         return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        
        while unvisited_vertice != []:
            mini = sys.maxsize
            locate = 0
            print(unvisited_vertice)
            for number in self.graph_matrix[start]:
                if number != 0 and number < mini and locate in unvisited_vertice:
                    mini = number
                    print('mini',str(number),':',mini)
                locate += 1
            print('mini:', mini, 'locate:', locate)

            unvisited_vertice.remove(locate)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, locate, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
#         str_list = []
#         for n in range(self.V):
#             str_list.append(str(n))
#         print(str_list)
        Dijkstra_dict = {}
#         Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    [1, 2, 3, 4, 5, 6, 7, 8]
    mini 4 : 4
    mini: 4 locate: 9
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-7-ad894d500811> in <module>
         94 
         95 # print('--------Dijkstra--------')
    ---> 96 print('Dijkstra', g.Dijkstra(0))
         97 # Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
    

    <ipython-input-7-ad894d500811> in Dijkstra(self, s)
         67             print('mini:', mini, 'locate:', locate)
         68 
    ---> 69             unvisited_vertice.remove(locate)
         70             print(unvisited_vertice)
         71             self.graph_matrix[start] = self.comp_num(start, locate, unvisited_vertice)
    

    ValueError: list.remove(x): x not in list


👆換一種寫法還是抓到錯誤的index，把下段獨立出來先想清楚。目標是找到非0的最小值和他的index，同時確認這個index在`unvisited_vertice`內才能更新權重值
```python
[0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
[1, 2, 3, 4, 5, 6, 7, 8]
mini 4 : 4
mini: 4 locate: 9
```


```python
import sys
unvisited_vertice = [1, 2, 3, 4, 5, 6, 7, 8]

# self.graph_matrix[start] = graph_matrix_start 把self.graph_matrix[start]替換成graph_matrix_start寫迴圈
graph_matrix_start = [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    
lst = graph_matrix_start
def find_mini_except_zero(lst):
    index = 0
    mini = sys.maxsize
    for i in lst:
        if i == 0:
            index += 1
        else:
            if i < mini:
                mini = i
            else:
                index += 1
    print('mini:', mini, 'index:', index)

find_mini_except_zero(lst)
```

    mini: 4 index: 8
    

👆還是錯的，繼續寫，無條件加index會導致每次回傳的結果都是最後一個index


```python
import sys
unvisited_vertice = [1, 2, 3, 4, 5, 6, 7, 8]

# self.graph_matrix[start] = graph_matrix_start 把self.graph_matrix[start]替換成graph_matrix_start寫迴圈
graph_matrix_start = [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    
lst = graph_matrix_start
def find_mini_except_zero(lst):
    index = 0
    mini = sys.maxsize
    cur_mini = mini
    for i in lst:
        if i == 0:
            index += 1
        else:
            if i < mini:
                mini = i
                cur_mini = index
                index += 1
            else:
                index += 1
        
    print('mini:', mini, 'index:', cur_mini)

find_mini_except_zero(lst)
```

    mini: 4 index: 1
    

👆多加一個`cur_mini`變數可以成功抓到index的function，丟回原本的演算法嘗試


```python
from collections import defaultdict
import sys

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def find_mini_except_zero(self, lst):
        index = 0
        mini = sys.maxsize
        cur_mini = mini
        
        for i in lst:
            if i == 0:
                index += 1
            else:
                if i < mini:
                    mini = i
                    cur_mini = index
                    index += 1
                else:
                    index += 1
        print('mini:', mini, 'index:', cur_mini)
        
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize and num in unvisited_vertice:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
#     def compare_num(self, start, add_point):
#         for num in range(self.V):
#             if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
#                 self.graph_matrix[start][num] = self.graph[add_point][num]
#         print('self.graph_matrix[start]:', self.graph_matrix[start])
#         return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start])

            unvisited_vertice.remove(index)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, locate, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
#         str_list = []
#         for n in range(self.V):
#             str_list.append(str(n))
#         print(str_list)
        Dijkstra_dict = {}
#         Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    mini: 4 index: 1
    [2, 3, 4, 5, 6, 7, 8]
    [0, 4, 8, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    
    mini: 4 index: 1
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-25-67db7e8ad491> in <module>
        105 
        106 # print('--------Dijkstra--------')
    --> 107 print('Dijkstra', g.Dijkstra(0))
        108 # Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
    

    <ipython-input-25-67db7e8ad491> in Dijkstra(self, s)
         78             index = self.find_mini_except_zero(self.graph_matrix[start])
         79 
    ---> 80             unvisited_vertice.remove(index)
         81             print(unvisited_vertice)
         82             self.graph_matrix[start] = self.comp_num(start, locate, unvisited_vertice)
    

    ValueError: list.remove(x): x not in list


👆新寫法會導致每次都找到最小值，卻不會排除不在`unvisited_vertice`內的數而導致抓到list之外的數字無法運行。繼續嘗試修改：


```python
import sys
unvisited_vertice = [1, 2, 3, 4, 5, 6, 7, 8]

# self.graph_matrix[start] = graph_matrix_start 把self.graph_matrix[start]替換成graph_matrix_start寫迴圈
graph_matrix_start = [0, 4, 9223372036854775807, 3, 9223372036854775807, -100, 9223372036854775807, 8, 9223372036854775807]
    
lst = graph_matrix_start
def find_mini_except_zero(lst, unvisited_vertice):
    index = 0
    mini = sys.maxsize
    cur_mini = mini
    
    for i in lst:
        if i == 0:
            index += 1
        else:
            if i < mini:
                cur_mini = index
                if cur_mini not in unvisited_vertice:
                    index += 1
                else:
                    mini = i
                    index += 1
            else:
                index += 1
        
    print('mini:', mini, 'index:', cur_mini)

find_mini_except_zero(lst, unvisited_vertice)
```

    mini: -100 index: 5
    

👆加入篩選`unvisited_vertice`的條件，再放回演算法嘗試


```python
from collections import defaultdict
import sys

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if i == 0:
                index += 1
            else:
                if i < mini:
                    cur_mini = index
                    if cur_mini not in unvisited_vertice:
                        index += 1
                    else:
                        mini = i
                        index += 1
                else:
                    index += 1

        print('mini:', mini, 'index:', cur_mini)
        
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize and num in unvisited_vertice:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
#     def compare_num(self, start, add_point):
#         for num in range(self.V):
#             if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
#                 self.graph_matrix[start][num] = self.graph[add_point][num]
#         print('self.graph_matrix[start]:', self.graph_matrix[start])
#         return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
#         str_list = []
#         for n in range(self.V):
#             str_list.append(str(n))
#         print(str_list)
        Dijkstra_dict = {}
#         Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    mini: 4 index: 1
    [2, 3, 4, 5, 6, 7, 8]
    [0, 4, 8, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    
    mini: 8 index: 2
    [3, 4, 5, 6, 7, 8]
    [0, 4, 8, 7, 9223372036854775807, 4, 9223372036854775807, 8, 2]
    
    mini: 2 index: 8
    [3, 4, 5, 6, 7]
    [0, 4, 8, 7, 9223372036854775807, 4, 6, 8, 2]
    
    mini: 4 index: 8
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-32-43f5027d5925> in <module>
        109 
        110 # print('--------Dijkstra--------')
    --> 111 print('Dijkstra', g.Dijkstra(0))
        112 # Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
    

    <ipython-input-32-43f5027d5925> in Dijkstra(self, s)
         82             index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)
         83 
    ---> 84             unvisited_vertice.remove(index)
         85             print(unvisited_vertice)
         86             self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
    

    ValueError: list.remove(x): x not in list


👆發現邏輯上用排除法還是會導致`index`錯誤，現在錯誤的情況如下：
- unvisited_vertice = [3, 4, 5, 6, 7]
- graph_matrix_start = [0, 4, 8, 7, 9223372036854775807, 4, 6, 8, 2]
- result: mini: 4 index: 8

```python
import sys
unvisited_vertice = [3, 4, 5, 6, 7]

# self.graph_matrix[start] = graph_matrix_start 把self.graph_matrix[start]替換成graph_matrix_start寫迴圈
graph_matrix_start = [0, 4, 8, 7, 9223372036854775807, 4, 6, 8, 2]

lst = graph_matrix_start
def find_mini_except_zero(lst, unvisited_vertice):
    index = 0
    mini = sys.maxsize
    cur_mini = mini
    
    for i in lst:
        if i == 0:
            index += 1
        else:
            if i < mini:
                cur_mini = index
                if cur_mini not in unvisited_vertice:
                    index += 1
                else:
                    mini = i
                    index += 1
            else:
                index += 1
        
    print('mini:', mini, 'index:', cur_mini)

find_mini_except_zero(lst, unvisited_vertice)
# result: mini: 4 index: 8
```
👇繼續修正


```python
import sys
unvisited_vertice = [3, 4, 5, 6, 7]

# self.graph_matrix[start] = graph_matrix_start 把self.graph_matrix[start]替換成graph_matrix_start寫迴圈
graph_matrix_start = [0, 4, 8, 7, 9223372036854775807, 4, 6, 8, 2]

lst = graph_matrix_start
def find_mini_except_zero(lst, unvisited_vertice):
    index = 0
    mini = sys.maxsize
    cur_mini = mini
    
    for i in lst:
        if index in unvisited_vertice:
            if i < mini:
                cur_mini = index
                mini = i
                index += 1
            else:
                index += 1
        else:
            index += 1

    print('mini:', mini, 'index:', cur_mini)

find_mini_except_zero(lst, unvisited_vertice)
```

    mini: 4 index: 5
    


```python
from collections import defaultdict
import sys

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1

        print('mini:', mini, 'index:', cur_mini)
        
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize and num in unvisited_vertice:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
    
#     def compare_num(self, start, add_point):
#         for num in range(self.V):
#             if self.graph[add_point][num] !=0 and self.graph[add_point][num] < self.graph_matrix[start][num]:
#                 self.graph_matrix[start][num] = self.graph[add_point][num]
#         print('self.graph_matrix[start]:', self.graph_matrix[start])
#         return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        print(str_list)
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    mini: 4 index: 1
    [2, 3, 4, 5, 6, 7, 8]
    [0, 4, 8, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    
    mini: 8 index: 2
    [3, 4, 5, 6, 7, 8]
    [0, 4, 8, 7, 9223372036854775807, 4, 9223372036854775807, 8, 2]
    
    mini: 2 index: 8
    [3, 4, 5, 6, 7]
    [0, 4, 8, 7, 9223372036854775807, 4, 6, 8, 2]
    
    mini: 4 index: 5
    [3, 4, 6, 7]
    [0, 4, 8, 7, 10, 4, 6, 8, 2]
    
    mini: 6 index: 6
    [3, 4, 7]
    [0, 4, 8, 7, 10, 4, 6, 7, 2]
    
    mini: 7 index: 3
    [4, 7]
    [0, 4, 8, 7, 10, 4, 6, 7, 2]
    
    mini: 7 index: 7
    [4]
    [0, 4, 8, 7, 10, 4, 6, 7, 2]
    
    mini: 10 index: 4
    []
    [0, 4, 8, 7, 10, 4, 6, 7, 2]
    
    ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    Dijkstra {'0': 0, '1': 4, '2': 8, '3': 7, '4': 10, '5': 4, '6': 6, '7': 7, '8': 2}
    

👆可以成功走訪所有節點並更新權重，但計算最短路徑的結果是錯的，檢查權重更新的邏輯


```python
from collections import defaultdict
import sys

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1

        print('mini:', mini, 'index:', cur_mini)
        
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        print(str_list)
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6, 7, 8] 
    self.graph[start]: [0, 4, 0, 0, 0, 0, 0, 8, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 4, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    mini: 4 index: 1
    [2, 3, 4, 5, 6, 7, 8]
    [0, 4, 12, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 8, 9223372036854775807]
    
    mini: 8 index: 7
    [2, 3, 4, 5, 6, 8]
    [0, 4, 12, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9, 8, 15]
    
    mini: 9 index: 6
    [2, 3, 4, 5, 8]
    [0, 4, 12, 9223372036854775807, 9223372036854775807, 11, 9, 8, 15]
    
    mini: 11 index: 5
    [2, 3, 4, 8]
    [0, 4, 12, 25, 21, 11, 9, 8, 15]
    
    mini: 12 index: 2
    [3, 4, 8]
    [0, 4, 12, 19, 21, 11, 9, 8, 14]
    
    mini: 14 index: 8
    [3, 4]
    [0, 4, 12, 19, 21, 11, 9, 8, 14]
    
    mini: 19 index: 3
    [4]
    [0, 4, 12, 19, 21, 11, 9, 8, 14]
    
    mini: 21 index: 4
    []
    [0, 4, 12, 19, 21, 11, 9, 8, 14]
    
    ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
    

🌞成功! 👆找到邏輯錯誤的地方，錯誤寫法：
```python
def comp_num(self, start, add_point, unvisited_vertice):
    for num in range(self.V):
        if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
            if self.graph_matrix[start][num] == sys.maxsize:
                self.graph_matrix[start][num] = self.graph[add_point][num] #📌錯誤點
            elif self.graph_matrix[start][num] != sys.maxsize:
                if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
    return self.graph_matrix[start]
```
正確寫法：
```python
def comp_num(self, start, add_point, unvisited_vertice):
    for num in range(self.V):
        if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
            if self.graph_matrix[start][num] == sys.maxsize:
                self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num] #📌修正
            elif self.graph_matrix[start][num] != sys.maxsize:
                if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
    return self.graph_matrix[start]
```
應該要加上起點到目標點的距離，再加上目標點到目標點的鄰點的距離才是起點到目標點鄰點的真正距離。
用別的圖測試看看：
![](https://i.imgur.com/ygnyfhc.png) - [Dijkstra’s Shortest Path Algorithm in Python by Micah Shute
](https://medium.com/cantors-paradise/dijkstras-shortest-path-algorithm-in-python-d955744c7064)


```python
from collections import defaultdict
import sys

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1

        print('mini:', mini, 'index:', cur_mini)
        
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        print()
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        print()
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        print(str_list)
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(6)
g.graph = [[0 , 5 , 10, 0, 2, 0],
[5 , 0 , 2 , 4 , 0 , 0],
[10, 2, 0, 7, 0, 10],
[0 , 4 , 7 , 0 , 3 , 0],
[2 , 0 , 0 , 3 , 0 , 0],
[0, 0 , 10, 0 , 0 , 0],]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5] 
    self.graph[start]: [0, 5, 10, 0, 2, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    
    [0, 5, 10, 9223372036854775807, 2, 9223372036854775807]
    
    mini: 2 index: 4
    [1, 2, 3, 5]
    [0, 5, 10, 5, 2, 9223372036854775807]
    
    mini: 5 index: 1
    [2, 3, 5]
    [0, 5, 7, 5, 2, 9223372036854775807]
    
    mini: 5 index: 3
    [2, 5]
    [0, 5, 7, 5, 2, 9223372036854775807]
    
    mini: 7 index: 2
    [5]
    [0, 5, 7, 5, 2, 17]
    
    mini: 17 index: 5
    []
    [0, 5, 7, 5, 2, 17]
    
    ['0', '1', '2', '3', '4', '5']
    Dijkstra {'0': 0, '1': 5, '2': 7, '3': 5, '4': 2, '5': 17}
    

🌞正確!再嘗試一個圖
![](https://i.imgur.com/n3WgDdw.png)-[Dijkstra Algorithm Example by 
barngrader](https://www.youtube.com/watch?v=0nVYi3o161A)


```python
from collections import defaultdict
import sys

class Graph(): 
    import sys
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys # import sys套件
#         print('sys.maxsize:', sys.maxsize) # 用sys.maxsize表示最大值
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1

        print('mini:', mini, 'index:', cur_mini)
        
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            print('"s" is not in the graph.')
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        print('unvisited_vertice:', unvisited_vertice)
        
        start = unvisited_vertice.pop(s)
        print('start:', start, '\n''unvisited_vertice_after_pop:', unvisited_vertice, '\n''self.graph[start]:', self.graph[start], '\n'
              'self.graph_matrix[start]:', self.graph_matrix[start])
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        print('self.graph_matrix[start]:', self.graph_matrix[start])
        
        #先把自己到自己的距離設為0
        self.graph_matrix[start][start] = 0
        print(self.graph_matrix[start])
        print()
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        print(self.graph_matrix[start])
        print()
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            print(unvisited_vertice)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
            print(self.graph_matrix[start])
            print()
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        print(str_list)
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict

g = Graph(7)
g.graph = [[0, 3, 5, 6, 0, 0, 0],
[3, 0, 0, 2, 0, 0, 0],
[5, 0, 0, 2, 6, 3, 7],
[6, 2, 2, 0, 0, 9, 0],
[0, 0, 6, 0, 0, 5, 2],
[0, 0, 3, 9, 5, 0, 1],
[0, 0, 7, 0, 2, 1, 0]]

# print('--------Dijkstra--------')
print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
```

    unvisited_vertice: [0, 1, 2, 3, 4, 5, 6]
    start: 0 
    unvisited_vertice_after_pop: [1, 2, 3, 4, 5, 6] 
    self.graph[start]: [0, 3, 5, 6, 0, 0, 0] 
    self.graph_matrix[start]: [0, 0, 0, 0, 0, 0, 0]
    self.graph_matrix[start]: [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    [0, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    
    [0, 3, 5, 6, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    
    mini: 3 index: 1
    [2, 3, 4, 5, 6]
    [0, 3, 5, 5, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    
    mini: 5 index: 2
    [3, 4, 5, 6]
    [0, 3, 5, 5, 11, 8, 12]
    
    mini: 5 index: 3
    [4, 5, 6]
    [0, 3, 5, 5, 11, 8, 12]
    
    mini: 8 index: 5
    [4, 6]
    [0, 3, 5, 5, 11, 8, 9]
    
    mini: 9 index: 6
    [4]
    [0, 3, 5, 5, 11, 8, 9]
    
    mini: 11 index: 4
    []
    [0, 3, 5, 5, 11, 8, 9]
    
    ['0', '1', '2', '3', '4', '5', '6']
    Dijkstra {'0': 0, '1': 3, '2': 5, '3': 5, '4': 11, '5': 8, '6': 9}
    

🌞正確!把程式碼修乾淨
# Dijkstra 作業繳交版本


```python
from collections import defaultdict
import sys

class Graph(): 
    import sys
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1
                
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        
        start = unvisited_vertice.pop(s)
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        
        self.graph_matrix[start][start] = 0
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict
```

# 開始寫Kruskal演算法
👇先把Kruskal的`Kruskal()`和`addEdge()`加進來


```python
from collections import defaultdict
import sys

class Graph(): 
    import sys
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1
                
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        
        start = unvisited_vertice.pop(s)
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        
        self.graph_matrix[start][start] = 0
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict
    
#     def addEdge(self,u,v,w):
        
    def Kruskal(self):
        Kruskal_dict = {}
        return Kruskal_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
    
g = Graph(4)
# g.addEdge(0, 1, 10) #Start, Destination, Weight
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
    Kruskal {}
    

👇確認一下defaultdict用下面這個方法會跑出甚麼結果
```python
    def addEdge(self,u,v,w): 
        self.graph[u,v].append(w)
```


```python
from collections import defaultdict
import sys

class Graph(): 
    import sys
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        self.graph = defaultdict(list)
        import sys
    
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1
                
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        
        start = unvisited_vertice.pop(s)
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        
        self.graph_matrix[start][start] = 0
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict 
        
    def addEdge(self,u,v,w): 
        self.graph[u,v].append(w)
        
    def Kruskal(self):
        
        Kruskal_dict = {}
        return Kruskal_dict

# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#           [4, 0, 8, 0, 0, 0, 0, 11, 0],
#           [0, 8, 0, 7, 0, 4, 0, 0, 2],
#           [0, 0, 7, 0, 9, 14, 0, 0, 0],
#           [0, 0, 0, 9, 0, 10, 0, 0, 0],
#           [0, 0, 4, 14, 10, 0, 2, 0, 0],
#           [0, 0, 0, 0, 0, 2, 0, 1, 6],
#           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    Kruskal {}
    




    defaultdict(list,
                {(0, 1): [10],
                 (0, 2): [6],
                 (0, 3): [5],
                 (1, 3): [15],
                 (2, 3): [4]})



👆由此可知需把元組內的元素存成`Kruskal`的output`'A-B':weight`模式。其中`'A-B'`是節點名稱、`weight`是兩點間的權重(資料型態是`int`)，才能符合測資結果格式：
```python
Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        self.graph = defaultdict(list)
        import sys
        
        self.weight_set = {}
        
    def add_node(self, node):
        if node not in self.weight_set:
            self.weight_set.append(node)
        print(self.weight_set)
        
    def addEdge(self,u,v,w): 
        str(u),'-'str(v)
        
    def Kruskal(self):
        
        Kruskal_dict = {}
        return Kruskal_dict
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
print(g.graph[0,1])
g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    [0]
    [0, 1]
    [0, 1]
    [0, 1, 2]
    [0, 1, 2]
    [0, 1, 2, 3]
    [0, 1, 2, 3]
    [0, 1, 2, 3]
    [0, 1, 2, 3]
    [0, 1, 2, 3]
    Kruskal {}
    [10]
    




    defaultdict(list,
                {(0, 1): [10],
                 (0, 2): [6],
                 (0, 3): [5],
                 (1, 3): [15],
                 (2, 3): [4]})



👉🏾想法：把`defaultdict`在addEdge階段就轉成最終output格式。
- 把節點轉成字串
- 加上weight組成dict


```python
def create_str(u,v):
    if u <= v:
        return str(u)+'-'+str(v)
    elif u > v:
        return str(v)+'-'+str(u)
    
print(create_str(1,3))
print(create_str(3,1))
```

    1-3
    1-3
    


```python
dictionary = {}
def add_to_weight_set(string, weight):
    dictionary.setdefault(string, weight)
    return dictionary
    
string = '1-3'
weight = 15
add_to_weight_set(string, weight)

string = '2-3'
weight = 4
add_to_weight_set(string, weight)
```




    {'1-3': 15, '2-3': 4}



👆成功轉成output格式，加入原程式碼


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.weight_set = {}
        
    def create_str(self, u, v):
        if u <= v:
            return str(u)+'-'+str(v)
        elif u > v:
            return str(v)+'-'+str(u)
        
    def add_to_weight_set(self, string, weight):
        self.weight_set.setdefault(string, weight)
        return self.weight_set
    
    def sort_weight_set(self, weight_set):
        temp_dict = sorted(zip(weight_set.values(), weight_set.keys()))
        temp_dict_2 = []
        # [(4, '2-3'), (5, '0-3'), (6, '0-2'), (10, '0-1'), (15, '1-3')]
        
        for items in temp_dict:
            temp_dict_2.append(list(items))
            # [[4, '2-3'], [5, '0-3'], [6, '0-2'], [10, '0-1'], [15, '1-3']]
        
        return temp_dict
        
    def addEdge(self,u,v,w): 
        self.add_to_weight_set(self.create_str(u,v), w)
#         print(self.weight_set)
        
    def Kruskal(self):
        self.sort_weight_set(self.weight_set)
        
        Kruskal_dict = {}
        return Kruskal_dict
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
print(g.graph)
g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    Kruskal {}
    []
    




    []



👉🏾定義`sort_weight_set()`根據權重排序圖的邊


```python
tiny_dict = {}
temp_dict_2 = [[4, '2-3'], [5, '0-3'], [6, '0-2'], [10, '0-1'], [15, '1-3']]
for edges in range(len(temp_dict_2)):  
    key = temp_dict_2[edges][1]
    value = temp_dict_2[edges][0]
    tiny_dict.setdefault(key,value)
        
tiny_dict
```




    {'2-3': 4, '0-3': 5, '0-2': 6, '0-1': 10, '1-3': 15}




```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.weight_set = {}
        self.sorted_weight_set = {}
        
    def create_str(self, u, v):
        if u <= v:
            return str(u)+'-'+str(v)
        elif u > v:
            return str(v)+'-'+str(u)
        
    def add_to_weight_set(self, string, weight):
        self.weight_set.setdefault(string, weight)
        return self.weight_set
    
    def sort_weight_set(self, weight_set):
        temp_list = sorted(zip(weight_set.values(), weight_set.keys()))
        temp_list_2 = []
        # [(4, '2-3'), (5, '0-3'), (6, '0-2'), (10, '0-1'), (15, '1-3')]
        
        for items in temp_list:
            temp_list_2.append(list(items))
            # [[4, '2-3'], [5, '0-3'], [6, '0-2'], [10, '0-1'], [15, '1-3']]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.sorted_weight_set.setdefault(key,value)
        
        return self.sorted_weight_set
        
    def addEdge(self,u,v,w): 
        self.add_to_weight_set(self.create_str(u,v), w)
        
    def Kruskal(self):
        self.sorted_weight_set = self.sort_weight_set(self.weight_set)
        print(self.sorted_weight_set)
        
        Kruskal_dict = {}
        return Kruskal_dict
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
print(g.graph)
g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    {'2-3': 4, '0-3': 5, '0-2': 6, '0-1': 10, '1-3': 15}
    Kruskal {}
    []
    




    []




```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.node_set = []
        self.node_list = []
        self.weight_set = {}
        self.sorted_weight_set = {}
        
    def create_str(self, u, v):
        if u <= v:
            return str(u)+'-'+str(v)
        elif u > v:
            return str(v)+'-'+str(u)
        
    def add_to_weight_set(self, string, weight):
        self.weight_set.setdefault(string, weight)
        return self.weight_set
    
    def sort_weight_set(self, weight_set):
        temp_list = sorted(zip(weight_set.values(), weight_set.keys()))
        temp_list_2 = []
        # [(4, '2-3'), (5, '0-3'), (6, '0-2'), (10, '0-1'), (15, '1-3')]
        
        for items in temp_list:
            temp_list_2.append(list(items))
            # [[4, '2-3'], [5, '0-3'], [6, '0-2'], [10, '0-1'], [15, '1-3']]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.sorted_weight_set.setdefault(key,value)
        
        return self.sorted_weight_set
        
    def addEdge(self,u,v,w): 
        self.add_to_weight_set(self.create_str(u,v), w)
        
        if u not in self.node_list:
            self.node_list.append(u)
        
        self.graph_dict[u,v].append(w)
        
    def Kruskal(self):
        self.sorted_weight_set = self.sort_weight_set(self.weight_set)
        print(self.sorted_weight_set)
        
        print(self.node_list)
        
        Kruskal_dict = {}
        return Kruskal_dict
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
print(g.graph_dict)
# g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    {'2-3': 4, '0-3': 5, '0-2': 6, '0-1': 10, '1-3': 15}
    [0, 1, 2]
    Kruskal {}
    defaultdict(<class 'list'>, {(0, 1): [10], (0, 2): [6], (0, 3): [5], (1, 3): [15], (2, 3): [4]})
    

👆成功return根據權重排序後的dict!接著寫確認有無環的部分  
但發現要確認節點時這樣的寫法會導致沒辦法直接從節點確認是否屬於同一個set，因為key是一個字串。換種方式寫`addEdge()`


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {}
        self.node_pair = []
        self.node_list = []
        
#     def create_str(self, u, v):
        
#     def add_to_weight_set(self, string, weight):

    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        self.graph_dict[u,v].append(w)
        self.node_pair.append([u,v])
        
        if u not in self.node_list:
            self.node_list.append(u)
        if v not in self.node_list:
            self.node_list.append(v)
        
    def Kruskal(self):
        # 按權重排序
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print(self.weight_dict)
        print(self.weight_dict[(2,3)])
        
        
        Kruskal_dict = {}
        return Kruskal_dict
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
print(g.graph_dict)
# g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    {(2, 3): [4], (0, 3): [5], (0, 2): [6], (0, 1): [10], (1, 3): [15]}
    [4]
    Kruskal {}
    defaultdict(<class 'list'>, {(0, 1): [10], (0, 2): [6], (0, 3): [5], (1, 3): [15], (2, 3): [4]})
    

👇測試一下怎麼取出在`dict`內`key`的`node`  
因為dict是無序的不能直接用index取想要的值，所以要先轉成list才能取到


```python
dic = {(2, 3): [4], (0, 3): [5], (0, 2): [6], (0, 1): [10], (1, 3): [15]}
print(list(dic.keys()))
print(type(list(dic.keys())))
print()
print(list(dic.keys())[0])
print(type(list(dic.keys())[0]))
print()
print(list(dic.keys())[0][0])
print(type(list(dic.keys())[0][0]))
```

    [(2, 3), (0, 3), (0, 2), (0, 1), (1, 3)]
    <class 'list'>
    
    (2, 3)
    <class 'tuple'>
    
    2
    <class 'int'>
    


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
#     def create_str(self, u, v):
        
#     def add_to_weight_set(self, string, weight):

    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
#             print(node_one, node_two)

            node_one_set_index = self.node_set.index([node_one])
            node_two_set_index = self.node_set.index([node_two])
            print(node_one_set_index, node_two_set_index)
            print(self.node_set[node_one_set_index], self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print(len_node_one_set, len_node_two_set)
            
#             if len_node_one_set >= len_node_two_set:
#                 if node_two not in self.node_set[node_one_set_index]:
#                     self.node_set[node_one_set_index].append(node_two)
                    
        Kruskal_dict = {}
        return Kruskal_dict
    
g = Graph(4)
# g.addEdge(6, 3, 22) # 自己的
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# print(g.graph_dict)
# g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    self.weight_dict: {(2, 3): [4], (0, 3): [5], (0, 2): [6], (0, 1): [10], (1, 3): [15]}
    self.node_list: [0, 1, 2, 3]
    self.node_set: [[0], [1], [2], [3]]
    
    2 3
    [2] [3]
    1 1
    0 3
    [0] [3]
    1 1
    0 2
    [0] [2]
    1 1
    0 1
    [0] [1]
    1 1
    1 3
    [1] [3]
    1 1
    Kruskal {}
    

👇確認一下找尋集合index的function可否正常運行


```python
node_set = [[6,0], [1,44], [2,3,5,-1], [3]]
def find_set_index(node):
    for sets in range(len(node_set)):
        if node in node_set[sets]:
            return sets
find_set_index(-1)
```




    2




```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
#     def create_str(self, u, v):
        
#     def add_to_weight_set(self, string, weight):

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
            print('node_one:', node_one, 'node_two:', node_two)

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
            print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print('len_node_one_set:', len_node_one_set, 'len_node_two_set:', len_node_two_set)
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index].append(node_two)
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index].append(node_one)
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
            print('MST:',MST)
            print()
                    
        Kruskal_dict = {}
        return Kruskal_dict
    
g = Graph(4)
# g.addEdge(6, 3, 22) # 自己的
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# print(g.graph_dict)
# g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    self.weight_dict: {(2, 3): [4], (0, 3): [5], (0, 2): [6], (0, 1): [10], (1, 3): [15]}
    self.node_list: [0, 1, 2, 3]
    self.node_set: [[0], [1], [2], [3]]
    
    node_one: 2 node_two: 3
    node_one_set_index: 2 node_two_set_index: 3
    node_one_set: [2] node_two_set: [3]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(2, 3): [4]}
    
    node_one: 0 node_two: 3
    node_one_set_index: 0 node_two_set_index: 2
    node_one_set: [0] node_two_set: [2, 3]
    len_node_one_set: 1 len_node_two_set: 2
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 2
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0] node_two_set: [2, 3, 0]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 1
    node_one_set_index: 2 node_two_set_index: 1
    node_one_set: [2, 3, 0] node_two_set: [1]
    len_node_one_set: 3 len_node_two_set: 1
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    node_one: 1 node_two: 3
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0, 1] node_two_set: [2, 3, 0, 1]
    len_node_one_set: 4 len_node_two_set: 4
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    Kruskal {}
    

👆成功印出結果!寫成return格式


```python
MST = {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
def transform_format(MST):
    # dict_keys([(2, 3), (0, 3), (0, 1)]) dict_values([[4], [5], [10]])
    temp_MST = {}
    for k in range(len(MST.keys())):
        key1 = list(MST.keys())[k][0]
        key2 = list(MST.keys())[k][1]
        value = list(MST.values())[k][0]
        print(key1, key2, value)
        
        if key1 <= key2:
            temp_MST.setdefault(str(key1)+'-'+str(key2), value)
        else:
            temp_MST.setdefault(str(key2)+'-'+str(key1), value)
    
    MST = temp_MST
    return MST
transform_format(MST)
```

    2 3 4
    0 3 5
    0 1 10
    




    {'2-3': 4, '0-3': 5, '0-1': 10}




```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def transform_format(MST):
        # dict_keys([(2, 3), (0, 3), (0, 1)]) dict_values([[4], [5], [10]])
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]
            print(key1, key2, value)

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
            print('node_one:', node_one, 'node_two:', node_two)

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
            print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print('len_node_one_set:', len_node_one_set, 'len_node_two_set:', len_node_two_set)
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index].append(node_two)
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index].append(node_one)
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
            print('MST:',MST)
            print()
            # MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
                    
        Kruskal_dict = transform_format(MST)
        return Kruskal_dict
    
g = Graph(4)
# g.addEdge(6, 3, 22) # 自己的
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# print(g.graph_dict)
# g.graph
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    self.weight_dict: {(2, 3): [4], (0, 3): [5], (0, 2): [6], (0, 1): [10], (1, 3): [15]}
    self.node_list: [0, 1, 2, 3]
    self.node_set: [[0], [1], [2], [3]]
    
    node_one: 2 node_two: 3
    node_one_set_index: 2 node_two_set_index: 3
    node_one_set: [2] node_two_set: [3]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(2, 3): [4]}
    
    node_one: 0 node_two: 3
    node_one_set_index: 0 node_two_set_index: 2
    node_one_set: [0] node_two_set: [2, 3]
    len_node_one_set: 1 len_node_two_set: 2
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 2
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0] node_two_set: [2, 3, 0]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 1
    node_one_set_index: 2 node_two_set_index: 1
    node_one_set: [2, 3, 0] node_two_set: [1]
    len_node_one_set: 3 len_node_two_set: 1
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    node_one: 1 node_two: 3
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0, 1] node_two_set: [2, 3, 0, 1]
    len_node_one_set: 4 len_node_two_set: 4
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    2 3 4
    0 3 5
    0 1 10
    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}
    

🌞成功!多測試幾組MST


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def transform_format(MST):
        # dict_keys([(2, 3), (0, 3), (0, 1)]) dict_values([[4], [5], [10]])
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]
            print(key1, key2, value)

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
            print('node_one:', node_one, 'node_two:', node_two)

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
            print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print('len_node_one_set:', len_node_one_set, 'len_node_two_set:', len_node_two_set)
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index].append(node_two)
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index].append(node_one)
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
            print('MST:',MST)
            print()
            # MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
                    
        Kruskal_dict = transform_format(MST)
        return Kruskal_dict
    
# g = Graph(4)
# g.addEdge(0, 1, 10) #Start, Destination, Weight
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

g6 = Graph(7)
g6.addEdge(0, 1, 5)
g6.addEdge(0, 5, 3)
g6.addEdge(1, 0, 5)
g6.addEdge(1, 2, 10)
g6.addEdge(1, 4, 1)
g6.addEdge(1, 6, 4)
g6.addEdge(2, 1, 10)
g6.addEdge(2, 3, 5)
g6.addEdge(2, 6, 8)
g6.addEdge(3, 2, 5)
g6.addEdge(3, 4, 7)
g6.addEdge(3, 6, 9)
g6.addEdge(4, 1, 1)
g6.addEdge(4, 3, 7)
g6.addEdge(4, 5, 6)
g6.addEdge(4, 6, 2)
g6.addEdge(5, 0, 3)
g6.addEdge(5, 4, 6)
g6.addEdge(6, 1, 4)
g6.addEdge(6, 2, 8)
g6.addEdge(6, 3, 9)
g6.addEdge(6, 4, 2)

print('Kruskal', g6.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    self.weight_dict: {(1, 4): [1], (4, 1): [1], (4, 6): [2], (6, 4): [2], (0, 5): [3], (5, 0): [3], (1, 6): [4], (6, 1): [4], (0, 1): [5], (1, 0): [5], (2, 3): [5], (3, 2): [5], (4, 5): [6], (5, 4): [6], (3, 4): [7], (4, 3): [7], (2, 6): [8], (6, 2): [8], (3, 6): [9], (6, 3): [9], (1, 2): [10], (2, 1): [10]}
    self.node_list: [0, 1, 5, 2, 4, 6, 3]
    self.node_set: [[0], [1], [5], [2], [4], [6], [3]]
    
    node_one: 1 node_two: 4
    node_one_set_index: 1 node_two_set_index: 4
    node_one_set: [1] node_two_set: [4]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [1]}
    
    node_one: 4 node_two: 1
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4] node_two_set: [1, 4]
    len_node_one_set: 2 len_node_two_set: 2
    MST: {(1, 4): [1]}
    
    node_one: 4 node_two: 6
    node_one_set_index: 1 node_two_set_index: 5
    node_one_set: [1, 4] node_two_set: [6]
    len_node_one_set: 2 len_node_two_set: 1
    MST: {(1, 4): [1], (4, 6): [2]}
    
    node_one: 6 node_two: 4
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6] node_two_set: [1, 4, 6]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2]}
    
    node_one: 0 node_two: 5
    node_one_set_index: 0 node_two_set_index: 2
    node_one_set: [0] node_two_set: [5]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 5 node_two: 0
    node_one_set_index: 0 node_two_set_index: 0
    node_one_set: [0, 5] node_two_set: [0, 5]
    len_node_one_set: 2 len_node_two_set: 2
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 1 node_two: 6
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6] node_two_set: [1, 4, 6]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 6 node_two: 1
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6] node_two_set: [1, 4, 6]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 0 node_two: 1
    node_one_set_index: 0 node_two_set_index: 1
    node_one_set: [0, 5] node_two_set: [1, 4, 6]
    len_node_one_set: 2 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5]}
    
    node_one: 1 node_two: 0
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0] node_two_set: [1, 4, 6, 0]
    len_node_one_set: 4 len_node_two_set: 4
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5]}
    
    node_one: 2 node_two: 3
    node_one_set_index: 3 node_two_set_index: 6
    node_one_set: [2] node_two_set: [3]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5]}
    
    node_one: 3 node_two: 2
    node_one_set_index: 3 node_two_set_index: 3
    node_one_set: [2, 3] node_two_set: [2, 3]
    len_node_one_set: 2 len_node_two_set: 2
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5]}
    
    node_one: 4 node_two: 5
    node_one_set_index: 1 node_two_set_index: None
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-142-9964e7263c3b> in <module>
        145 g6.addEdge(6, 4, 2)
        146 
    --> 147 print('Kruskal', g6.Kruskal())
        148 # Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
    

    <ipython-input-142-9964e7263c3b> in Kruskal(self)
         90             node_two_set_index = self.find_set_index(node_two)
         91             print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
    ---> 92             print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
         93 
         94             len_node_one_set = len(self.node_set[node_one_set_index])
    

    TypeError: list indices must be integers or slices, not NoneType


👆發現有些元素會在合併的過程消失，因為只有加上單一元素而不是合併兩個集合  
除此之外發現`transform_format()`忘記加上`self`  
還有`Kruskal_dict = transform_format(MST)`應該要寫成`Kruskal_dict = self.transform_format(MST)`


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def transform_format(self, MST):
        # dict_keys([(2, 3), (0, 3), (0, 1)]) dict_values([[4], [5], [10]])
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]
            print(key1, key2, value)

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
            print('node_one:', node_one, 'node_two:', node_two)

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
            print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print('len_node_one_set:', len_node_one_set, 'len_node_two_set:', len_node_two_set)
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index] += self.node_set[node_two_set_index]
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index] += self.node_set[node_one_set_index]
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
            print('MST:',MST)
            print()
            # MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
                    
        Kruskal_dict = self.transform_format(MST)
        return Kruskal_dict
    
# g = Graph(4)
# g.addEdge(0, 1, 10) #Start, Destination, Weight
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

g6 = Graph(7)
g6.addEdge(0, 1, 5)
g6.addEdge(0, 5, 3)
g6.addEdge(1, 0, 5)
g6.addEdge(1, 2, 10)
g6.addEdge(1, 4, 1)
g6.addEdge(1, 6, 4)
g6.addEdge(2, 1, 10)
g6.addEdge(2, 3, 5)
g6.addEdge(2, 6, 8)
g6.addEdge(3, 2, 5)
g6.addEdge(3, 4, 7)
g6.addEdge(3, 6, 9)
g6.addEdge(4, 1, 1)
g6.addEdge(4, 3, 7)
g6.addEdge(4, 5, 6)
g6.addEdge(4, 6, 2)
g6.addEdge(5, 0, 3)
g6.addEdge(5, 4, 6)
g6.addEdge(6, 1, 4)
g6.addEdge(6, 2, 8)
g6.addEdge(6, 3, 9)
g6.addEdge(6, 4, 2)

print('Kruskal', g6.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
# {'1-4': 1, '4-6': 2, '0-5': 3, '0-1': 5, '2-3': 5, '3-4': 7}
```

    self.weight_dict: {(1, 4): [1], (4, 1): [1], (4, 6): [2], (6, 4): [2], (0, 5): [3], (5, 0): [3], (1, 6): [4], (6, 1): [4], (0, 1): [5], (1, 0): [5], (2, 3): [5], (3, 2): [5], (4, 5): [6], (5, 4): [6], (3, 4): [7], (4, 3): [7], (2, 6): [8], (6, 2): [8], (3, 6): [9], (6, 3): [9], (1, 2): [10], (2, 1): [10]}
    self.node_list: [0, 1, 5, 2, 4, 6, 3]
    self.node_set: [[0], [1], [5], [2], [4], [6], [3]]
    
    node_one: 1 node_two: 4
    node_one_set_index: 1 node_two_set_index: 4
    node_one_set: [1] node_two_set: [4]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [1]}
    
    node_one: 4 node_two: 1
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4] node_two_set: [1, 4]
    len_node_one_set: 2 len_node_two_set: 2
    MST: {(1, 4): [1]}
    
    node_one: 4 node_two: 6
    node_one_set_index: 1 node_two_set_index: 5
    node_one_set: [1, 4] node_two_set: [6]
    len_node_one_set: 2 len_node_two_set: 1
    MST: {(1, 4): [1], (4, 6): [2]}
    
    node_one: 6 node_two: 4
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6] node_two_set: [1, 4, 6]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2]}
    
    node_one: 0 node_two: 5
    node_one_set_index: 0 node_two_set_index: 2
    node_one_set: [0] node_two_set: [5]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 5 node_two: 0
    node_one_set_index: 0 node_two_set_index: 0
    node_one_set: [0, 5] node_two_set: [0, 5]
    len_node_one_set: 2 len_node_two_set: 2
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 1 node_two: 6
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6] node_two_set: [1, 4, 6]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 6 node_two: 1
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6] node_two_set: [1, 4, 6]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3]}
    
    node_one: 0 node_two: 1
    node_one_set_index: 0 node_two_set_index: 1
    node_one_set: [0, 5] node_two_set: [1, 4, 6]
    len_node_one_set: 2 len_node_two_set: 3
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5]}
    
    node_one: 1 node_two: 0
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5] node_two_set: [1, 4, 6, 0, 5]
    len_node_one_set: 5 len_node_two_set: 5
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5]}
    
    node_one: 2 node_two: 3
    node_one_set_index: 3 node_two_set_index: 6
    node_one_set: [2] node_two_set: [3]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5]}
    
    node_one: 3 node_two: 2
    node_one_set_index: 3 node_two_set_index: 3
    node_one_set: [2, 3] node_two_set: [2, 3]
    len_node_one_set: 2 len_node_two_set: 2
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5]}
    
    node_one: 4 node_two: 5
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5] node_two_set: [1, 4, 6, 0, 5]
    len_node_one_set: 5 len_node_two_set: 5
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5]}
    
    node_one: 5 node_two: 4
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5] node_two_set: [1, 4, 6, 0, 5]
    len_node_one_set: 5 len_node_two_set: 5
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5]}
    
    node_one: 3 node_two: 4
    node_one_set_index: 3 node_two_set_index: 1
    node_one_set: [2, 3] node_two_set: [1, 4, 6, 0, 5]
    len_node_one_set: 2 len_node_two_set: 5
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    node_one: 4 node_two: 3
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5, 2, 3] node_two_set: [1, 4, 6, 0, 5, 2, 3]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    node_one: 2 node_two: 6
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5, 2, 3] node_two_set: [1, 4, 6, 0, 5, 2, 3]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    node_one: 6 node_two: 2
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5, 2, 3] node_two_set: [1, 4, 6, 0, 5, 2, 3]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    node_one: 3 node_two: 6
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5, 2, 3] node_two_set: [1, 4, 6, 0, 5, 2, 3]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    node_one: 6 node_two: 3
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5, 2, 3] node_two_set: [1, 4, 6, 0, 5, 2, 3]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    node_one: 1 node_two: 2
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5, 2, 3] node_two_set: [1, 4, 6, 0, 5, 2, 3]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    node_one: 2 node_two: 1
    node_one_set_index: 1 node_two_set_index: 1
    node_one_set: [1, 4, 6, 0, 5, 2, 3] node_two_set: [1, 4, 6, 0, 5, 2, 3]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [1], (4, 6): [2], (0, 5): [3], (0, 1): [5], (2, 3): [5], (3, 4): [7]}
    
    1 4 1
    4 6 2
    0 5 3
    0 1 5
    2 3 5
    3 4 7
    Kruskal {'1-4': 1, '4-6': 2, '0-5': 3, '0-1': 5, '2-3': 5, '3-4': 7}
    

🌞成功! 再多試幾個


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def transform_format(self, MST):
        # dict_keys([(2, 3), (0, 3), (0, 1)]) dict_values([[4], [5], [10]])
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]
            print(key1, key2, value)

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
            print('node_one:', node_one, 'node_two:', node_two)

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
            print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print('len_node_one_set:', len_node_one_set, 'len_node_two_set:', len_node_two_set)
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index] += self.node_set[node_two_set_index]
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index] += self.node_set[node_one_set_index]
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
            print('MST:',MST)
            print()
            # MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
                    
        Kruskal_dict = self.transform_format(MST)
        return Kruskal_dict
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    self.weight_dict: {(2, 3): [4], (0, 3): [5], (0, 2): [6], (0, 1): [10], (1, 3): [15]}
    self.node_list: [0, 1, 2, 3]
    self.node_set: [[0], [1], [2], [3]]
    
    node_one: 2 node_two: 3
    node_one_set_index: 2 node_two_set_index: 3
    node_one_set: [2] node_two_set: [3]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(2, 3): [4]}
    
    node_one: 0 node_two: 3
    node_one_set_index: 0 node_two_set_index: 2
    node_one_set: [0] node_two_set: [2, 3]
    len_node_one_set: 1 len_node_two_set: 2
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 2
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0] node_two_set: [2, 3, 0]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 1
    node_one_set_index: 2 node_two_set_index: 1
    node_one_set: [2, 3, 0] node_two_set: [1]
    len_node_one_set: 3 len_node_two_set: 1
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    node_one: 1 node_two: 3
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0, 1] node_two_set: [2, 3, 0, 1]
    len_node_one_set: 4 len_node_two_set: 4
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    2 3 4
    0 3 5
    0 1 10
    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}
    


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def transform_format(self, MST):
        # dict_keys([(2, 3), (0, 3), (0, 1)]) dict_values([[4], [5], [10]])
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]
            print(key1, key2, value)

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
            print('node_one:', node_one, 'node_two:', node_two)

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
            print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print('len_node_one_set:', len_node_one_set, 'len_node_two_set:', len_node_two_set)
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index] += self.node_set[node_two_set_index]
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index] += self.node_set[node_one_set_index]
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
            print('MST:',MST)
            print()
            # MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
                    
        Kruskal_dict = self.transform_format(MST)
        return Kruskal_dict
    
g = Graph(7)
g.addEdge(7, 5, 9)
g.addEdge(1, 2, 7) #Start, Destination, Weight
g.addEdge(1, 4, 5)
g.addEdge(2, 3, 8)
g.addEdge(2, 4, 9)
g.addEdge(2, 5, 7)
g.addEdge(3, 5, 5)
g.addEdge(4, 5, 15)
g.addEdge(4, 6, 6)
g.addEdge(6, 5, 8)
g.addEdge(7, 6, 11)

print('Kruskal', g.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    self.weight_dict: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7], (2, 3): [8], (6, 5): [8], (2, 4): [9], (7, 5): [9], (7, 6): [11], (4, 5): [15]}
    self.node_list: [7, 5, 1, 2, 4, 3, 6]
    self.node_set: [[7], [5], [1], [2], [4], [3], [6]]
    
    node_one: 1 node_two: 4
    node_one_set_index: 2 node_two_set_index: 4
    node_one_set: [1] node_two_set: [4]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [5]}
    
    node_one: 3 node_two: 5
    node_one_set_index: 5 node_two_set_index: 1
    node_one_set: [3] node_two_set: [5]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(1, 4): [5], (3, 5): [5]}
    
    node_one: 4 node_two: 6
    node_one_set_index: 2 node_two_set_index: 6
    node_one_set: [1, 4] node_two_set: [6]
    len_node_one_set: 2 len_node_two_set: 1
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6]}
    
    node_one: 1 node_two: 2
    node_one_set_index: 2 node_two_set_index: 3
    node_one_set: [1, 4, 6] node_two_set: [2]
    len_node_one_set: 3 len_node_two_set: 1
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7]}
    
    node_one: 2 node_two: 5
    node_one_set_index: 2 node_two_set_index: 5
    node_one_set: [1, 4, 6, 2] node_two_set: [3, 5]
    len_node_one_set: 4 len_node_two_set: 2
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7]}
    
    node_one: 2 node_two: 3
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [1, 4, 6, 2, 3, 5] node_two_set: [1, 4, 6, 2, 3, 5]
    len_node_one_set: 6 len_node_two_set: 6
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7]}
    
    node_one: 6 node_two: 5
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [1, 4, 6, 2, 3, 5] node_two_set: [1, 4, 6, 2, 3, 5]
    len_node_one_set: 6 len_node_two_set: 6
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7]}
    
    node_one: 2 node_two: 4
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [1, 4, 6, 2, 3, 5] node_two_set: [1, 4, 6, 2, 3, 5]
    len_node_one_set: 6 len_node_two_set: 6
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7]}
    
    node_one: 7 node_two: 5
    node_one_set_index: 0 node_two_set_index: 2
    node_one_set: [7] node_two_set: [1, 4, 6, 2, 3, 5]
    len_node_one_set: 1 len_node_two_set: 6
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7], (7, 5): [9]}
    
    node_one: 7 node_two: 6
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [1, 4, 6, 2, 3, 5, 7] node_two_set: [1, 4, 6, 2, 3, 5, 7]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7], (7, 5): [9]}
    
    node_one: 4 node_two: 5
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [1, 4, 6, 2, 3, 5, 7] node_two_set: [1, 4, 6, 2, 3, 5, 7]
    len_node_one_set: 7 len_node_two_set: 7
    MST: {(1, 4): [5], (3, 5): [5], (4, 6): [6], (1, 2): [7], (2, 5): [7], (7, 5): [9]}
    
    1 4 5
    3 5 5
    4 6 6
    1 2 7
    2 5 7
    7 5 9
    Kruskal {'1-4': 5, '3-5': 5, '4-6': 6, '1-2': 7, '2-5': 7, '5-7': 9}
    

🌞正確!把兩個演算法整理成一個.py檔


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1
                
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        
        start = unvisited_vertice.pop(s)
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        
        self.graph_matrix[start][start] = 0
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict
    
    def transform_format(self, MST):
        # dict_keys([(2, 3), (0, 3), (0, 1)]) dict_values([[4], [5], [10]])
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]
            print(key1, key2, value)

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
#         print(temp_list)
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
#         print(temp_list_2)
        # [[[4], (2, 3)], [[5], (0, 3)], [[6], (0, 2)], [[10], (0, 1)], [[15], (1, 3)]]
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        print('self.weight_dict:', self.weight_dict)
        
        print('self.node_list:', self.node_list)
        print('self.node_set:', self.node_set)
        print()
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]
            print('node_one:', node_one, 'node_two:', node_two)

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            print('node_one_set_index:', node_one_set_index, 'node_two_set_index:', node_two_set_index)
            print('node_one_set:', self.node_set[node_one_set_index], 'node_two_set:' ,self.node_set[node_two_set_index])
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            print('len_node_one_set:', len_node_one_set, 'len_node_two_set:', len_node_two_set)
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index] += self.node_set[node_two_set_index]
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index] += self.node_set[node_one_set_index]
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
            print('MST:',MST)
            print()
            # MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
                    
        Kruskal_dict = self.transform_format(MST)
        return Kruskal_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}    
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
    self.weight_dict: {(2, 3): [4], (0, 3): [5], (0, 2): [6], (0, 1): [10], (1, 3): [15]}
    self.node_list: [0, 1, 2, 3]
    self.node_set: [[0], [1], [2], [3]]
    
    node_one: 2 node_two: 3
    node_one_set_index: 2 node_two_set_index: 3
    node_one_set: [2] node_two_set: [3]
    len_node_one_set: 1 len_node_two_set: 1
    MST: {(2, 3): [4]}
    
    node_one: 0 node_two: 3
    node_one_set_index: 0 node_two_set_index: 2
    node_one_set: [0] node_two_set: [2, 3]
    len_node_one_set: 1 len_node_two_set: 2
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 2
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0] node_two_set: [2, 3, 0]
    len_node_one_set: 3 len_node_two_set: 3
    MST: {(2, 3): [4], (0, 3): [5]}
    
    node_one: 0 node_two: 1
    node_one_set_index: 2 node_two_set_index: 1
    node_one_set: [2, 3, 0] node_two_set: [1]
    len_node_one_set: 3 len_node_two_set: 1
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    node_one: 1 node_two: 3
    node_one_set_index: 2 node_two_set_index: 2
    node_one_set: [2, 3, 0, 1] node_two_set: [2, 3, 0, 1]
    len_node_one_set: 4 len_node_two_set: 4
    MST: {(2, 3): [4], (0, 3): [5], (0, 1): [10]}
    
    2 3 4
    0 3 5
    0 1 10
    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}
    


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1
                
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        
        start = unvisited_vertice.pop(s)
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        
        self.graph_matrix[start][start] = 0
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict
    
    def transform_format(self, MST):
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index] += self.node_set[node_two_set_index]
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index] += self.node_set[node_one_set_index]
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
        Kruskal_dict = self.transform_format(MST)
        return Kruskal_dict

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7], 
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print('Dijkstra', g.Dijkstra(0))
# Dijkstra {'0':0, '1':4, '2':12, '3':19, '4':21, '5':11, '6':9, '7':8, '8':14}    
    
g = Graph(4)
g.addEdge(0, 1, 10) #Start, Destination, Weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print('Kruskal', g.Kruskal())
# Result: Kruskal {'2-3':4, '0-3':5, '0-1':10}
```

    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}
    

# 最終繳交版本


```python
from collections import defaultdict
import sys

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def find_mini_except_zero(self, lst, unvisited_vertice):
        index = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in lst:
            if index in unvisited_vertice:
                if i < mini:
                    cur_mini = index
                    mini = i
                    index += 1
                else:
                    index += 1
            else:
                index += 1
                
        return cur_mini
    
    def comp_num(self, start, add_point, unvisited_vertice):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            return {}
        
        unvisited_vertice = []
        
        for vertex in range(self.V):
            unvisited_vertice.append(vertex)
        
        start = unvisited_vertice.pop(s)
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        
        self.graph_matrix[start][start] = 0
        
        add_point = start
        self.graph_matrix[start] = self.comp_num(start, add_point, unvisited_vertice)
        
        while unvisited_vertice != []:
            index = self.find_mini_except_zero(self.graph_matrix[start], unvisited_vertice)

            unvisited_vertice.remove(index)
            self.graph_matrix[start] = self.comp_num(start, index, unvisited_vertice)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict
    
    def transform_format(self, MST):
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_index(self, node):
        for node_set_index in range(len(self.node_set)):
            if node in self.node_set[node_set_index]:
                return node_set_index
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def addEdge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]

            node_one_set_index = self.find_set_index(node_one)
            node_two_set_index = self.find_set_index(node_two)
            
            len_node_one_set = len(self.node_set[node_one_set_index])
            len_node_two_set = len(self.node_set[node_two_set_index])
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_index]:
                    self.node_set[node_one_set_index] += self.node_set[node_two_set_index]
                    self.node_set[node_two_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_index]:
                    self.node_set[node_two_set_index] += self.node_set[node_one_set_index]
                    self.node_set[node_one_set_index] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
        Kruskal_dict = self.transform_format(MST)
        return Kruskal_dict
    
# Reference
# Dijkstra
# - [Python Dictionary](https://www.programiz.com/python-programming/dictionary)
# - [演算法筆記 by someone from 師大資工](http://www.csie.ntnu.edu.tw/~u91029/Path.html)
# - [Dijkstra's algorithm from Wikipedia](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
# - [Shortest Path：Intro(簡介) by Chiu, Hao-Chien](http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html)
# - [Dijkstra’s shortest path algorithm | Greedy Algo-7](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

# Kruskal
# - [克魯斯克爾演算法 from Wikipedia](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
# - [演算法筆記 by someone from 師大資工](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html#2)
# - [Minimum Spanning Tree：Intro(簡介)](http://alrightchiu.github.io/SecondRound/minimum-spanning-treeintrojian-jie.html)
# - [Minimum Spanning Tree：Kruskal's Algorithm](http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html)

# Others
# - [List of LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
```

# Reference
Dijkstra

- [Python Dictionary](https://www.programiz.com/python-programming/dictionary)
- [演算法筆記 by someone from 師大資工](http://www.csie.ntnu.edu.tw/~u91029/Path.html)
- [Dijkstra's algorithm from Wikipedia](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
- [Shortest Path：Intro(簡介) by Chiu, Hao-Chien](http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html)
- [Dijkstra’s shortest path algorithm | Greedy Algo-7](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

Kruskal
- [克魯斯克爾演算法 from Wikipedia](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
- [演算法筆記 by someone from 師大資工](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html#2)
- [Minimum Spanning Tree：Intro(簡介)](http://alrightchiu.github.io/SecondRound/minimum-spanning-treeintrojian-jie.html)
- [Minimum Spanning Tree：Kruskal's Algorithm](http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html)

Others
- [List of LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
