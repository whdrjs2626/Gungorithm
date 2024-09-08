"""
문제 설명
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.
"""

# 최대공약수를 직접 구한 버전
def lcm(a, b):
    while b:
        r = a % b
        a, b = b, r
    return a

def solution(arr):
    a = arr[0]
    for num in arr[1:]:
        b = num
        a = a * b // lcm(a, b)
    return a


# gcd함수를 사용하여 최소공배수를 바로 구한 버전
def solution(arr):
    from math import gcd
    answer = arr[0]

    for num in arr:
        answer = answer * num // gcd(answer, num)

    return answer
