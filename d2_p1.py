import math 

# for range abcd - xyzkt: go from ab to xyz
def num_length(x: int) -> int:
    if x == 0:
        return 1
    return int(math.log10(x)) + 1

def half_the_number(x: int) -> int:
    half_length = num_length(x) // 2
    return x // 10**half_length

def double_the_number(x: int) -> int:
    return int(str(x) * 2)

def solve(lb: int, ub: int) -> int: # lb and ub stand for lowerbound and upperbound
    ans = 0
    if lb > ub:
        return 0
    
    if num_length(lb) % 2 == 1:
        lb = 10**num_length(lb)
    
    if num_length(ub) % 2 == 1:
        ub = 10**(num_length(ub) - 1) - 1
    
    start, end = half_the_number(lb), half_the_number(ub)

    for x in range(start, end + 1):
        num = double_the_number(x)
        if lb <= num <= ub:
            ans += num
    
    return ans 

# NOW WE'RE ACTUALLY SOLVING THE THING
ans = 0
with open('aoc_2025/test_input/d2.txt', 'r', encoding='utf-8') as f:
    data = f.read()

test = data.split(',')

for t in test:
    lb, ub = map(int, t.split('-'))
    ans += solve(lb, ub)

print(ans)