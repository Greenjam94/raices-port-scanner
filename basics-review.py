# # Reading input
# name = input("whats your name?")
# hello_name = "hello " + name + "!"
# print(hello_name)

# # Writing to a file
# f = open("hello.txt", "a")
# f.write(hello_name + "\n")
# f.close()

# For loops
# names = ["Simon", "Johanna", "Eduardo"]
# for name in names:
#     print("Hello " + name + "!")

# If statements
# new_member = True
# if new_member:
#     print("Welcome to RAICES!")
# else:
#     print("Welcome back!")

# Exceptions
import sys
from time import sleep

try:
    while True:
        print("Infinite loop!")
        sleep(2)
except KeyboardInterrupt:
    print("\n Exiting Program!")
    sys.exit()
