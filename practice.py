# Define variables
name, name1 = 'sumel', 'sumel ahmad'
age = age1 = 25
phone = '017790'
email = 'sumelahmadbd@gmail.com'

print(name)


# Prompt user to enter their information
name = str(input("Enter your Name: "))
age = int(input("Enter Your Age: "))
phone = int(input("Enter Your Phone Number: "))
email = str(input("Enter Your E-mail: "))

print(name, age, phone, email)


# Take two inputs separated by a space

a, c = input().split()
a = int(a)
c = int(c)
b = a / c

print(b)

a = 5
a = a+5

print(a)

a = 5
a += 5
print(a)

a = 5
a %= 4

print(a)

a = 5
a **= 4

print(a)

r = int(input("Enter The Radious:"))
p = 2*3.1416*r
print(p)