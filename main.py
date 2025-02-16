"""
1 1 0
1 1 0
0 0 1

1 1 0
1 1 1
0 1 1
"""

def solution2(n, computers):
    answer = 0
    visited = [False for _ in range(n)]     # 방문 여부 저장 배열

    for com in range(n):
        if visited[com] == False:   # 1번 ~ n번 컴퓨터까지 가면서 방문하지 않은 컴퓨터라면
            DFS(n, computers, com, visited)
            answer += 1
    return answer


def DFS(n, computers, com, visited):
    visited[com] = True        # 해당 노드의 방문 여부를 True로 변경
    for i in range(n):          # 해당 노드와 연결된 다음 노드들을 모두 탐색
        if i != com and computers[i][com] == 1 and visited[i] == False:
                DFS(n, computers, i, visited)       # i랑 연결된 다음 노드도 쭉 탐색

# 자기 자신이 아니고, 이전 노드(com)와 현재 노드(i)가 연결된 노드이며, 현재 노드가 방문하지 않은 노드라면 방문하고, 현재 노드(i)에 대한 DFS를 계속 진행
# 연결되지 않은 노드가 나오는 순간 DFS 종료


from collections import deque


def solution1(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1

    return answer


def BFS(n, computers, com, visited):
    visited[com] = True  # 방문을 했으므로 방문여부를 참으로 변경
    queue = deque()
    queue.append(com)

    while len(queue) > 0:  # 큐에 요소가 남아있는 동안 계속 append, pop 작업을 진행
        com = queue.pop()
        visited[com] = True

        for i in range(n):
            if visited[i] == False and computers[i][com] == 1 and i != com:
                queue.append(i)


from collections import deque


def solution3(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1

    return answer


def BFS(n, computers, com, visited):
    visited[com] = True  # 방문을 했으므로 방문여부를 참으로 변경
    queue = deque()
    queue.append(com)

    for i in range(n):
        if visited[i] == False and computers[i][com] == 1 and i != com:
            BFS(n, computers, i, visited)

"""
def fibo(n):
    if n in (0, 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
def solution(n):
    return fibo(n) % 1234567
# """
# """
# def solution(arr1, arr2):
#     answer = []
#     for i, row in enumerate(arr1):
#         tmp = []
#         for j, num2 in enumerate(row):
#             tmp.append(num2 * arr2[j][i])
#         answer.append(tmp)
#
#     return answer
#
#
# # 2 3 2   5 4 3
# # 4 2 4   2 4 1
# # 3 1 4   3 1 1
# if __name__ == "__main__":
#     arr1 = [[1, 4], [3, 2], [4, 1]]
#     arr2 = [[3, 3], [3, 3]]
#     print(solution(arr1, arr2))
# """

import math
def solution(numer1, denom1, numer2, denom2):
    return list(map(lambda a: a // math.gcd(denom1 * numer2 + denom2 * numer1, denom1 * denom2), [denom1 * numer2 + denom2 * numer1, denom1 * denom2]))

# 2 3 2   5 4 3
# 4 2 4   2 4 1
# 3 1 4   3 1 1
if __name__ == "__main__":
    result = solution(1,2,3,4)
    print(result)


