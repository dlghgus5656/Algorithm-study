# 문제
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

# for 변수 in reversed(range(시작, 끝, 증가폭))
import sys

N = int(input())
y = int(sys.stdin.readline())

# 1번째 방법
for i in range(N, 0, -1):
    print(i)
# 2번째 방법
for i in range(y, 0, -1):
    print(i)
