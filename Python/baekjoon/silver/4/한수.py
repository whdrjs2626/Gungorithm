"""
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""

import sys
n = int(sys.stdin.readline())

def han(a):
    c = a//1000
    b = (a-c*1000)//100
    s = (a-c*1000-b*100)//10
    i = (a-c*1000-b*100-s*10)%10
    if c == 0:
        if b == 0:
            return 1
        else:
            if b-s == s-i:
                return 1
    else:
        if c-b == b-s and b-s == s-i:
            return 1
    return 0
sum = 0
for i in range(n):
    sum += han(i+1)
print(sum)
