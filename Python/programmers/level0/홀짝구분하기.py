"""
문제 설명
자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
"""

a = int(input())
print('{0} is even'.format(str(a)) if a % 2 == 0 else '{0} is odd'.format(str(a)))
