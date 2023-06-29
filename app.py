

# course = "Python's for beginners"
# print(course)
#
# course = 'Python for "Beginners"'
# print(course)
#
# course = ''''
# Hi Lee,
#
# Here is your internship letter from safaricom
#
# Thank you,
# The support team
#
# '''
# print(course)


# course = 'python for beginners'
# print(len(course))  # print length of the word course
# print(course.find('n'))  # print the index of that letter where it appears first
# print(course.upper())  # convert word to upper case
# print(course.title())  # capitalize every word in the sentence
# print(course.capitalize())  # capitalise the fist letter in a statement
# print('python' in course)  # checks whether the word exist in a statement
# print(course.replace('beginners', 'dummies'))  # finds and replace the word selected i.e beginners


# print(10+3)  # Addition = 13
# print(10-3)  # Subtraction = 7
# print(10*3)  # Multiplication = 30
# print(10**3)  # Exponential(power) = 1000
# print(10//3)  #  Returns the whole part of a fraction = 3
# print(10%3)  # Modulus(Returns the remainder after division) = 1
# print(10/3)  # Division(Returns the combined value after division) = 3.3333333333

#operation precedence
# Parenthesis
# Exponential
# Division
# Multiplication
# Addition
# Subtraction


# conditional statements
# weight Converter
# weight = int(input("Enter your weight: "))
# weightType = input(('(L)bs or (K)gs: '))
#
# if weightType.upper() == 'L':
#     convertedWeight = weight * 0.45359237
#     print(f"You are {convertedWeight} kilos")
# else:
#     convertedWeight = weight / 0.45359237
#     print(f"You are {convertedWeight} pounds")

# pin = 8626
# pinTrial = 0
# trialLimit = 3
# while pinTrial < trialLimit:
#     Enter_Pin = int(input("Enter the pin: "))
#     pinTrial += 1
#     if Enter_Pin == pin:
#         print("You can now proceed dude")
#         break
# else:
#     print("Sim card blocked")

# number = int(input("Enter a number to be checked"))
#
# if number%2 == 0:
#     print("The number is even")
# elif number%2 == 1:
#     print("The number is an odd number")
#     if  number/1 == number and number/number == 1 and number%3 != 0 :
#         print("The number is a prime number")
# else:
#     print("The number seems not to be existing!!!")

# class Human:
#     def eat(self,human):
#         print("all {} can eat".format(human))
#
# class Child(Human):
#
#     name = "Lee"
#
#     def walk(self):
#         print("All chidren can walk")
#         print(self.name)
#
#     def eat(self,human):
#         super().eat(human)
#
# child =  Child()
#
# child.eat("Children")
#
# child.walk()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
