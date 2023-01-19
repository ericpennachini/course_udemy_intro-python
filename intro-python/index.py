# condición imposible
# if 5 < 3:
#     print("esto no se va a ver")

x = "ericssen el crack"
y = 1234

# print(x, y)

email = "eric.pennachini@gmail.com"

# print(email)

a, b, c = "you", "are", "perfect"

# print(a, b, c)

value1 = value2 = value3 = "go"

# print(value1, value2, value3)

begin = "help "
end = "me"

# print(begin + end)


word = "palabra"
phrase = 'asdasd asdasd'

# print(word, phrase)

anIntegerNumber = 209
aFloatNumber = 209.34
aComplexNumber = 24j

# print(anIntegerNumber, aFloatNumber, aComplexNumber)



_list = [1, 2, 3]

print(_list)

# list.clear()

print(_list)

list2 = _list.copy()

_list.append(5)

print(_list, list2)

list3 = _list

print(_list, list2, list3.count(2))

print(len(_list))


# list.pop()

# list.append("hola")

_list.reverse()
print(_list)

_list.sort()
print(_list)


tuple = ('hi', 'i\'m', 'Eric')
print(tuple)
print(tuple.index('hi'))

newListFromTuple = list(tuple)

# print(newListFromTuple)

newRange = range(10)

# print(newRange)

newDictionary = {
    "name": "Aslan",
    "race": "negrito peludo",
    "age": 14
}

print(newDictionary)
print(newDictionary["name"])
print(newDictionary.get("age"))

# newDictionary["noisy"] = True

# print(newDictionary)

# newDictionary.pop("age")
# print(newDictionary)

# newDictionary.popitem()
# print(newDictionary)

# copyOpNewDict = newDictionary.copy()
# otherCopyOfDict = dict(newDictionary)

# del newDictionary["race"]
# print(newDictionary)

# copyOpNewDict.clear()
# print(copyOpNewDict, otherCopyOfDict)


michis = {
    "Aslan": {
        "name": "Aslan",
        "age": 14,
        "race": "negrito"
    },
    "Ragnar": {
        "name": "Ragnar",
        "age": 5,
        "race": "negrito"
    },
    "Leia": {
        "name": "Leia",
        "age": 0.5,
        "race": "marmoladita"
    }
}
print(michis)

doguis = dict(
    name="Iron",
    race="border collie",
    age=10
)

print(doguis)