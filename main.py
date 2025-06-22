def video_control(video_len, pos, op_start, op_end, type):
    total = int(video_len.split(':')[0]) * 60 + int(video_len.split(':')[1])
    cur = int(pos.split(':')[0]) * 60 + int(pos.split(':')[1])
    start = int(op_start.split(':')[0]) * 60 + int(op_start.split(':')[1])
    end = int(op_end.split(':')[0]) * 60 + int(op_end.split(':')[1])
    if type == "next":
        cur += 10
        cur = min(cur, total)
    else:
        cur -= 10
        cur = max(cur, 0)
    if cur < end and cur > start:
        cur = end
    print(str(cur // 60).zfill(2) + ":" + str(cur % 60).zfill(2))
    return str(cur // 60).zfill(2) + ":" + str(cur % 60).zfill(2)

def solution(video_len, pos, op_start, op_end, commands):
    for com in commands:
        pos = video_control(video_len, pos, op_start, op_end, com)
    return pos

result = solution("10:55",	"00:05",	"00:15",	"06:55",	["prev", "next", "next"])

print(result)