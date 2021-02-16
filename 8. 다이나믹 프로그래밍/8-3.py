# 호출되는 함수 확인

d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]

pibo(6)

# 이처럼 재귀 함수를 이용해 다이나믹 프로그래밍 소스코드를
# 작성하는 방법을 탑다운 방식이라고 한다.

# 단순히 반복문을 이용하여 소스코드를 작성하는 경우는
# 보텀업 방식이라고 한다.