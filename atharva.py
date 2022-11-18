
x = 16
r = x % 2

if r == 0:
    print("Even")
    if x > 5:           # Nested If condition
        print("Great")

    else:
        print("Not so great")

else:
    print("Odd")

print("Ok Bye!!!")

# elif condition

a = 2

if a == 1:
    print("One")
elif a == 2:
    print("Two")
elif a == 3:
    print("Three")

else:
    print("wrong input")
