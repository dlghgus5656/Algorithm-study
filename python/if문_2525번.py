A, B = map(int, input().split())
C = int(input())

if (C + B) // 60:
    A += (C + B) // 60
    B = (C + B) % 60
else:
    B += C

while A > 23:
    A %= 24

print(A, B)
