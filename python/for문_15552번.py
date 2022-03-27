# 문제
# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

# 출력
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

# 💡 sys.stdin.readline() 사용법
# 📌한 개의 정수를 입력받을 때
# import sys
# a = int(sys.stdin.readline())
# 😨 그냥 a = sys.stdin.readline() 하면 안되나요?
# 👉 sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
# 만약 3을 입력했다면, 3\n 이 저장되기 때문에, 개행문자를 제거해야 합니다.
# 또한, 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.

# map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수입니다.


import sys

T = int(input())  # Test case

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
