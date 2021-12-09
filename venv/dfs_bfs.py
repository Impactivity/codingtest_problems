#-*- coding: utf-8 -*-

import sys
from collections import deque

read = sys.stdin.readline

n = int(input())

graph = [list(map(int, read().rstrip() )) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
answer = []
house = 0

queue = deque()


dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(graph,i ,j):
    global house,visited,n,queue
    queue.append([i,j])
    graph[i][j] = 0
    house = 1
    while queue:
        x,y = queue.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < n :
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 0
                    house += 1
                    queue.append((nx,ny))
    return visited

for i in range (n):
    for j in range (n):
        if graph[i][j] == 1 :
            bfs(graph,i , j)
            answer.append(house)



print(len(answer))

answer.sort()
for i in answer:
    print(i)





#
# import sys
# from collections import deque
#
# read = sys.stdin.readline
#
# n=int(sys.stdin.readline())
# graph =[sys.stdin.readline() for _ in range(n)]
#
# visited = [[0] * n for _ in range(n)]
# answer = []
# house = 0
#
# queue = deque()
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
#
#
# def bfs(graph,i ,j):
#     global house,visited,n,queue
#     queue.append([i,j])
#
#     while queue:
#         x,y = queue.popleft()
#         if x == n-1 and y == n-1 :
#             break
#
#         for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]
#
#             if 0 <= nx < n and 0 <= ny < n :
#                 if visited[nx][ny] == 0 and graph[nx][ny] == '1':
#                     visited[nx][ny] = 1
#
#                     house += 1
#                     queue.append([nx,ny])
#     return visited
#
# for i in range (n):
#     for j in range (n):
#         if graph[i][j] == '1' :
#             bfs(graph,i , j)
#             answer.append(house)
#             house = 0
#
#
# count = 0
# for i in answer :
#     if i != 0:
#         count+=1
# print(count)
#
# for i in answer:
#     if i != 0 : print(i)
#












# read = sys.stdin.readline
# n,m = map(int, read().split())
#
# graph = [read().rstrip() for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# queue = deque()
# queue.append([0,0])
# visited[0][0] = 1
#
#
# while queue:
#     x,y = queue.popleft()
#
#     if x == n-1 and y == m-1 :
#         print(visited[x][y])
#         break
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m :
#             if visited[nx][ny] == 0 and graph[nx][ny] == '1':
#                 queue.append((nx,ny))
#                 visited[nx][ny] = visited[x][y]+1