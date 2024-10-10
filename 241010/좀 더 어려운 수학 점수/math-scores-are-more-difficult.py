arr1 = input().split()
arr2 = input().split()
am, ae = int(arr1[0]), int(arr1[1])
bm, be = int(arr2[0]), int(arr2[1])

if am>bm:
    print('A')
elif bm>am:
    print('B')
else:
    if ae>be:
        print('A')
    else:
        print('B')