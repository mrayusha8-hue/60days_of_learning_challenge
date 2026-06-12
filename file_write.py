#Write a program that creates a file named notes.txt and writes three lines of text to it using the with statement.
with open("notes.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

with open("notes.txt", "r") as f:
    print(f.read())


#Wite a program that appends the line "This is an appended line." to notes.txt without erasing existing content.

with open("notes.txt", "a") as f:
 f.write("This is an appended line.\n")
with open("notes.txt","r") as f:
    print(f.read())
    
#Character Counts
with open("notes.txt", "r") as file:
    total_chars = len(file.read())
print(total_chars)

#Count words
with open("notes.txt", "r") as f:
    notes = f.read()

words = notes.split()
print("Words:", len(words))

#Count lines
with open("notes.txt", "r") as f:
    lines = f.readlines()

print("Lines:", len(lines))

#Search lines
word = input("Enter word: ")

with open("notes.txt", "r") as f:
    data = f.read()

if word in data:
    print("Found")
else:
    print("Not Found")

#reading lines using loop
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())