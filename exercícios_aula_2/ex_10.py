for i in range(1, 11):
    l = [str(i)]
    for j in range(1, i + 1):
        if j % 2 == 0:
            l.append(str(j))
    print(" ".join(l))

