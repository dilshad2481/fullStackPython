import math
#1 Write a python script to take your name as input from the user and then print it.
name = input("What is your name? ")
print(name)
#2 Write a python script to take input from the user. Input must be a number.
number = int(input("Enter a number: "))
print(number)
#33. Write a python script which takes two numbers from the user, then calculate their sum
#and display the result.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(sum)
#4. Write a python script which takes the radius from the user and display area of a circle.
radius = float(input("Enter radius: "))
area = math.pi * (radius ** 2)
print(area)
#5. Write a python script to calculate the square of a number. Number is entered by the user.
number = int(input("Enter number to square it: "))
squared = number **2
print(squared)
#6Write a python script to calculate the area of Triangle. Number is entered by the user.
height = int(input("Enter height of triangle: "))
base = int(input("Enter base of triangle: "))
areaOfTriangle = (height * base) / 2
print(areaOfTriangle)
#7. Write a python script to calculate average of three numbers, entered by the user
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
average = (number1 + number2 + number3) / 3
print(average)
#8. Write a python script to calculate simple interest
principalAmount = int(input("Enter principal amount: "))
interestRate = (float(input("Enter annual interest rate as percentage: "))) / 100
time = float(input("Enter time in years: "))
finalAmount = principalAmount*(1 + (interestRate * time))
print(finalAmount)
#9. Write a python script to calculate the volume of a cuboid.
length = float(input("Enter length of cuboid: "))
width = float(input("Enter width of cuboid: "))
height = float(input("Enter height of cuboid: "))
volume = length * width * height
print(volume)
#10. Write a python script to calculate area of a rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print(area)