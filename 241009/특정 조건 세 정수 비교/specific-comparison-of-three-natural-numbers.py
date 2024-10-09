arr = input().split()
arr[0], arr[1], arr[2] = int(arr[0]), int(arr[1]), int(arr[2])
if arr[0]==min(arr):
    print(1, end = " ")
else:
    print(0, end = " ")
if arr[0]==arr[1]==arr[2]:
    print(1)
else:
    print(0)