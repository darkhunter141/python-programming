#
#
# n = int(input("enter your number"))
# result = 0
# for i in range(1,n+1):
#     result = result + i
#     print(result)
# print(result)


# n = int(input("enter your number"))
# result = 0
# for i in range(1,n+1):
#     result = result + i*i
#     print(result)
# print(result)
#
#
# n = int(input("enter your number"))
# result = 0
# for i in range(1,n+1):
#     result = result + i**i
#     print(result)
# print(result)
#
# n = int(input("enter your number"))
# result = 0
# r = 0
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         result = result + 1
#         print(result, end= ' ,')
#         r = r + result
#     print()
# print(r)


n = int(input("Enter your number"))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        i = -i
    else:
        i = + i
    print(i, end=' ,')
    sum = sum + i
print()
print("Sum of the series is: ", sum)
