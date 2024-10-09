arr1 = input().split()
arr2 = input().split()
am, ae = int(arr1[0]), int(arr1[1])
bm, be = int(arr2[0]), int(arr2[1])
if am>bm and ae>be:
    print(1)
else:
    print(0)