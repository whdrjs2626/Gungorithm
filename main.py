"""
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
"""
def solution(num):
    if num == 1: return 0
    count = 0
    while True:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        count += 1
        if count > 500:
            return -1
        elif num == 1:
            return count



if __name__ == "__main__":
    result = solution(1)
    print(result)

