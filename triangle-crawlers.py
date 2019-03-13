# Exercise 7.16
#  Consider the triangle shown below. This triangle houses a colony of Tri-
#  angle Crawlers, and one big Eater of Triangle Crawlers. The Eater is located
#  in point D. All Triangle Crawlers are born in point A. A Triangle Crawler
#  which ends up in point D gets eaten.  Every day, each Triangle Crawler moves
#  over one of the lines to a randomly-determined neighboring point, but not to
#  the point where he was the day before. This movement takes one day. For
#  instance, a Triangle Crawler that was just born in A, on the first day of
#  his life will move to B, C, or D. If he moves to B, the next day he will
#  move to C or D (but not back to A). If on his first day he moves to C
#  instead, the next day he will move to B or D (but not back to A). If he
#  moves to D, he gets eaten.

#                              C
#                             /|\
#                            / | \
#                           /  |  \
#                          /   |   \
#                         /    |    \
#                        /     D     \
#                       /     / \     \
#                      / ..../   \---, \
#                     /.%             `.\
#                    A ----------------- B

#  There is a one-third probability that Triangle Crawler on the first day of
#  his life immediately goes to D, and therefore only lives one day. In
#  principle, a Triangle Crawler may reach any age, however high, by moving in
#  circles from A to B to C and back to A again (or counterclockwise, from A to
#  C to B and back to A again). However, since every day he makes a random
#  choice between the two possible follow-up directions, every day after the
#  first there is a one-half probability that he ends up in point D, and dies.
#  Write a program that calculates an approximation of the average age that a
#  Triangle Crawler reaches. Do this by simulating the lives of 100,000
#  Triangle Crawlers, counting the days that they live, and dividing the total
#  by 100,000. The output of your program should be a single floating point
#  number, rounded to two decimals.

#  Hint 1: You can follow two different approaches: either you simulate the
#  behavior of one single Triangle Crawler and repeat that 100,000 times, or
#  you start with a population of 100,000 triangle crawlers in point A, and
#  divide these over variables that keep track of how many Triangles are in
#  each point, each day, including the point that they came from (assigning a
#  remaining odd Triangle Crawler to a randomly determined neighboring point).
#  The first method is short and simple but slow, the second is long and
#  complex but fast. You may use either method.

#  Hint 2: Do not use 100,000 Triangle Crawlers in your first attempts. Start
#  with 1000 (or even only 1), and only try it out with 100,000 once your
#  program is more or less finished. Testing is much quicker with fewer
#  Triangle Crawlers. 1000 Triangle Crawlers should be done in under a second,
#  so if your program takes longer, you probably have created an endless loop.

#  Hint 3: I won’t be too specific, but the final answer is somewhere between 1
#  and 5 days. If you get something outside that range, it is definitely wrong.
#  You may try to determine the exact answer mathematically before starting on
#  the exercise, which is doable though quite hard.

# We can't use the choice() method, because it hasn't been introduced yet,
# so we can use numbers to represent positions: 1 = A, 2 = B, 3 = C, 4 = D

from random import randrange

daysLived = 0
for t in range(1,100000):

    choice = ''
    PP = '' # the Previous Position
    day = 0
    while True:
        day += 1
        #print("Day ", day)

        if day == 1:
            PP = 1
            choice = randrange(2, 5)
            #print("crawler is at 1 and went to", choice)
            continue

        if choice == 1: # If the crawler picks A
            if PP == 2: # if the previous position was B
                choice = randrange(3, 5) # options are C = 3 or D = 4
                #print("crawler is at 1 and went to", choice)
            if PP == 3: # if the previous position was C
                choice = randrange(2, 5, 2) # options are B = 2 or D = 4
                #print("crawler is at 1 and went to", choice)
            PP = 1 # set the previous position to the current position
            continue

        if choice == 2:
            if PP == 1:
                choice = randrange(3, 5)
                #print("crawler is at 2 and went to", choice)
            if PP == 3:
                choice = randrange(1, 5, 3)
                #print("crawler is at 2 and went to", choice)
            PP = 2
            continue

        if choice == 3:
            if PP == 1:
                choice = randrange(2, 5, 2)
                #print("crawler is at 3 and went to", choice)
            if PP == 2:
                choice = randrange(1, 5, 3)
                #print("crawler is at 3 and went to", choice)
            PP = 3
            continue

        if choice == 4:
            #print("dead at", day, "days old")
            daysLived += day
            break

print( "Average life span is {0:2f}".format(daysLived / 100000) )
