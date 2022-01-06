#-*- coding: utf-8 -*-
from collections import deque
import sys
#sys.setrecursionlimit(10000000)
# n의 범위는 1<= n <= 1000 , m의점위는 0 <= m <= n*(n-1)/2
# 입력을 받을 때 input().split()으로 받으면 시간초과가 떠서 read().split()으로 변경하고
# 컴파일 돌리니깐 정상적으로 컴파일됨

read = sys.stdin.readline

n,m = map(int, read().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int , read().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(num):
    queue = deque()
    visited[num] = 1
    queue.extend(graph[num])

    while queue:
        node = queue.popleft()

        if visited[node] == 0 :
            visited[node] = 1
            queue.extend(graph[node])
    return

# def dfs(num):
#     visited[num] = 1
#     for i in graph[num] :
#         if not visited[i]:
#             dfs(i)
#     return

count = 0

#For문 돌면서 아직 방문하지 않은 노드를 찾으면서 count + 1 해준다.
for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        count += 1

# count2 = 0
# for i in range(1,n+1):
#     if visited[i] == 0:
#         dfs(i)
#         count2 += 1


print(count)
#print(count2)


