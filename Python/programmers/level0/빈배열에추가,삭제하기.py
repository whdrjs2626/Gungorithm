"""
문제 설명
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고, flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ arr의 길이 = flag의 길이 ≤ 100
arr의 모든 원소는 1 이상 9 이하의 정수입니다.
현재 X의 길이보다 더 많은 원소를 빼는 입력은 주어지지 않습니다.
"""

def solution(arr, flag):
    result = []
    for n, f in zip(arr, flag):
        if f:
            result.extend([n] * n * 2)
        else:
            result = result[:-n]
    return result
