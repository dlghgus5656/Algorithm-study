# 문제
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

# 작성해야 하는 함수는 다음과 같다.

# Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

# 설명
# 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 a가 주어집니다.
# 함수의 리턴값에는 a에 포함되있는 정수 n개의 합(정수)이 주어집니다.

# for문을 사용해서 값을 출력하는 방법
def solve(a):
    sum = 0
    for i in range(a):
        sum += i
    return sum


# python의 내장함수를 사용하는 방법


def solve(a):
    return sum(a)
