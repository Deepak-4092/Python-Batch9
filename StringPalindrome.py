i = input("Enter a string: ")
a = i.replace(" ", "").lower()
if a == a[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
