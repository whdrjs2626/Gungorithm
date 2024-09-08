# def solution(n):
#     answer = 0
#     for i in range(1, n + 1):
#         sum = 0
#         for j in range(i, n + 1):
#             sum += j
#             if sum == n:
#                 answer += 1
#     return answer

if __name__ == "__main__":
    n = 15
    answer = 0
    for i in range(1, n + 1):
        sum = 0
        j = i
        while sum < n:
            sum += j
            j += 1
            if sum > n:
                continue
            elif sum == n:
                answer += 1


    print(result)