#print(random.randint(5, 20))
#What did you see on line 1?
#I was getting numbers between 5 and 20, so I imagine that the 2 integers in "print(random.randint(5, 20))" dictate the range to generate from


#print(random.randrange(3, 10, 2))
#What did you see on line 2?
#3, 5, 7, 9. I imagine that similar to .radint that the first 2 integers are the range, but with the first being the start and the second the stop and the 3rd indicating the step size

#What was the smallest number you could have seen, what was the largest?
#Smallest can be 3, the start and the largest will be 9 as the step size of 2prevents a 10 or higher

#Could line 2 have produced a 4?
#negative as it can only go in increments from 2 from 3, meaning the next possible integer would be 5

#print(random.uniform(2.5, 5.5))
#What did you see on line 3?
#Either a 2,3,4 or 5 followed by a long randomly generated decimal, assuming a randomly generated float in the range of 2.5 to 5.5
#What was the smallest number you could have seen, what was the largest?
#2.5 is the smallest and 5.5 the largest as random.uniform is inclusive


import random

def main():
    print(random.randint( 1, 100))

main()