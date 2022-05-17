def sosu(x):
    if x == 1:  # 1은 모든 수의 약수이기 때문에 pass
        return False
    for i in range(2, int(x**0.5)+1):  # 제곱근이 있는 수 중에
        if x % i == 0:  # 약수가 있으면 false
            return False
    return True  # 이외에는 소수


all_list = list(range(2, 246912))  # 문제에서 제한한 범위
memo = []  # for문 밖에 리스트 정의

for i in all_list:  # 2부터 2*123,456 범위
    if sosu(i):  # sosu함수에 해당하면
        memo.append(i)  # 리스트에 추가

n = int(input())  # 범위를 주기 위한 입력


while True:
    count = 0
    if n == 0:  # 0 입력하면 아웃되는 게 조건
        break
    for i in memo:  # memo리스트 중에서
        if n < i <= 2*n:  # 입력한 값의 범위 내에서 값이 있으면
            count += 1  # 있을 때 마다 카운트 +1
    print(count)  # 개수를 출력하는 조건에 맞춰 카운트를 출력
    n = int(input())
