# BFS - 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘
# 큐 자료구조에 기초한다는 점

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],  # 1에 연결된 노드
    [1, 7],     # 2에 연결된 노드
    [1, 4, 5],  # 3
    [3, 5],     # 4
    [3, 4],     # 5
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)

# BFS - 큐 이용, 큐 자료구조 이용