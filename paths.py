i = int(input("i = "))
j = int(input("j = "))
D = int(input("D = "))
C = int(input("C ="))


def Count_Paths(i, j, D, C):
    if (i > D) or (j > C):
        return Count_Paths == 0
    elif (i == D) and (j == C):
        return 1
    else:
        return Count_Paths == (Count_Paths(i + 1, j, D, C) + Count_Paths(i, j + 1, D, C))


print(Count_Paths(i, j, D, C))




