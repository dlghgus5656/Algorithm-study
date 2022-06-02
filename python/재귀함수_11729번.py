# 하노이 탑 이동 순서

# 문제
# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

# 아래 그림은 원판이 5개인 경우의 예시이다.


# 입력
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

# 출력
# 첫째 줄에 옮긴 횟수 K를 출력한다.

# 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

# 예제 입력 1
# 3
# 예제 출력 1
# 7
# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3

# 풀이 전략
# n개의 원판을 A에서 C로 이동시키는 과정을 생각해보면 최종적으로
# n-1개의 원판을 B에 놓고,
# 남은 하나의 원판을 A에서 C로 옮긴 후 B의 원판들을 C에 옮기면 된다.

n = int(input())


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)


count = 0

for _ in range(n):
    count = 2*count + 1

print(count)
hanoi(n, 1, 2, 3)

# hanoi 함수를 보면 재귀 호출을 할 때 인자의 순서가 다른 것을 볼 수 있는데,
#  원래 인자 순서대로 설명하면 a는 현재 n개의 원판이 쌓여있는 곳, b는 n-1개의 원판을 옮겨 놓을 곳,
# C는 a에서 남은 원판을 놓을 곳이 된다.
# 풀이 전략에서의 동작을 함수로써 작성하여 해결한 것
