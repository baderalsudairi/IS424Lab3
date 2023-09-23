
numbers = []


for i in range(10):
    value = float(input(f"Enter value {i + 1}: "))
    numbers.append(value)

element in the list
largest = numbers[0]


for number in numbers:
    if number > largest:
        largest = number


print(f"The largest number in the list is: {largest}")
