# 백준 1008번 문제 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

# 1번째 방법
A, B = input().split()
print(int(A)/int(B))
# 2번째 방법
A, B = map(int, input().split())
print(A/B)
