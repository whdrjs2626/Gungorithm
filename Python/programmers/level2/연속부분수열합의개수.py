"""
문제 설명
철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.
원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ elements의 길이 ≤ 1,000
1 ≤ elements의 원소 ≤ 1,000
"""

def solution(elements):
    length = len(elements)
    result = elements.copy()
    elements += elements[:-1]

    for i in range(2, length + 1):
        for j in range(0, length):
            result.append(sum(elements[j:j + i]))
    return len(set(result))

"""
처음엔 위와 같이 풀어서 통과는 했으나 소요시간이 상당히 오래걸림
시간복잡도를 줄여보고자 수정한 부분이 아래 함수

차이점 이라면 기존에 연속된 숫자를 가져오기 위해 리스트 슬라이싱을 사용하였음 -> elements[j:j + i]
리스트 슬라이싱은 조회하는 객체의 개수만큼의 시간복잡도가 소요되어 단일 객체만 가져오는 방식으로 수정하였음
"""

def solution(elements):
    length = len(elements)
    result = set(elements.copy())

    for i in range(length):
        sum = elements[i]
        for j in range(i+1, length+i):
            sum += elements[j % length]
            result.add(sum)
    return len(result)
