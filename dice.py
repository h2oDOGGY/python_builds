import os
os.chdir(r"C:\My\script\\path\")

import time
from random import *

person = input("Please enter your name: ")

print("Hello",person, 'are you ready to play? [Y/N]')
response = input("")
if response == "Y":
	print("Throwing die")
	dice_1 = randint(1,6)
	dice_2 = randint(1,6)
	total = dice_1 + dice_2
	time.sleep(3)
	print(dice_1)
	print(dice_2)
	print(total)
elif response =="y":
	print("Throwing die")
	dice_1 = randint(1,6)
	dice_2 = randint(1,6)
	total = dice_1 + dice_2
	time.sleep(3)
	print(dice_1)
	print(dice_2)
	print(total)
else:
	print("Goodbye", person)