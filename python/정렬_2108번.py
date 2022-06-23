# 통계학

# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
# 단, N은 홀수라고 가정하자.

# 산술평균: N개의 수들의 합을 N으로 나눈 값
# 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값: N개의 수들 중 가장 많이 나타나는 값
# 범위: N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500, 000)이 주어진다. 단, N은 홀수이다.
# 그 다음 N개의 줄에는 정수들이 주어진다.
# 입력되는 정수의 절댓값은 4, 000을 넘지 않는다.

# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.

# 예제 입력 1
# 5
# 1
# 3
# 8
# -2
# 2
# 예제 출력 1
# 2
# 2
# 1
# 10
# 예제 입력 2
# 1
# 4000
# 예제 출력 2
# 4000
# 4000
# 4000
# 0
# 예제 입력 3
# 5
# -1
# -2
# -3
# -1
# -2
# 예제 출력 3
# -2
# -2
# -1
# 2
# 예제 입력 4
# 3
# 0
# 0
# -1
# 예제 출력 4
# 0
# 0
# 0
# 1

import sys

N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
# 정렬
arr = sorted(arr)
# 빈도수 배열
cnt_arr = {}
sum_arr = 0
for i in arr:
    sum_arr += i
    if i in cnt_arr:
        cnt_arr[i] += 1
    else:
        cnt_arr[i] = 1
avr = round(sum_arr / len(arr))
mid = arr[N//2]
rng = max(arr) - min(arr)
# 빈도수 배열의 빈도들 중 최대값 구하기
max_cnt = max(cnt_arr.values())
tmp = []
# 최빈값들의 key(최빈값에 해당하는 입력받은 숫자)를 tmp에 담기
for i in cnt_arr:
    if max_cnt == cnt_arr[i]:
        tmp.append(i)
# 최빈값 배열을 입력받은 숫자에 대해 오름차순 정렬
tmp = sorted(tmp)
# 최빈값이 1개이상이면, 두번째 값 출력
if len(tmp) > 1:
    mode = tmp[1]
# 최빈값이 1개이면 해당값 출력
else:
    mode = tmp[0]
# print(avr)
# print(mid)
# print(mode)
# print(rng)
print("산술평균 : " + str(avr))
print("중앙값 : " + str(mid))
print("최빈값 : " + str(mode))
print("최대 최소값 거리 : " + str(rng))
