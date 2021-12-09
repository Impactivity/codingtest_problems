#-*- coding: utf-8 -*-


#from collections import deque

#
# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
#
#
# root_node = 1
#
#
# def BFS_with_adj_list(graph, root):
#     visited = []
#     queue = deque([root])
#
#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             queue += graph[n] - set(visited)
#     return visited


#print(BFS_with_adj_list(graph_list, root_node))



#n개의 정점, m개의 간선 , 시작할번호 v


import sys
#from __future__ import print_function

from collections import deque

read = sys.stdin.readline

n,m,v  = map(int, read().split())


#n개의 정점, m개의 간선 , 시작할번호 v

graph = [[] for _ in range(n + 1)]
stack = []

queue = deque()

for i in range(m):
    a,b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

visit1 = [0] * (n+1)
visit2 = []

# def dfs(graph, queue):
#     stack.append(v)
#     while stack:
#         node = stack.pop()
#         if node not in visit1 and node != 0:
#             visit1.append(node)
#             stack.extend(graph[node])
#     return visit1

def dfs(v):
    print(v)
    global visit1, graph
    visit1[v] = 1
    for i in sorted(graph[v]):
        if visit1[i] != 1:
            dfs(i)

dfs(1)








# def dfs(v):
#     print(v, end=' ')
#     global visit1, graph
#     visit1[v] = 1
#     for i in sorted(graph[v]):
#         if visit1[i]!=1:
#             dfs(i)
# dfs(v)
# print(v)

def bfs(graph, queue):
    queue.append(v)
    while queue:
        node = queue.popleft()
        if node not in visit2 and node != 0:
            visit2.append(node)
            queue.extend(graph[node])
    for i in visit2:
        print(i)
    return 1
#print(dfs(graph,stack))

#bfs(graph,queue)


from collections import deque

# graph = { 'A':['B'] , 'B':['A','C','D'], 'C':['A','B'], 'D':['A','C'] }
#
#
#
#
# def dfs(graph, start_node) :
#     visit = []
#     stack = [start_node]
#
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])
#     return visit
#
#
# def bfs(graph, start_node):
#     visit = []
#     queue = deque()
#
#     queue.append(start_node)
#     while queue:
#         node = queue.popleft()
#         if node not in visit:
#             visit.append(node)
#             queue.extend(graph[node]) #extend는 literal 형태로 삽입, append는 원소 하나 삽입
#
#     return visit
#
# #print(graph['A'])
# print(dfs(graph, 'A'))
#
# print(bfs(graph, 'A'))