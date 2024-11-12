
it = 10

# while it > 1:
#     if it !=3:
#         print(it)
#     it -= 1

while it > 1:
    if it == 9:
        it -= 1
        continue
    elif it == 3:
        break
    else:
        print(it)
    it -= 1

print("While loop execution is completed")