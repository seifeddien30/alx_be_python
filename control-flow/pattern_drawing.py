sizePattern = int(input("Enter the size of the pattern:"))
i = 0
x = 0
while i < sizePattern:
    for x in range(sizePattern):
        print("*", end="") 
    print()
    
    i += 1
