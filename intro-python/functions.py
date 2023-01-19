# def myFunction():
#     print('My first function :D')

# myFunction()

# def printData(*argument):
#     print('Argument value:', argument)

# printData('Hola', 'soy', 'Eric', 'Pennachini')

# def fullName(name, lastName, age):
#     print(name, lastName, '(' + str(age) + ')')

# fullName(name='Eric', lastName='Pennachini', age=31)

# def fullName2(**kwa):
#     print(kwa['name'], kwa['lastName'], '(' + str(kwa['age']) + ')')


# fullName2(name='Eric', lastName='Pennachini', age=31)

# def myFunctionList(list):
#     for l in list:
#         print(l)

# myFunctionList([234, 234, 234])

# def concatenateStrings(stringList):
#     strings = ''
#     for s in stringList:
#         strings = strings + s + ' '
#     return strings

# print(concatenateStrings(['asd', 'sdf', 'ert']))


def recursiveFunc(i):
    if i < 1:
        return i
    print('i = ' + str(i))
    recursiveFunc(i - 1)

recursiveFunc(8)
