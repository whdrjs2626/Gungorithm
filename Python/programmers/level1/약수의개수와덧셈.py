"""
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
"""

def solution(left, right):
    sum = 0
    for n in range(left, right + 1):
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            sum += n
        else:
            sum -= n
    return sum
