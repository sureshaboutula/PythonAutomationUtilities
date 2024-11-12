# read the file and store all the lines in the list
# reverse the list and write back to the text file
with open('test.txt', 'r') as reader: # This style of opening file does not need file.close()
    content = reader.readlines()
    #reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
