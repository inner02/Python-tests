def find_length_of_a(b, c):
    return (c**2 - b**2)**0.5

def find_length_of_b(a, c):
    return (c**2 - a**2)**0.5

def find_length_of_c(a, b):
    return (a**2 + b**2)**0.5

def main():
    print("Pythagoras' Calculator")
    print("1. Find the length of A given B and C")
    print("2. Find the length of B given A and C")
    print("3. Find the length of C given A and B")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        b = float(input("Enter the length of side B: "))
        c = float(input("Enter the length of side C: "))
        a = find_length_of_a(b, c)
        print("Length of side A:", a)
    elif choice == 2:
        a = float(input("Enter the length of side A: "))
        c = float(input("Enter the length of side C: "))
        b = find_length_of_b(a, c)
        print("Length of side B:", b)
    elif choice == 3:
        a = float(input("Enter the length of side A: "))
        b = float(input("Enter the length of side B: "))
        c = find_length_of_c(a, b)
        print("Length of side C:", c)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
