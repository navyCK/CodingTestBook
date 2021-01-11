# 인접 리스트 방식 예제

graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)


# 인접 리스트 방식은 연결된 정보만 저장하기 때문에
# 메모리를 효율적으로 사용한다.
# 하지만 이 속성 때문에 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.
