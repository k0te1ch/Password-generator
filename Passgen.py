import os
import sys
from random import randint

def generate(len):
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        os.system("cls")
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system("clear")
    print("Passwords:")
    for _ in range(10):
        for _ in range(len):
            print(chr(randint(32, 127)), end="")
        print()

generate(int(input("The number of characters in the password?\n")))

input("Press enter to exit")