# number = int(input("Enter a number: "))
#
# if number > 5:
#     print("Number is larger than 5")
# elif number == 5:
#     print("Number is equal to 5")
# else:
#     print("Number is smaller than 5")

def suma(start, end):
    value = 0
    for number in range(start, end + 1, 1):
        value = value + number
    return value

def suma2(a, b):
    return b*(b+1)/2 - (a-1)*a/2

def OutputString(s):
    print("The string is: " + str(s))

def areaCuadrilateral(l, a):
    area = l*a
    print("The area of the cuadrilateral shape is: " + str(area))

def suma3(a, *b):
    return a+ sum(b)

print(suma3(1,2))
print(suma3(1,2,3))
print(suma3(1,2,3,4))
print(suma3(1,2,3,4,5))

def method(a, id):
    a[id] = -1

field = [1,2,3,4,5]
print(field)
method(field, 0)
print(field)
method(field, 4)
print(field)

n1 = 10
n2 = 20
result = suma(n1, n2)
result2 = suma2(n1, n2)
print("The sum of numbers from " + str(n1) + " to " + str(n2) + " is: " + str(result))
print("The sum of numbers from " + str(n1) + " to " + str(n2) + " is: " + str(result2))
OutputString("Hello Class")
areaCuadrilateral(2, 2)