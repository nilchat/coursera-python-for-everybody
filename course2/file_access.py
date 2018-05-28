fhand = open("mbox-short.txt")
value = 0.0
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        # extract X-DSPAM-Confidence: value for each line
        value += float(line[line.find(":") + 1:])
        count += 1
print("{:.12f}".format(value / count))
