ans = 0
cur = 50

queries = input().split("\r");

for q in queries:
    x = q
    print(f'processing {x}')
    
    rotations = int(x[1:])
    if x[0] == 'L':
        cur = (cur + rotations * 99) % 100
    else:
        cur = (cur + rotations) % 100
    
    ans += int(cur == 0)

print(ans)
