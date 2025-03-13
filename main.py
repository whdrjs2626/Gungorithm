"""
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
"""
import math
def solution(n, w, num):
    div = math.ceil(n / w)
    cur = math.ceil(num / w)
    last = [i for i in range((div - 1) * w + 1, n + 1)]
    if div % 2 == 0:
        last.reverse()
        last = ([0] * (w - len(last))) + last
    else:
        last += [0] * (w - len(last))
    first = [i for i in range((cur - 1) * w + 1, cur * w + 1)]
    if cur % 2 == 0:
        first.reverse()
    return div - cur + 1 if last[first.index(num)] else div - cur



if __name__ == "__main__":
    result = solution(13,3,6)
    print(result)

