"""
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
"""

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        l1 = []
        for j in range(len(arr2[0])):
            a = 0
            for k in range(len(arr2)):
                a += arr1[i][k] * arr2[k][j]
            l1.append(a)
        answer.append(l1)
    return answer
