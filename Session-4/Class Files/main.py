# file1 = open(r'ye jaee\test.txt')

# print(file1.readline(), end='')
# print(file1.readline(), end='')
# print(file1.readline(), end='')

# file1.write("\nYe chizi")

# file1.close()

with open(r'ye jaee\test.txt', 'r') as file1:
    content = file1.read()
    print(content)

