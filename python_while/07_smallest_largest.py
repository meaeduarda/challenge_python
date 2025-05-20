answer = 'S'
total_sum = 0
average = 0
quantity = 0
largest = 0
smallest = 0

while answer in 'S':
    number = int(input('Enter a number: '))
    total_sum += number
    quantity += 1

    if quantity == 1:
        largest = smallest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    answer = str(input('Do you want to continue? [Y/N] ').upper().strip()[0])  # upper - capitalize, strip removes spaces, 0 considers the first letter

average = total_sum / quantity
print(f'You entered {quantity} numbers and the average was {average}')
print(f'The largest number was {largest} and the smallest was {smallest}')
print('=' * 10)
print("IT'S FINISHED")