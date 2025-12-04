def solve(s: str, lb: int, ub: int, need: int):
    if need == 0:
        return ""
    
    ans = lb
    for i in range(lb + 1, ub + 1):
        if int(s[i]) > int(s[ans]):
            ans = i 
    
    need -= 1
    return s[ans] + solve(s, ans + 1, len(s) - need, need)

with open('test_input/d3.txt', 'r') as f:
    ans = 0
    for s in f:
        s = s[:-1]
        sol = int(solve(s, 0, len(s) - 12, 12))
        print(sol)
        ans += sol

    print(ans)

# s = "818181911112111"
# print(solve(s, 0, len(s) - 12, 12))