"""
문제 설명
정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

제한사항
6 ≤ num_list의 길이 ≤ 30
1 ≤ num_list의 원소 ≤ 100
"""

def solution(num_list):
    return sorted(num_list)[5:]
