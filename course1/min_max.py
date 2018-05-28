largest = None
smallest = None
nums = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    nums.append(num)

largest = max(nums)
smallest = min(nums)

print("Maximum is", largest)
print("Minimum is", smallest)
