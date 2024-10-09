arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
min = a
if b<min:
    min = b
elif c<min:
    min = c
print(min)