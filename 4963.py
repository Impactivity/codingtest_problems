import sys
from collections import deque


dx = [ 0, 0, -1, 1 , -1, -1, 1, 1]
dy = [ -1, 1, 0 ,0, -1, 1, 1 ,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        a,b = queue.popleft()
        graph[a][b] == 0

        #상하좌우, 대각선 좌상,좌하,우상,우하 4개 포함 총 8개
        #이동
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx > h-1 or ny < 0 or ny > w-1 :
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return

read = sys.stdin.readline
while 1:

    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, read().split())) for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)


