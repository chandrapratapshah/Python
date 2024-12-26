'''Dictionary & Set'''
'''Dictionary'''

# dict = {
#     "name" : "chandra",
#     "learning" : "coding",
#     "subject" : ["python", "java", "C"],
#     "topic" : ("dict", "set"),
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4,
#     12.99 : 94.5,
#     12.99 : 94.5 #duplicate key can not be included
# }
# print(dict)
# print(dict["name"])
# print(dict["topic"])
# print(dict["age"])

# dict["name"] = "RAJ"
# dict["surname"] = "SHAH" #from this method we can add dict key.
# print(dict)

# null_dict = {}
# null_dict["name"] = "chandrapratapshah"
# print(null_dict)

'''Nested Dictionaries'''
# student = {
#     "name" : "chnadra",
#     "sub" : {
#         "phy" : 95,
#         "che" : 94,
#         "mth" : 97
#     }
# }

'''Dictionaries Methods'''

# print(len(list(student.keys())))
# print(len(list(student.values())))
# pairs = list(student.items())
# print(pairs[1])
# print(student["sub2"]) #Its return errror
# print(student.get("sub2")) #but, its return -> None
# new_dict = {"age" : 23, "grade" : "A"}
# student.update(new_dict)
# print(student)

'''Sets in Python'''

# collection = {1, 2, 2, 2, "hello", "world", "world", 4}
# print(collection)
# print(len(collection))
# collection = {} #it is empty dictionary

# collection = set()
# print(collection)
# print(type(collection))

'''Sets Method'''
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("chandrapratapshah")
# collection.add("DPS")
# collection.add("IIT-Madras")
# collection.add((1,2,3))
# # collection.add([1,2,3]) #hastvalue
# # collection.remove(1)
# # collection.clear()
# print(collection)

# collection = {"hello", "apnacollege", "world", "coding","python"}

# print(collection.pop())
# print(collection.pop())
# print(collection.pop())

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.union(set2))
# # print(set1)
# # print(set2)
# print(set1.intersection(set2))

'''Practice Question'''
#Q1
# dict = {
#     "cat" : "a small animal",
#     "table" : ("a piece of furniture", "list of fact & Figures")
#     #We can use Tuple as well list in this function
# }
# print(dict)

# #Q2
# list1 = {
#     "python", "java", "C++", "python", "javascript",
#     "java", "python", "java", "C++", "C"
# }
# print(len(list1))

#Q3
'''Method 1'''
# sub_1 = int(input("Enter Sub 1 Marks:"))
# sub_2 = int(input("Enter Sub 2 Marks:"))
# sub_3 = int(input("Enter Sub 3 Marks:"))

# dict = {
#     "Subject_1" : sub_1,
#     "Subject_2" : sub_2,
#     "Subject_3" : sub_3,
# }
# print(dict)

'''Method - 2'''
# marks = {}

# x = int(input("enter phy:"))
# marks.update({"phy" : x})

# x = int(input("enter mth:"))
# marks.update({"mth" : x})

# x = int(input("enter che:"))
# marks.update({"che" : x})

# print(marks)

#Q3
# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)