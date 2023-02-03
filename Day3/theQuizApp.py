thisdic = {
    "Which is the world's largest country?": "Russia",
    "Which country has the highest GDP?   " : "USA",
    "Which country has the highest population in the globe?": "China",
    "Which is the smallest country in the world?": "Vatican City",
    "Number of Oceans on planet Earth?    ": 5,
    "Number of continents on planet Earth?": 7,
}


for i in thisdic:
    print(i)
    answer = input("Answer: ")
    if(answer == thisdic.get(i)):
        print("Correct!")
    else:
        print("Incorrect!")    
# print(thisdic)
# for i in thisdic:
#     print(i)
#     print(thisdic.get(i))
    # print(thisdic[i])
    # print(thisdic.keys())
    # print(thisdic.values())