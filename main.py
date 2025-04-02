"""
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
"""
import math
def solution(a, b):
    if (a + b) % 2 == 0:
        if a % 2 == 0 and b % 2 == 0:
            return abs(a - b)
        else:
            return a**2 + b**2
    else:
        return 2 * (a + b)



if __name__ == "__main__":
    result = solution(3, 5)
    print(result)

