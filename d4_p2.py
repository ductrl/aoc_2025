s = []

with open('test_input/d4.txt') as f:
    for line in f:
        s.append(list(line.strip()))

def solve() -> int:
    m, n = len(s), len(s[0])
    moves = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]] # move clockwise

    def check_inbound(x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < m and y < n 

    def check_access(x: int, y: int) -> bool:
        cnt = 0
        for m in moves:
            new_x = x + m[0]
            new_y = y + m[1]
            
            if check_inbound(new_x, new_y):
                cnt += int(s[new_x][new_y] == '@')
        return cnt < 4

    ans = 0 
    for x in range(m):
        for y in range(n):
            if s[x][y] == '@':
                if check_access(x, y):
                    ans += 1
                    s[x][y] = '.'

    return ans 

ans = 0
cur_sol = 1
while cur_sol > 0:
    cur_sol = solve()
    ans += cur_sol

print(ans)
# lucky for me this doesn't take 2 years to run