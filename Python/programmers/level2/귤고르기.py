"""
문제 설명
경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
"""

"""
tangerine 리스트 내 숫자의 개수를 직접 구한 케이스 - collections 내 Counter 객체를 몰랐음
"""
def solution(k, tangerine):
    count = 0
    size = {}
    for i in tangerine:
        if size.get(i, -1) == -1:
            size[i] = 1
        else:
            size[i] += 1
    size = sorted(size.items(), key=lambda item: item[1], reverse=True)
    for i, row in enumerate(size):
        count += row[1]
        if count >= k:
            return i + 1


"""
tangerine 리스트 내 숫자의 개수를 Counter 객체로 구한 케이스
"""
def solution(k, tangerine):
    import collections
    tangerine_cnt = collections.Counter(tangerine)
    count = 0
    for i, v in enumerate(sorted(tangerine_cnt.values(), reverse=True)):
        count += v
        if count >= k:
            return i + 1
