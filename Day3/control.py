# table
# for i in range(1,11):        
#     print(1*i," ",2*i," ",3*i," ",4*i," ",5*i," ",6*i," ",7*i," ",8*i," ",9*i," ",10*i)
# print("------------------------------------------------")
# for i in range(1,11): 
#     print(11*i," ",12*i," ",13*i," ",14*i," ",15*i," ",16*i," ",17*i," ",18*i," ",19*i," ",20*i)
    


#reverse :
# for i in range(1,11):        
#     print(i," " ,11-i)

# a = (1,2,4,5)
# b = (5,4,2,1)
# ans = zip(a,b)
# print(tuple(ans))

# for i in range(5):
#     a = int(input(""))
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)

# a = input("Enter any input: ")
# if(a.islower()):
#     print("LowerCase")
# elif(a.isupper()):
#     print("UpperCase")
# elif(a.isdigit()):
#     print("Digit")
#-----------------------------------------------------------------------------
# ch = ord(input("Enter any character: "))
# if(ch >= 65 and ch <=90):
#     print("Upper Case")
# elif ch >=97 and ch <=122:
#     print("Lower Case") 
# elif ch >= 48 and ch <=57:
#     print("Digit")
# else:
#     print("Special Character")        

# for ch in 'shriramkumawat':
#     print(ch)
#     if ch == 'm' :
#         break
#     print('Current Letter: ',ch)
#--------------------------------------------------------
# count = 0
# odd = 0
# for i in range(1,20):
#     if i%2 == 0:
#         count +=1
#     else:
#         odd +=1
# print("count: ",count)
# print("odd count: ",odd)
#-------------------------------------------------------------------------------------
# import time
# name = ""
# count = 0
# while name!="shriram":
#     count +=1
#     name = input("Enter your name: ")
#     if(count == 5):
#         print("Exceeded the trials you are blocked for 3 seconds:")
#         time.sleep(3)
# if(name == "shriram"):
#     print("Thanks for entering valid name")    
#----------------------------------------------------------------------------------------
import time
def registration():
    global username
    global password
    username = input("Create your username: ")
    password = input("Create your password: ")
def login():
    count = 0
    while(True):
        userInput = input("Enter your usernmae: ")
        passInput = input("Enter your password: ")
        if(userInput == username and passInput == password):
            print("Successfully Logged in ")
            break
        count +=1
        print("xxxxxxxxxxxxxxxxx Invalid username or password xxxxxxxxxxxxx\n")
        if(count == 3):
            print("Wait for 5 seconds!")
            time.sleep(5)
print("Register for the site: ")
registration()
print("------------Successfully Registered!------------\n")
print("Login your id and password ")
login()    
#-------------------------------------------------------------------------------

# n = int(input("Enter currency: "))
# if(n >= 1000):
#     print("1000 : ",n//1000)
#     n = n%1000
# if n>=200:
#     print("200  :",n//200)    
#     n = n%200
# if n>=100:
#     print("100  :",n//100)
#     n = n%100
# if n>=20:
#     print("20   :",n//20)
#     n = n%20
# if n>=10:
#     print("10   :",n//10)
#     n = n%10            
# if n>=5:
#     print("5   :",n//5)
#     n = n%5
# if n>=2:
#     print("2   :",n//2)
#     n = n%2
# if n>=1:
#     print("1   :",n//1)
#     n = n%1       