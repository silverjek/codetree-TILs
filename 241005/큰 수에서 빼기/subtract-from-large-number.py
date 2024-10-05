arr = input().split()
a, b = int(arr[0]), int(arr[1])
if a>b:
    res = a-b
if b>a:
    res = b-a
print(res)