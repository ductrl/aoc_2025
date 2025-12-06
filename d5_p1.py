ranges, ids = [], []

with open('test_input/d5.txt') as f:
    current = ranges

    for line in f:
        line = line.strip()
        if line == "":
            current = ids 
            continue 
        current.append(list(map(int, line.split('-'))))
        if len(current[-1]) < 2:
            current[-1] = current[-1][0]
    
ranges.sort()
new_ranges = [ranges[0]]
# Combining the overlapped ranges
for i in range(1, len(ranges)): 
    if ranges[i][0] <= new_ranges[-1][1]:
        new_ranges[-1][1] = max(ranges[i][1], new_ranges[-1][1])
    else:
        new_ranges.append(ranges[i])

ranges = new_ranges
# Find the index of the last range with range[0] <= target
def binary_search(target: int) -> int:
    l, r = 0, len(ranges) - 1
    ans = -1
    
    while l <= r:
        m = (l + r) // 2
        if ranges[m][0] <= target:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans

def solve(id: int) -> bool:
    index = binary_search(id)
    return (index != -1 and ranges[index][1] >= id)

ans = 0
for id in ids:
    ans += int(solve(id))

print(ans)