"""
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
"""
import sys

x_dict = {}
y_dict = {}

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())

    if x_dict.get(x, '') == '':
        x_dict[x] = 1
    else:
        x_dict[x] += 1

    if y_dict.get(y, '') == '':
        y_dict[y] = 1
    else:
        y_dict[y] += 1

for key in x_dict:
    if x_dict[key] == 1:
        print(key, end=' ')

for key in y_dict:
    if y_dict[key] == 1:
        print(key)
