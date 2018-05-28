import re
fh = open("regex_sum_94691.txt")
all_number_list = []
for line in fh:
    line = line.rstrip()
    numbers = re.findall("[0-9]+", line)
    if len(numbers) > 0:
        all_number_list.extend(numbers)

all_number_list = list(map(int, all_number_list))
print(sum(all_number_list))
