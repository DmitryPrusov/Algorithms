ar = [5, 1, 13, 2, 10, 8, 4]

for maxi in reversed(range(len(ar))):
    for i in range(0, maxi):
        if ar[i] > ar[i+1]:
            temp = ar[i]
            ar[i] = ar[i+1]
            ar[i+1] = temp
print(ar)


