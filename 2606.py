#-*- coding: utf-8 -*-

import sys
from collections import deque

read = sys.stdin.readline

com = int(input())
lines = int(input())

graph = [ []*(com + 1) for _ in range(com + 1) ]

for _ in range(lines):
    a,b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)


queue = deque()
queue.append(1)
visited = [0] * (com+1)
visited[1] = 1
cnt = 0
while queue :
    com = queue.popleft()

    if com != '' and com != 0 :
        for i in graph[com]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                cnt += 1

print(cnt)