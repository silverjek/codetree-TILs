arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
if a<b and a<c:
    if b<c:
        print(b)
    else:
        print(c)
if b<a and b<c:
    if a<c:
        print(a)
    else:
        print(c)
if c<a and c<b:
    if a<b:
        print(a)
    else:
        print(b)