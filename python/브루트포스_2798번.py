# 브루트 포스(brute force)
# brute: 무식한, force: 힘   무식한 힘으로 해석할 수 있다.

# 완전탐색 알고리즘. 즉, 가능한 모든 경우의 수를 모두 탐색하면서 요구조건에 충족되는 결과만을 가져온다.

# 이 알고리즘의 강력한 점은 예외 없이 100%의 확률로 정답만을 출력한다.

# 블랙잭

# 문제
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.

# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 예제 입력 1
# 5 21
# 5 6 7 8 9
# 예제 출력 1
# 21
# 예제 입력 2
# 10 500
# 93 181 245 214 315 36 185 138 216 295
# 예제 출력 2
# 497

# 삼중for문을 돌려 계산할 수 있는 값중에서 m을 넘지않는 가장 큰 값을 구해준다.
# 삼중인 이유는 카드 세 개를 뽑는다고 문제에서 제시했기 때문에 완전 탐색을 하기 위함이다.

# 인풋이 두 줄로 되어 있기 때문에 n,m을 첫째 줄에서 입력을 받고, cards로 둘째 줄에 입력을 받는다.
# result와 length를 초기화하고
# 3중 반복문으로 cards의 합을 sum_value에 저장한다.
# 반복문의 범위가 저렇게 되는 이유는 반복 추출이 없게 뽑히기 때문이다.
# 문제에서 M보다 세 개의 카드의 합이 작아야하는 조건이 있기 때문에 if문을 사용하고,
# result에 이들의 최대값을 저장하고 출력한다.
n, m = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))

result = 0
length = len(cards)


for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = cards[i]+cards[j]+cards[k]
            if sum_value <= m:
                result = max(result, sum_value)
print(result)


# (파이썬 itertools 라이브러리를 이용하면 간결하게 가능하다.)
# from itertools import permutations

# n, m = map(int, input().split())

# num = list(map(int, input().split()))
# permutationArray = permutations(num, 3)
# ans = 0
# for i in permutationArray:
#     if(m+1 > sum(i)):
#         ans = max(ans, sum(i))

# print(ans)
