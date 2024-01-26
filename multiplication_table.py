# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 13: Print multiplication table from 1 to 10:

for number in range (1,11):
    print (number, ":", end = " ")
    for number_2 in range (1,11):
        print ((number * number_2), end=" ")
    print()

