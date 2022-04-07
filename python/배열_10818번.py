# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
# 예제 입력
# 5
# 20 10 35 30 7
# 예제 출력
# 7 35

# 풀이 1. max, min 함수 사용
N = int(input())
# 입력을 공백으로 구별해서 나누고 map로 정수형으로 각각 변환해주고 이를 list()를 통해 리스트(배열) 형태로 변환
array = list(map(int, input().split()))
print(min(array), max(array))

# 풀이 2. sort(정렬) 사용
N = int(input())
array = list(map(int, input().split()))
array.sort()  # sort() 함수를 사용해 오름차순으로 정렬한다.
print(array[0], array[-1])  # 첫번째가 최솟값 마지막이 최댓값이므로 [0]과 [-1] 을 출력해준다.
