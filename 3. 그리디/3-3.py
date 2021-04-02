n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))  # 7 3 1 8
    min_value = min(data)                   # 1
    result = max(result, min_value)         # 둘 중 최대값

print(result)