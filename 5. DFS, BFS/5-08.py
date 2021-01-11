# DFS 예제

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)

# DFS - 스택 원리, 재귀 함수 이용