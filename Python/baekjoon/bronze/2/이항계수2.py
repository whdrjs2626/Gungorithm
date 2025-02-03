"""
문제
자연수
\(N\)과 정수
\(K\)가 주어졌을 때 이항 계수
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에
\(N\)과
\(K\)가 주어진다. (1 ≤
\(N\) ≤ 1,000, 0 ≤
\(K\) ≤
\(N\))

출력

\(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.
"""

import sys

N, K = map(int, sys.stdin.readline().split())

if N - K < K:
    K = N - K

bunja = 1
bunmo = 1
for i in range(1, K+1):
    bunja *= (N - i + 1)
    bunmo *= i

print((bunja // bunmo) % 10007)
