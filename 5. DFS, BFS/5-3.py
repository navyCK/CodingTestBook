# 재귀 함수 - 자기 자신을 다시 호출하는 함수

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# print를 무한히 실행하는데, 재귀의 최대 깊이를 초과하면 종료한다.
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 마치 뫼비우스의 띠...