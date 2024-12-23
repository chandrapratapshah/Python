'''String & Conditional Statements'''
# str1 = 'chanda patap shah'
# str2 = "chanda Pratap shah"
# str3 = '''chandra pratap shah'''

#Double and Single cots use for :-
# "This isn't chandra pratap shah"
# 'This isn"t chandra pratap shah'

# str4 = "This is a string. \twe are creating it in python."
# print(str4)

'''Concatenation'''
# str5 = "apna"
# str6 = "college"
# final_str = str5 + " " + str6
# print(final_str)
# print(len(final_str))

'''Length of str'''
# str7 = "chandrapratapshah"
# str8 = "apnacollege"
# len1 = len(str7)
# len2 = len(str8)
# print(len1 , len2)

'''Indexing'''
# str = "Apna College"
# chr = str[3]
# print(chr)
# print(str[2])

'''Slicing'''
# str = "ApnaCollege"
# print(str[:6])

# str= "Apple"
# print(str[-4:])

'''String Function'''
# str = "i am studing python from Apnacollege"
# print(str.endswith("ge"))
# print(str.capitalize())
# print(str.replace("python" , "JavaScripts"))
# print(str.find("from"))
# print(str.count("python"))

'''Questions Practice'''
#Q1
# name = str(input("Enter First Name :"))
# name = len(name)
# print("Length of your name is", name)

#Q2
# str = "Hi, $I am the $ symbol of 1$, $ is currency of $ USA"
# print(str.count("$"))

'''Conditional Statements'''
# light = "re"

# if (light == "red"):
#     print("STOP")
# elif(light == "green"):
#     print("GO")
# elif(light == "yellow"):
#     print("LOOK")
# else:
    # print("CONFUSED")

# num = 5

# if(num > 2):
#     print("greater than 2")
# elif(num > 3):
#     print("grater than 3")

# age = 16

# if(age >= 18):
#     print("Can Vote") #indentation {}
# else:
#     print("Can't Vote")

'''Example'''
# marks = int(input("Enter Student Marks :"))

# if(marks >= 90):
#     print("Grade = A")
# elif(90 > marks and marks >= 80 ):
#     print("Grade = B")
# elif(80 > marks and marks >= 70):
#     print("Grade = C")
# else:
#     print("Grade = D")

'''Nesting'''
# age = 17

# if(age >= 18):
#     if(age >= 80):
#         print("Can't drive")
#     else:
#         print("Can Drive")
# else:
    # print("Can't drive")

'''Practice Questions'''

#Q1
# num = int(input("Enter Number:"))

# if(num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

#Q2
# num_1 = int(input("Enter 1st Number:"))
# num_2 = int(input("Enter 2st Number:"))
# num_3 = int(input("Enter 3st Number:"))

# if(num_1 >= num_2 and num_1 >= num_3):
#     print(num_1)
# elif(num_2 >= num_3):
#     print(num_2)
# else:
#     print(num_3)

#Q3
# num = int(input("Enter a Number :"))

# if(num % 7 == 0):
#     print("Yes" , num , "is a multiple of 7.")
# else:
#     print("Not a Multiple of 7.")