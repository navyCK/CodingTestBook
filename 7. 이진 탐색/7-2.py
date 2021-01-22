# 이진 탐색 : 반으로 쪼개면서 탐색하기

# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

# 시간 복잡도 - O(logN)
# 퀵 정렬과 비슷

# 재귀 함수로 구현한 이진 탐색

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)