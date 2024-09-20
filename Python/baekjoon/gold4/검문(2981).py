"""
문제
트럭을 타고 이동하던 상근이는 경찰의 검문을 받게 되었다. 경찰은 상근이가 운반하던 화물을 하나하나 모두 확인할 것이기 때문에, 검문하는데 엄청나게 오랜 시간이 걸린다.

상근이는 시간을 때우기 위해서 수학 게임을 하기로 했다.

먼저 근처에 보이는 숫자 N개를 종이에 적는다. 그 다음, 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다. M은 1보다 커야 한다.

N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성하시오.
"""

import sys
from math import gcd

"""
N_list[0] = 공통나누는값 M * 몫[0] + 나머지 R
N_list[1] = M * 몫[1] + R
N_list[2] = M * 몫[2] + R
우리가 구할건 나머지 R이 같은 공통 M
아래 식에서 위 식을 빼게되면
(N_list[1] - N_list[0]) = M * (몫[1] - 몫[0])
(N_list[2] - N_list[1]) = M * (몫[2] - 몫[1])

즉 M은 (N_list[1] - N_list[0])와 (N_list[2] - N_list[1])의 공약수임
위 두 숫자의 최대공약수를 구한 후 그 최대 공약수의 1을 제외한 약수를 구하면 된다.
"""

N = int(sys.stdin.readline())
N_list = list(int(sys.stdin.readline()) for _ in range(N))
diff_list = [N_list[i] - N_list[i - 1] for i in range(1, N)]

gcd_num = diff_list[0]

for i in range(1, len(diff_list)):
    gcd_num = gcd(gcd_num, diff_list[i])

result = []
for i in range(2, int(gcd_num ** 0.5) + 1):
    """
    최대공약수 gcd_num의 약수를 구하는 방법을 효율적으로 만든 방법
    1. 최대공약수의 제곱근까지만 비교함
    2. 나눴을 때 0이 되는 값이 약수임 -> 몫도 약수인 셈이다. gcd_num = i * 몫 -> 몫도 한번에 추가 
    """
    if gcd_num % i == 0:
        result.append(i)
        result.append(gcd_num // i)

result.append(gcd_num)
print(' '.join(map(str, sorted(list(set(result))))))