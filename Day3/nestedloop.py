import time

# n=int(input("Enter the number of rows: ")) 
# for i in range(1,n+1):
#     time.sleep(0.3) 
#     print("* "*n) 

n=int(input("Enter the number of rows: ")) #n=5
for i in range(1,n+1): #i=1  , n=6
    for j in range(1,n+1): # j=1
        print(i,end=" ")
    print()