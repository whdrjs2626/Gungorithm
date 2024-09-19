"""
문제 설명
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
"""

def solution(people, limit):
    from collections import deque
    """
    deque를 사용한 이유
    
    원래 리스트를 그냥 정렬하여 pop(0)을 통해 최소값을 가져오려 했으나
    pop(0)은 데이터를 지우고 한칸씩 앞으로 당기기 때문에 O(1)이 아닌 O(N)가 소요되어 시간초과가 발생함
    
    따라서 리스트를 deque로 변환하여
    popleft()를 사용하게되면 O(1)이 소요되기 때문에 시간 초과가 나지 않음
    """
    people = deque(sorted(people))
    count = 0
    while people:
        max = people.pop()
        if not people:
            count += 1
            break
        min = people.popleft()
        if max + min > limit:
            people.appendleft(min)
        count += 1
    return count



"""
피벗(left, right)을 사용한 방법

해당 방법 또한 피벗을 사용하여 인덱스로 접근하기 때문에 O(1)로 원하는 최소값, 최대값에 접근이 가능함
"""

def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    count = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        count += 1
    return count
