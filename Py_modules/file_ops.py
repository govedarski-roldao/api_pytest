try:
    f = open("myfile.txt", "r")
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
finally:
    f.close()

print("\n****Using with option****\n")
with open("myfile.txt", "r") as f:
    # print(f.readline())
    # list2 = f.read().split("\n")
    # print(list2)
    for line in f:
        print(line.strip())
