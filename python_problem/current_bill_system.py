total_unit = int(input("Enter the amount of total unit: "))
sum = 0
temp = 0
for i in range(1, total_unit + 1):
    if i == 50:
        sum = sum + i * 3.75
        print(sum)
    if i > 50 and i < 76:
        temp = i
        sum = sum + i * 4.19
        print(sum)
    if i <= 200:
        sum = sum + i * 5.72
        print(sum)
    if i <= 300:
        sum = sum + i * 6.00
        print(sum)
    if i <= 400:
        sum = sum + i * 6.34
        print(sum)
    if i <= 600:
        sum = sum + i * 9.94
        print(sum)
    else:
        sum = sum + i * 11.46
        print(sum)

print("Your total current bill is : ", sum)
