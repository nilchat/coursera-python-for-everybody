name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

hours = []
for line in fh:
    if line.startswith("From "):
        words = line.rstrip().split()
        hours.append(words[5].split(":")[0])
hours_count = [(item, hours.count(item)) for item in hours]
hours_count = sorted(set(hours_count))


for item in hours_count:
    print(item[0], item[1])
