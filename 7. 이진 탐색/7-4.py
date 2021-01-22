# 한 줄 입력받아 빠르게 출력
# 데이터 개수가 많아 input() 동작 속도가 느려질 때
# sys 라이브러리를 사용

import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)