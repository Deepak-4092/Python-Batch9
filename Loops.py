# Program 1: Using while loop with break
while True:
    name = input("Enter your name: ")
    if name != "":
        break



# Program 2: Using continue to skip characters
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ")


print()
# Program 3: Using break in for loop
for i in range(1, 21):
    if i == 13:
        break
    print(i, end=" ")
