"""
문제 설명
정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.

제한사항
5 ≤ num_list의 길이 ≤ 50
-9 ≤ num_list의 원소 ≤ 9
"""

def solution(num_list):
    odd_sum, even_sum = 0, 0
    for i in range(1, len(num_list) + 1):
        if i % 2 == 0:
            even_sum += num_list[i - 1]
        else:
            odd_sum += num_list[i - 1]
    return max(even_sum, odd_sum)
