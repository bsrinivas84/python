import random

#Generators are useful when you want to produce values one at a time instead of building everything in memory at once.
#1. Yields lazily 2. Faster Start 3. Stream data 4. Cleaner iteration
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    print("After For")
    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)
    print("After final yield")

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))