# Find numbers between 100 and 300 divisible by 7 but not multiples of 5

numbers = []  # list to store valid numbers

for i in range(100, 301):  # 301 because the upper limit is inclusive
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(str(i))  # convert to string for joining later

# Display results in one line separated by commas
print(", ".join(numbers)) 

