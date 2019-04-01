import math
first_index = raw_input("Enter the first index ")
first_index = float(first_index)
second_index = raw_input("Enter the second index ")
second_index = float(second_index)
third_index = raw_input("Enter the third index ")
third_index = float(third_index)
#Obtain the inputs and convert them into decimal numbers#
answer_1 = ((-1 * second_index) + math.sqrt((second_index ** 2) - (4 * first_index * third_index))) / 2
answer_2 = ((-1 * second_index) - math.sqrt((second_index ** 2) - (4 * first_index * third_index))) / 2
#Applied Quadratic formula#
print answer_1
print answer_2
#This program can't calculate complex numbers :( #
