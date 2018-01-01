# сортировка выбором

ar = [5, 1, 8, 2, 10, 13, 4]

for i in range(len(ar)):
    value = ar[i]
    index = i
    for j in range(i+1, len(ar)):
        if ar[j] < value:
            value = ar[j]
            index = j

    ar[index] = ar[i]
    ar[i] = value

print(ar)








