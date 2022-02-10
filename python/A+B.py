# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# split 함수는 / 한 문자열을 / 나누어 / 리스트로 구분해 준다.

# A, B = input().split()
# x = int(A)
# y = int(B)

# print(x+y)

# map의 기본형은 map(적용할 함수, 반복 가능한 자료형)이다. map함수를 활용하면, 한 줄의 코딩으로 모든 자료형 각각에 함수를 적용할 수 있다.

A, B = map(int, input("입력: ").split())
print(A+B)
