"""
문제 설명
정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
"""

def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0
