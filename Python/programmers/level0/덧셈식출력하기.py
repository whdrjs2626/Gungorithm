"""
문제 설명
두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

a + b = c
제한사항
1 ≤ a, b ≤ 100
"""

a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')
