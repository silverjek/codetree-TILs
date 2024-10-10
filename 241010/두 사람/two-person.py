arr1 = input().split()
arr2 = input().split()
ageA, ageB = int(arr1[0]), int(arr2[0])
sexA, sexB = arr1[1], arr2[1]

if ageA>=19 and sexA=='M' or ageB>=19 and sexB=='M':
    print(1)
else:
    print(0)