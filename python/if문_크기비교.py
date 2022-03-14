# 백준 1330번 문제

# A = int(input())
# B = int(input())
A, B = map(int, input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
