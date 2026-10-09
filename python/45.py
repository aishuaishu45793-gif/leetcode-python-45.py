# 111. Find the Third Largest Number

numbers = [10, 25, 8, 40, 30, 15]

unique_numbers = sorted(set(numbers), reverse=True)

if len(unique_numbers) >= 3:
    print("Third largest:", unique_numbers[2])
else:
    print("There are fewer than three distinct numbers.")