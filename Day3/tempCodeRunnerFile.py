# squares = []
# for i in range(1,11):
#     squares.append(i**3)
# print(squares)
#--------------------------------------------------------------
#printing values directly in the list
# print([i*i for i in range(11)])    

#----------------------------------------------------------------
#using map 
# def square(x):
#     return x*x
# squares = list(map(square,[1,2,3,4,5]))
# print(squares)

#--------------------------------------------------------------------
#using lambda function 
# squares = list(map(lambda x: x*x, [1,2,3,4,5]))
# print(squares)

#5.
# fruits = [" ManGo", "@apple@", "bananas", " CHIKKU ", "Guava"]
# fruits[0] = fruits[0].lower().lstrip()
# fruits[1] = fruits[1].replace("@","")
# fruits[3] = fruits[3].lower().strip()
# fruits[4] = fruits[4].lower()
# for i in fruits:
#     print(i)

# readable and easier than the upper using map  

# def newFruits(x):
#     return x.title().strip().replace("@","")
# fruits = list(map(newFruits, [" ManGo", "@apple@", "bananas", " CHIKKU ", "Guava"]))
# print(fruits)

# fruits = [" ManGo", "@apple@", "bananas", " CHIKKU ", "Guava"]
# def clean(x):
#     return x.strip("@ ").capitalize()
# fruits = [clean(f) for f in fruits]
# print(fruits)

# name = "shriram kumawat"
# print(name.capitalize())
# print(name.title())

#---------------------------------------------------------------
# movies = ["Pathaan","Bahubali","KGF", "Drishyam","Kesari"]
# stars = ["SRK","Prabhas","Yash","AD","AK"]
# # for i,j in list(zip(movies,stars)):
#     # print(f"{j} stars in {i} movie.")
# print(list(zip(movies,stars)))

#------------------------------------------------------------
str = input("Enter any string: ")
s = str.lower()
for i in s:
    cn = 0
    for j in s:
        temp = i
        
        if(temp == j):
            cn += 1
    print(f"{i} occurred {cn} times in {str}")

# table = int(input("Enter the number: "))
