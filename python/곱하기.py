# 백준 2588번 문제

# 1. 문자열을 이용한 풀이(반복문X)
A = int(input())
B = input()  # int를 안쓰고 문자열 형태로 남겨둔 이유는 문자열에 접근해야 하기 때문이다.

print(A*int(B[2]))  # B의 세 번째 자리 즉 일의 자리

print(A*int(B[1]))  # 십의 자리

print(A*int(B[0]))  # 백의 자리

print(A*int(B))


# 2. 문자열을 이용한 풀이(반복문O)
A = int(input())
B = input()

for i in range(3, 0, -1):  # 위의 프린트문들을 반복문으로 바꾼것
    print(A * int(B[i - 1]))

print(A * int(B))

# 3. 산술 연산자를 이용한 풀이
A = int(input())
B = int(input())

print(A * (B % 10))  # 385를 10으로 나눈 나머지는 5 즉 일의 자리

print(A * (B % 100 // 10))  # 385를 100으로 나눈 나머지는 85 그리고 다시 10으로 나눈 몫은 8 즉 십의 자리

print(A * (B // 100))  # 385를 100으로 나눈 몫은 3 즉 백의 자리

print(A * B)
