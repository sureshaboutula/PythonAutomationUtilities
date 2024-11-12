# file = open('test.txt')
# # Read all the content
# # print("Stle 1", file.read())
#
# # Read n number of characters by passing parameter
# #print("Style2", file.read(2))
#
# # Read one single line at a time
# print(file.readline()) # asdyus
# print(file.readline()) # bdddasd
#
# file.close()

# Print line by line using readline() method
# file = open('test.txt')
#
# line = file.readline()
# while line!='':
#     print(line)
#     line = file.readline()
#
# file.close()

file = open('test.txt')
# file.readlines()

for line in file.readlines():
    print(line)

file.close()