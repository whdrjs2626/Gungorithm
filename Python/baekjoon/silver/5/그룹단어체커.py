"""
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
"""

import sys

def zero(a): # 알파벳 배열 초기화 함수
    for i in range(len(a)):
        a[i] = 0

num = int(sys.stdin.readline())

alphabet = [] # 알파벳 개수 배열
count = 0 # 그룹 단어 개수

for i in range(26): # 알파벳 개수 초기화
    alphabet.append(0)

for i in range(num): # 입력받은 횟수만큼 반복
    str = sys.stdin.readline().rstrip() # 단어입력
    flag = True # 그룹 단어 여부
    zero(alphabet)
    for j in range(0, len(str)): # 단어 한 글자씩 반복
        if j == 0:
            pass
        elif alphabet[ord(str[j])-97] != 0 and str[j-1] != str[j]: # 알파벳의 개수가 0이 아님(이미 나왔던 알파벳) and 현재 알파벳 이전 알파벳과 다른 알파벳인 경우 그룹단어가 아님
            flag = False
            break
        alphabet[ord(str[j]) - 97] += 1 # 현재 알파벳의 개수 1증가
    if flag:
        count += 1

print(count)
