"""
문제 설명
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(quiz):
    result = []
    for q in quiz:
        tmp = q.split(' ')
        s = ''.join(tmp[0:3])
        result.append('O' if str(eval(s)) == tmp[4] else 'X')
    return result