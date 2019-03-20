# http://www.spronck.net/pythonbook/index.xhtml
# Exercise 7.15
# 5 tourists, 1 monkey, and ??? coconuts

#   According to an old puzzle, five tourists and their monkey are stranded on
#   an island. During the day they gather coconuts, which they put in a big
#   pile. When night falls, they go asleep.  In the middle of the night, the
#   first tourist wakes up, and, not trusting his buddies, he divides the pile
#   into five equal parts, takes what he believes to be his share and hides it.
#   Since he had one coconut left after the division, he gives it to the
#   monkey. Then he goes back to sleep.

#   An hour later, the next tourist wakes up. He behaves in the same way as the
#   first tourist: he divides the pile into five equal shares, with one coconut
#   left over which he gives to the monkey, hides what he believes to be his
#   share, and goes to sleep again.  The same happens to the other tourists:
#   they wake up one by one, divide the pile, give one coconut to the monkey,
#   hide their share, and go back to sleep.

#   In the morning they all wake up. They divide what remains of the coconuts
#   equally amongst them. Since that leaves one coconut, they give it to the
#   monkey.  Exercises 91

#   The question is: what is the smallest number of coconuts that they can
#   have started with?  Write a Python program that solves this puzzle. If you
#   can solve it for any number of tourists, all the better.

b = 0
while True:
    b += 1
    # uncomment these two lines if the monkey gets a coconut in the morning
    u = ((b * 5) + 1)
    monkey = 6

    # uncomment these two lines if the monkey does not get a coconut in the
    # morning (most solutions online use this option)
    #u = b * 5
    #monkey = 5
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
                        print("A tour boat crashes on a deserted island.")
                        print("During the day, the five stranded tourists gather", int(p), "coconuts")
                        print("During the night, each greedy tourist decides to hide some coconuts for him/herself.")
                        print("Secretly by turns, each tourist divides the pile into five equal parts, burries his/her part, and leaves the rest in a pile.")
                        print("They give a coconut to a watching monkey, so it doesn't wake the rest of the tourists.")
                        print()
                        print("tourist 1 takes", int(x), "coconuts, leaving", int(q))
                        print("tourist 2 takes", int(y), "coconuts, leaving", int(r))
                        print("tourist 3 takes", int(z), "coconuts, leaving", int(s))
                        print("tourist 4 takes", int(w), "coconuts, leaving", int(t))
                        print("tourist 5 takes", int(v), "coconuts, leaving", int(u))
                        print()
                        print("in the morning the tourists divide", u, "coconuts among themselves") 
                        g = u // 5
                        print("each tourist gets", g, "coconuts")

                        print()
                        print("tourist 1 gets a total of", int(x + g))
                        print("tourist 2 gets a total of", int(y + g))
                        print("tourist 3 gets a total of", int(z + g))
                        print("tourist 4 gets a total of", int(w + g))
                        print("tourist 5 gets a total of", int(v + g))
                        print()
                        print("the monkey gets", monkey, "coconuts")

                        break
