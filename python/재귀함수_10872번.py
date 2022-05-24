# 팩토리얼

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# 예제 입력 1
# 10
# 예제 출력 1
# 3628800
# 예제 입력 2
# 0
# 예제 출력 2
# 1


# for문 코드
import math
b = int(input())
result = 1
if b > 0:
    for i in range(1, b+1):
        result *= i
print(result)

# 재귀 함수 코드

# 자기 자신을 불러오며 결과적으로 n = 5일 경우
# result는 5 * 4 * 3 * 2 * 1 의 식이 완성되고 그 값을 리턴해 출력된다.


def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n - 1)
    return result


n = int(input())
print(factorial(n))

# math라이브러리를 사용
a = int(input())
print(math.factorial(a))
