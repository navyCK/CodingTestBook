# 피보나치 수열
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


# 한 번 푼 문제는 그 결과를 저장해 놓았다가
# 나중에 동일한 문제를 풀어야 할 때 이미 저장한 값을 반환한다.
