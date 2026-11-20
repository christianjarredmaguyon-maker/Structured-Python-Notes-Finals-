# 8. Custom Range
start = int(input("Enter start: "))
end = int(input("Enter end: "))

total = 0

for i in range(start, end + 1):
    total += i

print("Total:", total)
