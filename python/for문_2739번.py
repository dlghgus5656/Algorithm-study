# 문제
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.
# 출력 형식에 맞춰서 출력하면 된다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

# 출력
# 출력형식과 같게 N*1부터 N*9까지 출력한다.

N = int(input())

for i in range(1, 10):  # 1~9
    if N >= 1 and N <= 9:
        print(N, '*', i, '=', N*i)
    else:
        print("1보다 크거나 같고, 9보다 작거나 같아야합니다.")

# Num = int(input())
# 1<=Num<=9

# for i in range(1,10):
#     result = Num* i
#     print( Num,'*',i ,'=',result)

# N=int(input())
# for i in range(1,10):
#     print("%d * %d = %d" %(N, i, N*i))
