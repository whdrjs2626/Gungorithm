"""
문제 설명
정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 < num < 1,000,000
0 ≤ k < 10
num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.
"""

def solution(num, k):
    num_list = list(str(num))
    flag = 0
    for i in range(0, len(num_list)):
        if k == int(num_list[i]):
            answer = i + 1
            flag = 1
            break
    if not flag:
        answer = -1
    return answer
