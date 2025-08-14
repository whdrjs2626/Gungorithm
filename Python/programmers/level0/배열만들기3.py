def solution(arr, intervals):
  s1, e1 = intervals[0]
  s2, e2 = intervals[1]
  return arr[s1:e1+1] + arr[s2:e2+1]


import itertools
def solution2(arr, intervals):
    return list(itertools.chain.from_iterable([arr[inter[0]:inter[1]+1] for inter in intervals]))

