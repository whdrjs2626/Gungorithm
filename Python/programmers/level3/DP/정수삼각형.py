"""
문제 설명
         7
        3 8
       8 1 0
      2 7 4 4
     4 5 2 6 5

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
입출력 예
triangle	                                              result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	    30
"""


"""
DP - 앞에서 계산한 식을 배열에 미리 저장해 연산속도를 증가시킴 - 계산 한 것은 다시 하지 않는다.
1. 최적 부분 구조 - 큰 문제를 작은 문제로 나눠, 작은 문제의 답을 모아 큰 문제를 해결
2. 중복 부분 문제 - 부분 문제가 중첩됨 - 동일한 작은 문제를 반복적으로 해결

방식 2가지
1. Top-Down - 하향식, 메모이제이션, 위 > 아래
    한번 계산한 결과를 메모리 공간에 메모(메모이제이션)
    같은 문제를 다시 호출하면 메모한 결과를 가져옴 -> 캐싱
    재귀함수 사용
2. Bottom-Up - 상향식, 아래 > 위
    작은문제 + 작은문제 = 큰문제
    반복문 사용
"""


def solution(triangle):  # Bottom-Up 방식으로 풀이 / for문 내에 첫번째 인자, 마지막 인자냐에 따른 조건을 안두기 위해 배열 앞뒤로 [0]을 추가
    triangle = [[0] + t + [0] for t in triangle]
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
    return max(triangle[len(triangle) - 1])




def solution2(triangle):  # Top-Down 방식으로 풀이 / 맨 아래부터 차례대로 최대값을 구함
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer


def f(triangle, i, j, memo):
    if i == len(triangle) - 1:
        return triangle[i][j]

    if (i, j) in memo:
        return memo[(i, j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i, j)] = x
    return x
