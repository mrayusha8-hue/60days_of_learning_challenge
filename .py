#Programming Language and Founders Dictionary

catalog = {
    "python": "Guido van Rossum",
    "java": "James Gosling",
    "c": "Dennis Ritchie",
    "c++": "Bjarne Stroustrup",
    "javascript": "Brendan Eich",
    "ruby": "Yukihiro Matsumoto",
}

collection = []

print("------------ CATALOG ------------")
for key, value in catalog.items():
    print(f"{key:11}: {value}")
print("-------------------------------")

while True:
    language = input("Select the language (q to quit): ").lower()
    if language == "q":
        break
    elif catalog.get(language) is not None:   # check if exists in dictionary
        collection.append(language)
    else:
        print("Sorry, not found.")

print("\n----- SELECTED LANGUAGES -----")
for language in collection:
    print(f"{language.title():11}: {catalog[language]}")
print("-------------------------------")
