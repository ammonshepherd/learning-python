# http://www.spronck.net/pythonbook/index.xhtml
# Exercise 7.15
# 5 pirates, 1 monkey, and ??? coconuts

#   According to an old puzzle, five pirates and their monkey are stranded on
#   an island. During the day they gather coconuts, which they put in a big
#   pile. When night falls, they go asleep.  In the middle of the night, the
#   first pirate wakes up, and, not trusting his buddies, he divides the pile
#   into five equal parts, takes what he believes to be his share and hides it.
#   Since he had one coconut left after the division, he gives it to the
#   monkey. Then he goes back to sleep.

#   An hour later, the next pirate wakes up. He behaves in the same way as the
#   first pirate: he divides the pile into five equal shares, with one coconut
#   left over which he gives to the monkey, hides what he believes to be his
#   share, and goes to sleep again.  The same happens to the other pirates:
#   they wake up one by one, divide the pile, give one coconut to the monkey,
#   hide their share, and go back to sleep.

#   In the morning they all wake up. They divide what remains of the coconuts
#   equally amongst them. Since that leaves one coconut, they give it to the
#   monkey.  Exercises 91

#   The question is: what is the smallest number of coconuts that they can
#   have started with?  Write a Python program that solves this puzzle. If you
#   can solve it for any number of pirates, all the better.

b = 0
answer = "no"
while answer == "no":
    b += 1
    # uncomment these two lines if the monkey gets a coconut in the morning
    #u = ((b * 5) + 1)
    #monkey = 6

    # uncomment these two lines if the monkey does not get a coconut in the
    # morning (most solutions online use this option)
    u = b * 5
    monkey = 5
    if u % 4 == 0:
        v = u / 4
        t = ((v * 5) + 1)
        if t % 4 == 0:
            w = t / 4
            s = ((w * 5) + 1)
            if s % 4 == 0:
                z = s / 4
                r = ((z * 5) + 1)
                if r % 4 == 0:
                    y = r / 4
                    q = ((y * 5) + 1)
                    if q % 4 == 0:
                        x = q / 4
                        p = ((x * 5) + 1)
                        print("start with: ", p, "coconuts")
                        print("pirate 1 takes", x, "coconuts, leaving", q)
                        print("pirate 2 takes", y, "coconuts, leaving", r)
                        print("pirate 3 takes", z, "coconuts, leaving", s)
                        print("pirate 4 takes", w, "coconuts, leaving", t)
                        print("pirate 5 takes", v, "coconuts, leaving", u)
                        print("in the morning the pirates divide", u, "coconuts among themselves") 
                        g = u // 5
                        print("each pirate gets", g, "coconuts")

                        print()
                        print("pirate 1 gets a total of", x + g)
                        print("pirate 2 gets a total of", y + g)
                        print("pirate 3 gets a total of", z + g)
                        print("pirate 4 gets a total of", w + g)
                        print("pirate 5 gets a total of", v + g)
                        print()
                        print("the monkey gets", monkey, "coconuts")

                        answer = "yes"
                        break
                    else:
                        answer = "no"
                        continue
                else:
                    answer = "no"
                    continue
            else:
                answer = "no"
                continue
        else:
            answer = "no"
            continue
    else:
        answer = "no"
        continue
