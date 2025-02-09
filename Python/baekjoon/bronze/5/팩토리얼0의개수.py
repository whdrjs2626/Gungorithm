"""
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
"""

import sys
T = int(sys.stdin.readline())

facto = 1

for i in range(2, T + 1):
    facto *= i

result = str(facto)

flag = False
count = 0
if result[len(result) - 1] == '0':
    flag = True
    count = 1

for i in range(len(result) - 2, -1, -1):
    if result[i] == '0' and flag:
        count += 1
    else:
        break
print(count)
