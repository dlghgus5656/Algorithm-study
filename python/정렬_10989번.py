# 수 정렬하기 3

# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
# 예제 출력 1
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7


# import sys

# N = int(sys.stdin.readline())
# nums = []
# result = [0 for _ in range(10001)]

# for i in range(N):
#     num = int(sys.stdin.readline())
#     result[num] += 1

# for i in range(len(result)):
#     for j in range(result[i]):
#         print(i)

import sys
input = sys.stdin.readline
num = int(input())
arr = [0]*10000

for i in range(num):
    a = int(input())
    arr[a-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)

# 계수정렬

# 입력으로 받을 수 있는 10,000개의 수를 담을 수 있는 배열을 만들고,

# 입력받을 때 마다 그 수에 해당하는 인덱스에 +1을 해줘서 값으로 그 수의 개수를 담는다.

# 그리고 다시 배열을 돌면서 값이 0이 아니라면 값만큼 인덱스에 해당하는 숫자를 출력하는 방식

# ? 메모리제한이 작을 때 사용할 수 있는 정렬인 계수정렬과

# ? 시간초과가 발생할 때 사용할 수 있는 파이썬 라이브러리 sys
