print("Get max, min, swap value of variables")
print("\n1. Max \n2. Min \n3. Swap")

a, b = map(int, input("Enter two numbers (comma separated): ").split(","))

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Maximum value:", max(a, b))

elif choice == 2:
    print("Minimum value:", min(a, b))

elif choice == 3:
    a, b = b, a
    print("After swapping:", a, b)

else:
    print("Invalid Choice")
