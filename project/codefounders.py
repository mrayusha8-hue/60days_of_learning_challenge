#Programming Language and Founders Dictionary

catalog = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich",
    "Ruby": "Yukihiro Matsumoto",}
collection = []
total_list=0
print("------------ CATALOG ------------")
for key,value in catalog.items():
    print(f"{key:11}: {value}")

print("-------------------------------")
while True:
    language = input("Select the language (q to quit): ").lower()
    if language == "q":
        break
    elif catalog.get(language) is not None:   # check if exists in dictionary
        collection.append(language)            


for language in collection:
    total_list += catalog.get(language)
    print(language)
 


    

     