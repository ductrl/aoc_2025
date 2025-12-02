import math 

def detect_cycle(s: str) -> bool:
    return (s + s).index(s, 1) < len(s)

def solve(lb: int, ub: int) -> int:
    ans = 0
    for x in range(lb, ub + 1):
        if detect_cycle(str(x)):
            ans += x 
    
    return ans

# idk really how to do this except for brute forcing it
ans = 0
with open('aoc_2025/test_input/d2.txt', 'r', encoding='utf-8') as f:
    data = f.read()

test = data.split(',')

for t in test:
    lb, ub = map(int, t.split('-'))
    ans += solve(lb, ub)

print(ans)