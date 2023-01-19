# inputData = input('Enter some data: ')

# newList = ['hi', 'world', 'black', 'cat', 'Leia']

# if newList.count(inputData) > 0:
#     print('You\'ve guessed a value: "', inputData, '" :D')
# else: 
#     print('The value doesn\'t exists :c')

defaultErrorMessage = 'Not a number! Aborting...'

print('')

firstValue = input('Enter 1st value: ')
numberFirstValue = 0

try:
    numberFirstValue = int(firstValue)
except:
    print(defaultErrorMessage)
    exit()

secondValue = input('Enter 2nd value: ')
try:
    numberSecondValue = int(secondValue)
except:
    print(defaultErrorMessage)
    exit()

result = 0

operation = input('Enter an operation: ')

print('-----------------')

if operation == '+':
    result = int(firstValue) + int(secondValue)
elif operation == '-':
    result = int(firstValue) - int(secondValue)
elif operation == '*':
    result = int(firstValue) * int(secondValue)
elif operation == '/':
    result = int(firstValue) / int(secondValue)
else:
    print('Operation not supported! Aborting...')
    exit()

print('Result:', result)
print('')