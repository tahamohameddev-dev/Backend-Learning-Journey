# ####################################
# 01. SYNTAX & PRINTING
# ####################################

print("hello world")

print(2026 + 4)

# ####################################
# 02. VARIABLES & DATA TYPES
# ####################################

name = "Tom"
age = 22
is_Developer = True

print(name)

# ####################################
# 03. WORKING WITH STRINGS & NUMBERS
# ####################################

phrase = "Backend Academy"

print(phrase.upper())
print(phrase.lower())

print(phrase.isupper())
print(phrase.islower())

print(len(phrase))

print(phrase.index("B"))
print(phrase.replace("Academy","Lerning"))

# NUMBERS

my_num = 5
print(str(my_num) + " my favorite number")

print(3 + 4)
print(3 - 4)
print(3 / 4)
print(3 * 4)

print(abs(-5))
print(pow(4, 2))
print(max(9, 8))
print(min(4, 7))
print(round(7.5))

# ####################################
# 0.4 GITTING INPUT & BASIC CALCULATOR
# ####################################

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " your age " + age + "!")


# Calculator

num_1 = input("Enter number: ")
num_2 = input("Enter number: ")

Calculation = int(num_1) + int(num_2)
print(Calculation)

# ####################################
# 0.5 LISTS & LIST FUNCTIONS & TUPELS 
# ####################################

skills = ["Python", "Linux", "Git"]
skills.append("Databases")
skills.insert(1,"Docker")
skills.remove("Git")
# skills.clear()
print(skills )
print(skills.index("Python"))
print(skills.count("Linux"))

skills2 = skills.copy()

print(skills2)

# Tuples

