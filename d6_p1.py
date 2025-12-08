s = []

with open('test_input/d6.txt') as f:
    for line in f:
        s.append(line.strip().split())


n = len(s) - 1
def solve(symbol: str, col: int) -> int:
    ans = 0
    if symbol == "+":
        for i in range(n):
            ans += int(s[i][col])
    else:
        ans = 1
        for i in range(n):
            ans *= int(s[i][col])
    return ans 

ans = 0
for col in range(len(s[0])):
   ans += solve(s[-1][col], col)

print(ans)