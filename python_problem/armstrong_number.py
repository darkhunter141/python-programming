num = input()
sum = 0
result = 0
for char in num:
    cub_sum = sum + int(char)**len(num)
    result = cub_sum + result
    print(result)
if result == int(num):
    print("yes")
else:
    print("no")
