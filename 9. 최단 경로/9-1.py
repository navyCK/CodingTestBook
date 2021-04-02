# 방법 1. 간단한 다익스트라 알고리즘
# 시간 복잡도 : O(V제곱)
# 단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해
# 매 단계마다 1차원 리스트의 모든 원소를 순차 탐색

# 솔직히 이해가 안된다...

import sys
input = sys.stdin.readline     # input을 좀 더 빠르게
INF = int(1e9)                  # 무한 의미로 10억 설정

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])