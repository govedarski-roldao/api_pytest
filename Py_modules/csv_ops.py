import csv

with open("my_file.csv", mode="r") as file:
    csv_file = csv.reader(file)
    for line in csv_file:
        print(line[2])

print(
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

with open("my_file.csv", mode="r") as file:
    csv_other = csv.DictReader(file)
    for line in csv_other:
        print(line["email"])

print(
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
rows = []
with open("my_file.csv", mode="r") as file:
    csv_next = csv.reader(file)
    header = next(csv_next)
    for row in csv_next:
        rows.append(row)
print(rows)