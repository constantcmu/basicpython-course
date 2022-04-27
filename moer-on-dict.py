point = {}
n = int(input())
for k in range(n):
    ID , p = input().split()
    p = int(p)
    if ID not in point:
        point[ID] = [p,1]
    else:
        point[ID][0] += p
        point[ID][1] += 1
print(point)


exec(input().strip())

