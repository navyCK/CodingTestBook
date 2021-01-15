# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):       # i부터 0+1까지 1씩 감소
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)

# 삽입 정렬의 시간 복잡도 : 
# 리스트의 데이터가 거의 정렬되어 있는 상태라면
# 매우 빠르게 동작