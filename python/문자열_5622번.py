# 다이얼
# 문제
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.

# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

# 예제 입력 1
# WA
# 예제 출력 1
# 13
# 예제 입력 2
# UNUCIC
# 예제 출력 2
# 36


# 다이얼 배열 선언
arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# 문자열 입력
str = input()
# 시간 초기화
time = 0
# 해당 문자 길이 만큼 반복
for j in range(len(str)):
    # 배열에 해당하는 문자 찾기 위해 배열 반복
    for i in arr:
        # 배열 요소 안에 해당 문자 포함시
        if str[j] in i:
            # 찾은 인덱스 + 3 (인덱스는 0부터 시작)
            time += arr.index(i)+3
# 계산한 걸린 시간 출력
print(time)

# num = input()
# time = 0
# for i in num:
#     if i in ['A', 'B', 'C']:
#         time += 3
#     elif i in ['D', 'E', 'F']:
#         time += 4
#     elif i in ['G', 'H', 'I']:
#         time += 5
#     elif i in ['J', 'K', 'L']:
#         time += 6
#     elif i in ['M', 'N', 'O']:
#         time += 7
#     elif i in ['P', 'Q', 'R', 'S']:
#         time += 8
#     elif i in ['T', 'U', 'V']:
#         time += 9
#     elif i in ['W', 'X', 'Y', 'Z']:
#         time += 10
# print(time)
