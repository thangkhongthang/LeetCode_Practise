def numberOfArrays(differences, lower, upper):
    lis = []
    lis.append(0)
    for i in range(len(differences)):
        a = lis[i]+differences[i]
        lis.append(a)
    l = lower - min(lis)
    u = upper - max(lis)
    if u -l +1<=0:
        return 0  

    return u - l +1
differences = [1,-3,4]
lower = 1
upper = 6
print(numberOfArrays(differences, lower, upper))
