n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:          # 입력값 R R R U D D 하나씩 확인
    for i in range(len(move_types)):    # L R U D 중 하나 판단
        if plan == move_types[i]:       # 입력값이 move_types와 일치하면
            nx = x + dx[i]              # 기존 x 좌표 + 입력값
            ny = y + dy[i]              # 기존 y 좌표 + 입력값
        
    if nx < 1 or ny < 1 or nx > n or ny > n:
            continue            # 범위 초과시 무시

    x, y = nx, ny

print(x, y)