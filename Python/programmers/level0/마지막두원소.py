"""
문제 설명

정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
  num_list.append(num_list[len(num_list) - 1] - num_list[len(num_list) - 2] if num_list[len(num_list) - 1] > num_list[len(num_list) - 2] else num_list[len(num_list) - 1] * 2)
  return num_list
