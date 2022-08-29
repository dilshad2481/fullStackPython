#Assignment 5
#1. Write a python script to remove the last digit from a given number. (for example, if
#user enters 2534 then your output should be 253)
number = float(input("Enter a number: "))
removedDigit = int(number / 10)
print(removedDigit)
#2. Write a python script to get the last digit from a given number. (for example, if user
#enters 2089 then your output should be 9)
number = float(input("Enter a number: "))
lastDigit = int(number % 10)
print(lastDigit)
#3. Write a python script to swap data of two variables
a = float(input("Enter a: "))
b = float(input("Enter b: "))
temp = a
a = b
b = temp
print("After swapping: a = %d, b = %d" %(a,b))
#4. Write a python script to find x power y, where values of x and y are given by user
x = float(input("Enter x value: "))
y = float(input("Enter y value: "))
print(x ** y)
#5. Write a python script which takes a three digit number from the user and displays
#only its first digit.
number = int(input("Enter three digit number: "))
firstDigit = int(number / 100)
print(firstDigit)
#6. Write a python script which takes a three digit number from the user and displays
#only its middle digit.
number = int(input("Enter a number: "))
middleNumber = int((number / 10)) % 10
print(middleNumber)
#7. Write a python script which takes a three digit number from the user and displays
#only its last digit.
number = int(input("Enter three digit number: "))
lastDigit = number % 10
print(lastDigit)
#8. Write a python script to use IN operator to display the data present in the list
list = [3,5,6,7,34,26,7,3,75,2,7,4]
print(3 in list)
#9. Write a python script to use NOT IN operator to display the data not present in list
list2 = [3,5,6,2,0,47,35,2,3,4,5,6]
print(5 not in list2)
#10. Write a python script to use IS operator to display if both variables are the same
#object or not?
a = 'coke'
b = 'pepsi'
c = a
print(a is b)
print(a is c)
