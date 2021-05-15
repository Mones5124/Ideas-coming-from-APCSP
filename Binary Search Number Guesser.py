#two different binary searches will be used and I will export csv files with data of how long it took
#testing out binary search versus binary search with random instead of always starting at the middle

from random import randint
import pandas as pd
import matplotlib.pyplot as plt

#variables used in both
overall_minimum = 0
overall_maximum = 2**52

#overall_maximum = round((2**50))  #-2
#overall_maximum = 9235361611000000     #-100000000000000
#       seems to keep changing
#     maximum that python allows:
#           2^53 = 9007199254740992
#           somewhere between 2^53 and 10^17-1 it stops working (less than 2^54)

#python doesn't support 2^54 integers or 17 digits - 1
#       actually it does support 2^54 but only 3 repeats
#       could this have something to do with 64 bit and only being able to use 2^55 leaving 9 bits for other things
#       could it be possible that it can't have a very high number of repeats for that same reason?
# that's also why you can't have a very high number of repeats without crashig either

#overall_maximum = 10000000000000000


print(overall_maximum)
#print(str(len(str(overall_maximum))) + " digits")
repeat = 4000

#total number of digits needed to be computed
#print(str(len(str(overall_maximum*repeat))) + " digits")
#up to 20 digits?

#total number of integer spaces, one set of the max -1 for the pandas series and then the max as it computes it
"""print((overall_maximum*repeat)-1)
print(str(len(str((overall_maximum*repeat)-1))) + " digits")
"""
# 17 digits starting with 3602
#working: 72057594037927935         ^52 with 4 repeats  17 digits
#not working: 90071992547409919
#   but if I go with a smaller number and repeat it more, I get to 19 digits with no problem

"""normal binary search to find what number the person guessed"""

#reseting the values for the new loop
bs_loops_list = []
for i in range (0, repeat):
    minimum = overall_minimum
    maximum = overall_maximum
    bs_num = randint(minimum, maximum)
    #print(bs_num)
    loop = 0
    guess = (maximum+minimum)/2
    while guess != bs_num:
        #print(guess)
        if guess == bs_num:
            #print("broke")
            break
        elif guess > bs_num:
            maximum = guess
        elif guess < bs_num:
            minimum = guess
        loop += 1
        guess = round((maximum+minimum)/2, 0)
    #print(loop)
    bs_loops_list.append(loop)

#print(loops_list)
bs_loops_series = pd.Series(data = bs_loops_list)
#print(bs_loops_series)
print("Average for Binary Search: ")
print(sum(bs_loops_list)/len(bs_loops_list))
# ~2 seconds each for 10000 or 100000 from 0-10

#binary search is the most efficient

"""binary search with random guessing and then it picks above and below"""
minimum = overall_minimum
maximum = overall_maximum
#reseting the values for the new loop
#print(bs_rd_num)

#print()

bs_rd_loops_list = []
for i in range (0, repeat):
    minimum = overall_minimum
    maximum = overall_maximum
    bs_rd_num = randint(minimum, maximum)
    #print(bs_num)
    loop = 0
    guess = randint(minimum, maximum)
    while guess != bs_num:
        #print(guess)
        if guess == bs_num:
            #print("broke")
            break
        elif guess > bs_num:
            maximum = guess
        elif guess < bs_num:
            minimum = guess
        loop += 1
        guess = randint(minimum, maximum)
    #print(loop)
    bs_rd_loops_list.append(loop)

#print(loops_list)
bs_rd_loops_series = pd.Series(data = bs_rd_loops_list)
#print(bs_rd_loops_series)
print("Average for Random + Binary Search: ")
print(sum(bs_rd_loops_list)/len(bs_rd_loops_list))

"""Random Guess and taking out numbers already guessed"""
minimum = overall_minimum
maximum = overall_maximum
#reseting the values for the new loop

rd_num = randint(minimum, maximum)
#print(rd_num)


#binary search
#bs_loops_series.plot.bar()
#plt.bar(len(bs_loops_series), bs_loops_series)
#plt.bar(, bs_loops_list)
bs_loops_series.groupby([bs_loops_series]).count().plot.bar()
plt.title("Number of loops needed for Binary Search Algorithm")
plt.show()

#binary search random 
#bs_rd_loops_series.plot()
#plt.bar(len(bs_rd_loops_series), bs_rd_loops_series)
bs_rd_loops_series.groupby([bs_rd_loops_series]).count().plot.bar()
plt.title("Number of loops for needed for Binary Search with random pick Algorithm")
plt.show()




















"""
for x in range (9015300000000000, 10000000000000000):
    #           this code keeps changing the output I don't know what it varies on though
    overall_maximum = x
    print(overall_maximum)
    #print(str(len(str(overall_maximum))) + " digits")
    repeat = 10

    #normal binary search to find what number the person guessed

    #reseting the values for the new loop
    bs_loops_list = []
    for i in range (0, repeat):
        minimum = overall_minimum
        maximum = overall_maximum
        bs_num = randint(minimum, maximum)
        #print(bs_num)
        loop = 0
        guess = (maximum+minimum)/2
        while guess != bs_num:
            #print(guess)
            if guess == bs_num:
                #print("broke")
                break
            elif guess > bs_num:
                maximum = guess
            elif guess < bs_num:
                minimum = guess
            loop += 1
            guess = round((maximum+minimum)/2, 0)
        #print(loop)
        bs_loops_list.append(loop)

    #print(loops_list)
    #print("good")
    bs_loops_series = pd.Series(data = bs_loops_list)
    #print(bs_loops_series)
    #print("Average for Binary Search: ")
    #print(sum(bs_loops_list)/len(bs_loops_list))
    # ~2 seconds each for 10000 or 100000 from 0-10

    #binary search is the most efficient

    #binary search with random guessing and then it picks above and below

    minimum = overall_minimum
    maximum = overall_maximum
    #reseting the values for the new loop
    #print(bs_rd_num)

    #print()

    bs_rd_loops_list = []
    for i in range (0, repeat):
        minimum = overall_minimum
        maximum = overall_maximum
        bs_rd_num = randint(minimum, maximum)
        #print(bs_num)
        loop = 0
        guess = randint(minimum, maximum)
        while guess != bs_num:
            #print(guess)
            if guess == bs_num:
                #print("broke")
                break
            elif guess > bs_num:
                maximum = guess
            elif guess < bs_num:
                minimum = guess
            loop += 1
            guess = randint(minimum, maximum)
        #print(loop)
        bs_rd_loops_list.append(loop)

    #print(loops_list)
    bs_rd_loops_series = pd.Series(data = bs_rd_loops_list)
    #print(bs_rd_loops_series)
    #print("Average for Random + Binary Search: ")
    #print(sum(bs_rd_loops_list)/len(bs_rd_loops_list))
"""#"""
