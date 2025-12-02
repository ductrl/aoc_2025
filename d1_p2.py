ans = 0
cur = 50

queries = input().split("\r");

for q in queries:
    x = q
    print(f'processing {x}...')
    
    rotations = int(x[1:])
    if x[0] == 'L':
        if cur == 0:
            ans -= 1
        ans += (cur - rotations) // (-100) + 1
        cur = (cur + rotations * 99) % 100
    else:
        ans += (cur + rotations) // 100
        cur = (cur + rotations) % 100
    
    # print(f'currently at {cur}')
    # print(ans)
    # ans += int(cur == 0)

print(ans)
