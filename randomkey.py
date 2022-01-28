import random
import string
import csv
import pandas as pd

def randomkey(size = 8, chars =
	string.ascii_letters +  string.digits
	+ '!@#$%&()<>?'):
	return ''.join(random.choice(chars) for x in
		range(size))

#for x in range(3):
#	print(randomkey())

rk1 = randomkey()
rk2 = randomkey()
rk3 = randomkey()
rk4 = randomkey()
rk5 = randomkey()
rk6 = randomkey()
rk7 = randomkey()
rk8 = randomkey()
rk9 = randomkey()
rk10 = randomkey()
rk11 = randomkey()
rk12 = randomkey()
rk13 = randomkey()
rk14 = randomkey()
rk15 = randomkey()
rk16 = randomkey()
rk17 = randomkey()
rk18 = randomkey()
rk19 = randomkey()
rk20 = randomkey()

randomlist = [rk1, rk2, rk3, rk4, rk5, rk6, rk7,
rk8, rk9, rk10, rk11, rk12, rk13, rk14, rk15, rk16
, rk17, rk18, rk19, rk20]

df = pd.DataFrame(randomlist)
df.to_csv('randomlist.csv',index=False,
	header=False)
