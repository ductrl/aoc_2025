def solve(s: str):
    ans = 0
    max_num = int(s[-1])

    for i in range(len(s) - 2, -1, -1):
        num = int(s[i]) * 10 + max_num
        ans = max(ans, num)
        max_num = max(max_num, int(s[i]))
    
    return ans

ans = 0

with open('test_input/d3.txt', 'r') as f:
    for s in f:
        ans += solve(s[:-1])

print(ans)