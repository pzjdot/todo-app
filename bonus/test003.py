filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for item in filenames:
    item = item.replace('.', '-', 1)
    print(item)