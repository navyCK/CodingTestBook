# key 값을 이용한 정렬

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

# 정렬 알고리즘이 사용되는 경우 3가지

# 1. 정렬 라이브러리로 풀 수 있는 문제 
# 2. 정렬 알고리즘의 원리에 대해 물어보는 문제
# 3. 더 빠른 정렬이 필요한 문제