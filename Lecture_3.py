'''List & Tuple'''
# marsk1 = 94.4
# marks2 = 87.5
# marks3 = 95.2
# marks4 = 66.4
# marks5 = 45.1

# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])

# student = ["Chandra" , 95 , 21, "Kathmandu"]
# print(student[0])
# student[0] = "Raj"
# print(student)

# str = "hello"
# print(str[0])
# str[0] = "y"  #string is inmutable (Its cannot be change)
# print(str)

'''List Silicing'''
# marks = [87, 64, 33, 95, 76]
# print(marks[-3 : ])

'''List Method'''
# list = [2, 1, 3, 1]
# list.pop(2)
# print(list)

# list = ["a", "b" , "c"]
# list.sort(reverse=True)
# print(list)

'''Tuples in Python'''
# tup = (2, 1, 3, 1)
# print(tup[0])
# print(tup[1])

# tup[0] = 5
# print(tup)

# tup = (1, 2, 3, 4, 2, 2)
# # print(tup[1:3])
# # print(type(tup))
# print(tup.index(2))
# print(tup.count(2))

'''Practice Questions'''
#Q1
# movies = []
# Movie_1 = str(input("Enter First Movie Name:"))
# Movie_2 = str(input("Enter Second Movie Name:"))
# Movie_3 = str(input("Enter Third Movie Name:"))

# movies.append(Movie_1)
# movies.append(Movie_2)
# movies.append(Movie_3)
# print(movies)

#Q2
'''Palidrome Questions (Important)'''
# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]

# copy_list_1 = list_1.copy()
# copy_list_1.reverse()

# if(copy_list_1 == list_1):
#     print("palidrome")
# else:
#     print("Not Palidrome")

#Q3
# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"))

#Q4
# list = ["C", "D", "A", "A", "B", "B", "A"]
# list.sort()
# print(list)
