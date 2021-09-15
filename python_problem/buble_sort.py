list = [10,1,5,45,78,25,6]

for i in range(len(list)-1):
    for j in range (len(list)-1-i):
        if list[j]> list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)
