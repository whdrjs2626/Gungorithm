def solution(arr, intervals):
  s1, e1 = intervals[0]
  s2, e2 = intervals[1]
  return arr[s1:e1+1] + arr[s2:e2+1]