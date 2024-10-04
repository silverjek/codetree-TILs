arr = input().split()
arr = [int(x) for x in arr]
print(sum(arr))
print(sum(arr)//len(arr))
print(sum(arr)-sum(arr)//len(arr))