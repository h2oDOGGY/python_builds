#chapter 1
#addition
1+2 
1+3.5
-1+2.5

#subtracttion
100-45
-1.1+5

#muliplication
3*2
3.5*1.5
#division

	
#returns fraction
3/2
4/2
	#returns integer
3//2
-3//2
	#remainder
9%2

#exponents
2**2
2**10
1**10

#remember PEMDAS
#parentheses
#exponents
#multiplication
#division
#addition
#subtraction

#labels
a = 3
a +1

a=5
a+1

#types of numbers
type(3) #integer
type(3.5) #float
type(3.0) #float

#python will treat '3' different from '3.0' because they are different types
#convert to integer
int(3.8)
int(3.0)
#convert to float
float(3)

#functions
from fractions import Fraction #used to enter fractions
f = Fraction(3,4)
f
#Fraction(numberator, deominator)
Fraction(3,4)+1+1.5
Fraction(3,4) +1+Fraction(1/4)

#Complex numbers
a = 2+3j
type(a)

a = complex(2,3)
a
b=3+3j
a+b
a-b
a*b
a/b
#cannot use % or // for complex numbers

#use .real or .imag to retrieve complex number from variable
z = 2+3j
z.real
z.imag

# .conjugate() will retirieve equation but with opposite sign
z.conjugate()

#both real and imaginary parts are float
# abs() for absolute value

#getting user input
a=input() #input a value
a
s1 = 'a string'
s2 = "a string"
#strings are treated as characters
a='1'
int(a)+1 #convert a from string to integer
float(a)+1 #convert a from string to float

#cannot take a string with a floating point and convert
int('2.0')
#cannot supply fractional number as an input, and convert it to floating or integer
a=float(input())
3/4

a = input('Input an integer: ')
3
a = int(inputer())
a
a+1
 
# is_integer() used to check to see if value is an integer
1.1.is_integer() #false
1.0.is_integer() #true

#Fractions and COmplext Numbers as Input
a=Fraction(input('Enter a fraction: '))
3/4
a

z=complext(input('Enter a complex number: '))
2+3j #make sure to leave out spaces
z

#writing programs that do the math for you
#when a nonzero integer of a, divides into b, and has no remainder
def is_factor(a,b):
	if b % a ==0:
		return True
	else: return False

for i in range(1, 4):
	print(i)
#range loop starts at first integer and continues up to the integer just before the second one
for i in range(5):
	print(i)
#range loop starts at 0 (assumped value) and proceeds to integer just before listed value
for i in range(1,10,2):
	print(i)
#range loops steps by the third value listed

'''
Find the factors of an integer
'''

def factors(b):

	for i in range(1, b+1):
		if b % i == 0:
		print(i)

if __name__ == '__main__':

	b = input('Your Number Please: ')
	b = float(b)

	if b > 0 and b.is_integer():
		factors(int(b))
	else:
		print('Please enter a positive integer')

#format() plug labels and set it up so that they print in readable string
item1 = 'apples'
item2 = 'bananas'
item3 = 'grapes'
print('At the grocery store, I bought some {0} and {1} and {2}'.format(item1, item2, item3))
print('Number 1: {0} Number 2: {1} ' .format(1, 3.578))

def multi_table(a):
		for i in range(1,11):
			print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
	a = input('Enter a number: ')
	multi_table(float(a))

# .format() to specify decimal places; this will round up
'{0:.2f}'.format(1.23456789)

#convert units of measurement
(25.5*2.54)/100
#convert fahrenheit to celsius
F = 98.6
(F-32)*(5/9)
#convert celsisus to fahrenheit
C = 37
C*(9/5)+32

'''
Unit converter: Miles and Kilometers
'''
def print_menu():
	print('1. Kilometers to Miles')
	print('2. Miles to Kilometers')

def km_miles():
	km = float(input('Enter distance in kilometers: '))
	miles = km / 1.609
	
	print('Distance in miles: {0}'.format(miles))

def miles_km():
	miles = float(input('Enter distance in miles: '))
	km = miles * 1.609

	print('Distance in kilometers: {0}'.format(km))

if __name__ == '__main__':
	print_menu()
	choice = input('Which conversion would you like to do?: ')
	if choice == '1':
		km_miles()

	if choice == '2':
		miles_km()

#finding the roots of a quadratic equation
a = 1
b = 2
c = 1
D = (b**2 - 4*a*c)**0.5
x_1 = (-b + D)/(2*a)
x_2 = (-b-D)/(2*a)
x_1
x_2

'''
Quadratic equation root calculator
'''
def roots(a, b, c):
	D = (b*b - 4*a*c)**0.5
	x_1 = (-b + D)/(2*a)
	x_2 = (-b - D)/(2*a)

	print('x1: {0}'.format(x_1))
	print('x2: {0}'.format(x_2))

if __name__ == '__main__':
	a = input('Enter a: ')
	b = input('Enter b: ')
	c = input('Enter c: ')
	roots(float(a), float(b), float(c))

# 1
# print whether the number is even or odd
# display the number followed by the next 9 even or odd numbers

'''
even-odd vending machine
'''

def even_odd_vending(num): #define variable
	if(num % 2) ==0: #if number is divisable by 2 with 0 as a remainder
		print('Even') #then print 'even'
	else:
		print('Odd') #otherwise print 'odd'
	count =1 #
	while count <=9:
		num += 2 #add 2 to each number
		print(num) #print each num output
		count =+1 #increase in single increments
if __name__ == '__main__':
    try:
        num = float(input('Enter an integer: '))
        if num.is_integer():
            even_odd_vending(int(num))
        else:
            print('Please enter an integer')            
    except ValueError:
        print('Please enter a number')
		
#2 enhance the multiplication table so that it prints to whatever multiple chosen
'''
enhanced_multi_table.py

Multiplication table printer: Enter the number and the number
of multiples to be printed
'''

def multi_table(a):
		for i in range(1,11):
			print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    try:
        a = float(input('Enter a number: '))
		n = float(input('Enter the number of multiples: '))
		if not n.is_integer() or n < 0:
			print("The number of multiples should be a positive integer")
		else:
			multi_table(a, int(next))
		except ValueError:
			print('You entered an invalid input')

#3 create conversion for kilos and pounds; convert between units of temperature
'''
enhanced_unit_converter.py

Unit converter: 

Miles and Kilometers
Kilograms and Pounds
Celsius and Fahrenheit

'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

def kg_pounds():
    kg = float(input('Enter weight in kilograms: '))
    pounds = kg * 2.205

    print('Weight in pounds: {0}'.format(pounds))

def pounds_kg():
    pounds = float(input('Enter weight in pounds: '))
    kg = pounds / 2.205

    print('Weight in kilograms: {0}'.format(kg))

def cel_fahren():
    celsius = float(input('Enter temperature in celsius: '))
    fahrenheit =  celsius* (9 / 5) + 32
    print('Temperature in fahrenheit: {0}'.format(fahrenheit))

def fahren_cel():
    fahrenheit = float(input('Enter temperature in fahrenheit: '))
    celsius = (fahrenheit - 32)*(5/9)
    print('Temperature in celsius: {0}'.format(celsius))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do? ')

    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()

    if choice == '3':
        kg_pounds()
    if choice == '4':
        pounds_kg()
        
    if choice == '5':
        cel_fahren()
    if choice == '6':
        fahren_cel()

#4 write a fraction calculator  to perform basic mathematical operations between two fractions
'''
fractions_operations.py

Fraction operations
'''

from fractions import Fraction
def add(a, b):
    print('Result of adding {0} and {1} is {2} '.format(a, b, a+b))

def subtract(a, b):
    print('Result of subtracting {1} from {0} is {2}'.format(a, b, a-b))

def divide(a, b):
    print('Result of dividing {0} by {1} is {2}'.format(a, b, a/b))

def multiply(a, b):
    print('Result of multiplying {0} and {1} is {2}'.format(a, b, a*b))

if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a, b)
        if op == 'Subtract':
            subtract(a, b)
        if op == 'Divide':
            divide(a, b)
        if op == 'Multiply':
            multiply(a, b)
    except ValueError:
        print('Invalid fraction entered')

#5 all calculators to be extended
'''
Run until exit layout
'''
def fun():
print('I am in an endless loop')
if __name__ == '__main__':
	while True:
		fun()
	answer = input('Do you want to exit? (y) for yes ')
	if answer == 'y'
		break

#chapter 2