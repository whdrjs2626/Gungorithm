
def solution(citations):
    return sorted(citations)[len(citations)//2]

if __name__ == "__main__":
    result = solution([3, 0, 6, 1, 5])
    print(result)

