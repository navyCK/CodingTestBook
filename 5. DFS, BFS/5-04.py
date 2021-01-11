def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

# 재귀 함수의 수행은 스택 자료구조를 이용
# 스택 자료구조 활용 알고리즘은 재귀 함수를 이용하여 간편하게 구현
# DFS가 대표적인 예