a = input().split()
b = input().split()
c = input().split()
a[1], b[1], c[1] = int(a[1]), int(b[1]), int(c[1])
A, B, C, D = 0, 0, 0, 0

if a[0] == 'Y':
    if a[1] >= 37:
        A += 1
    else:
        C += 1
else:
    if a[1] >= 37:
        B += 1
    else:
        D += 1

if b[0] == 'Y':
    if b[1] >= 37:
        A += 1
    else:
        C += 1
else:
    if b[1] >= 37:
        B += 1
    else:
        D += 1

if c[0] == 'Y':
    if c[1] >= 37:
        A += 1
    else:
        C += 1
else:
    if c[1] >= 37:
        B += 1
    else:
        D += 1

if A>=2:
    print('E')
else:
    print('N')