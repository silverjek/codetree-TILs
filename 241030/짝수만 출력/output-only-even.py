arr = input().split()
a, b = int(arr[0]), int(arr[1])
while a<b+1:
    if a%2==0:
        print(a, end=' ')
    a += 1