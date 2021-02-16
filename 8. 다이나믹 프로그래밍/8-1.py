# 피보나치 함수를 재귀 함수로 구현

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 이렇게 작성한다면 x가 커질수록 수행 시간이 기하급수적으로 늘어나기
# 때문에 올바른 방법이 될 수 없다.