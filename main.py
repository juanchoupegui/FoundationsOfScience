number = int(input("Enter a number: "))

if number > 5:
    print("Number is larger than 5")
elif number == 5:
    print("Number is equal to 5")
else:
    print("Number is smaller than 5")


n1 = 10
n2 = 20


def suma(start, end):
    value = 0
    for n in range(start, end + 1, 1):
        value = value + n
    return value


result = suma(n1, n2)
print("The sum of numbers from " + str(n1) + " to " + str(n2) + " is: " + str(result))


def suma2(a, b):
    return b * (b + 1) / 2 - (a - 1) * a / 2


result2 = suma2(n1, n2)
print("The sum of numbers from " + str(n1) + " to " + str(n2) + " is: " + str(result2))


def output_string(s):
    print("The string is: " + str(s))


output_string("Hello Class")


def area_quadrilateral(length, width):
    area = length*width
    print("The area of the quadrilateral shape is: " + str(area))


area_quadrilateral(2, 2)


def suma3(a, *b):
    return a + sum(b)


print(suma3(1, 2))
print(suma3(1, 2, 3))
print(suma3(1, 2, 3, 4))
print(suma3(1, 2, 3, 4, 5))


def method(a, i):
    a[i] = -1


field = [1, 2, 3, 4, 5]
print(field)
method(field, 0)
print(field)
method(field, 4)
print(field)
