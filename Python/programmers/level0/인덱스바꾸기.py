"""
문제 설명
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(my_string, num1, num2):
    list_string = list(my_string)
    tmp = list_string[num1]
    list_string[num1] = list_string[num2]
    list_string[num2] = tmp
    answer = ''.join(list_string)
    return answer
    return answer
