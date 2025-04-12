
def solution(numbers):
    n_list = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    sum = 0
    for n in numbers:
        n_list[n] += 1

    for n_key in n_list.keys():
        if n_list[n_key] == 0:
            sum += n_key
    return sum



result = solution([1,2,3,4,5,6,7,8,0])

print(result)