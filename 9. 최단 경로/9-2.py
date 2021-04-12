# 방법 2. 개선된 다익스트라 알고리즘
# 시간 복잡도 : O(ElogV)
# 힙(Heap) 자료구조 사용 - 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리 => 
# 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

# 우선순위 큐 - 우선순위가 가장 높은 데이터를 가장 먼저 삭제
# 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용한다고 보자.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 이 코드를 바로 이해하기엔 어렵지만, 다익스트라 최단 경로 알고리즘의 소스 코드만 잘 기억해보자.