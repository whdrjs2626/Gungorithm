"""
문제 설명
머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 2022년 기준 선생님의 나이 age가 주어질 때, 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요

제한사항
0 < age ≤ 120
나이는 태어난 연도에 1살이며 매년 1월 1일마다 1살씩 증가합니다.
"""

def solution(age):
    answer = 2022 - age + 1
    return answer
