# Author: 汶穗
# Period: 2019.12.06 - 2019.12.20
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = self.graph[s]
        len_of_adja_list = len(self.graph[s])
        for i in adjacency_list:
            if i not in queue and i not in bfs_traversal:
                queue.append(i)
        return queue
    
    def bfs_recursive(self, s, queue, bfs_traversal):
        if s not in bfs_traversal:
            if s not in queue:
                queue.append(s)

                bfs_traversal.append(queue[0])
                queue.pop(0)

                cur_node = bfs_traversal[0]

                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
            
            else:
                bfs_traversal.append(queue[0])
                cur_node = queue[0]
                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                queue.pop(0)
                  
        return s, queue, bfs_traversal
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if self.graph[s] == []:
            return []
        
        s, queue, bfs_traversal = self.bfs_recursive(s, queue, bfs_traversal)

        while queue != []:
            for num in queue:
                self.bfs_recursive(num, queue, bfs_traversal)
                
        return bfs_traversal
    
    def add_adjacency(self, num, stack):
        adjacency_list = self.graph[num]
        for n in adjacency_list:
            if n not in stack:
                stack.append(n)
        return stack
        
    def DFS(self, s):
        dfs_traversal = []
        stack = []
        
        if self.graph[s] == []:
            return []

        stack.append(s)
        
        while stack != []:
            last_num = stack.pop() #記得這時候已經把最後一個數值從stack中pop出來
            if last_num not in dfs_traversal:
                dfs_traversal.append(last_num)        
                stack = self.add_adjacency(last_num, stack)
                    
        return dfs_traversal

# Reference
# - [佇列(Queue)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Queues/queue.html)
# - [堆疊(Stack)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Queues/stack.html)
# - [Graph演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/Graph.html#2)
# - [Graph: Intro(簡介)](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)
# - [廣度優先搜尋Wikipedia](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
# - [基礎資料結構(4)---圖形結構](http://marklin-blog.logdown.com/posts/1535607-underlying-data-structure-3-the-graphic-structure)
# - [廣度優先搜尋法(Breadth-First Search)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/breadth-first_search.html)
# - [Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206538#overview)
