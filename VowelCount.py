l = input("Enter a string: ")
count = 0
for C in l.lower():     
    if C in "aeiou":
        count += 1
print("no of vowels:", count)