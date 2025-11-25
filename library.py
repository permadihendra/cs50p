import random
import sys
from time import sleep

names = []

for arg in sys.argv[1:]:
    print(arg)
    names.append(arg)

print(names)

print("Lets suffle it three times :")
for i in range(3):
    random.shuffle(names)
    print(names)
    print("\n Lets suffle again")
    sleep(2)
