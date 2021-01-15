# 계수 정렬 - 특정한 조건이 부합할 때만 사용 가능하지만
# 매우 빠른 정렬 알고리즘

# 수행 시간 - O(N + K)

# 비교 기반 정렬 알고리즘

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 7, 1, 1, 3, 2, 1]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')


# 공간 복잡도 : 심각한 비효율성 초래할 수 있다.
# 데이터의 특성을 파악하기 어렵다면 퀵 정렬을 사용하는 것이 좋다.