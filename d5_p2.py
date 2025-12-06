ranges, ids = [], []

with open('test_input/d5.txt') as f:
    for line in f:
        if line.strip() == "":
            break
        ranges.append(list(map(int, line.strip().split('-'))))
    
ranges.sort()
new_ranges = [ranges[0]]
# Combining the overlapped ranges
for i in range(1, len(ranges)): 
    if ranges[i][0] <= new_ranges[-1][1]:
        new_ranges[-1][1] = max(ranges[i][1], new_ranges[-1][1])
    else:
        new_ranges.append(ranges[i])

ans = 0
for r in new_ranges:
    ans += r[1] - r[0] + 1

print(ans)