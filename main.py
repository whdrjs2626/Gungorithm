"""
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
"""
import math
def solution(n, w, num):
    # li = []
    # tmp = []
    # flag = 1
    # for i in range(1, n + 1):
    #     tmp.append(i)
    #     if i % w == 0:
    #         if flag % 2 == 0:
    #             tmp.reverse()
    #         li.append(tmp)
    #         tmp = []
    #         flag += 1
    # li.append(tmp)
    # li.reverse()
    div = math.ceil(n / w)
    cur = num // w
    last = [i for i in range((div - 1) * w + 1, n + 1)]
    if div % 2 == 0:
        last.reverse()
    else:
        a = 1
    return div - cur



if __name__ == "__main__":
    result = solution(22, 6, 8)
    print(result)

