# Exercise 1 — Easy
# Create and Write a File

# Tasks:
# 1. Create a file named student.txt.
file=open("student.txt","w")
# 2. Write your name, university, and degree into it.
file.write("usman shakir \n dawood university of engineering and technology \n data sciecnce")
# 3. Close the file using with open().
file.close()


# Exercise 2 — Easy
# Read a File

# Tasks:
# 1. Open student.txt in read mode.
file = open("student.txt", "r")
    
# 2. Read the complete content.
content = file.read()
file.close()
# 3. Print it.
print(content)

