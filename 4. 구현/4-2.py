h = int(input())
count = 0

for i in range(h + 1):                                  # 시간
    for j in range(60):                                 # 분
        for k in range(60):                             # 초
            if '3' in str(i) + str(j) + str(k):         # '3'이 포함되어 있다면 
                count += 1                              # 카운트 증가
                
print(count)