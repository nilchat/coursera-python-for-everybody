name = input("Enter file:")
senders = []
maxCount = 0
maxKey = None
with open(name) as fh:
    for line in fh:
        if line.startswith("From "):
            words = line.rstrip().split()
            senders.append(words[1])
sender_count = {name: senders.count(name) for name in senders}
for key in sender_count:
    if sender_count[key] > maxCount:
        maxCount = sender_count[key]
        maxKey = key

print(maxKey, maxCount)
