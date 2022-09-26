lst=[(2,5),(1,2),(4,4),(2,3),(2,1)]
length=len(lst)
for i in range(length):         
    for j in range(0, length-i-1):
        if (lst[j][1] > lst[j + 1][1]):
               temp = lst[j]
               lst[j]= lst[j + 1]
               lst[j + 1]= temp
print(lst)