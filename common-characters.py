# Exercise 8.2 Write a function that gets as parameters two strings. The
# function returns the number of characters that the strings have in common.
# Each character counts only once, e.g., the strings "bee" and "peer" only have
# one character in common (the letter “e”). You can consider capitals different
# from lower case letters. Note: the function should return the number of
# characters that the strings have in common, and not print it. To test the
# function, you can print the result in your main program.

def common_characters(string1, string2):
    count = 0
    same = ''
    for x in string1:
        for z in string2:
            if x == z:
                if z not in same:
                    same += z
                    count += 1
    return count

def common_letters(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    same = set1 & set2

    return len(same)

if __name__ == '__main__':
    word1 = 'gopher'
    word2 = 'golfball'
    #num = common_characters(word1, word2)
    num = common_letters(word1, word2)
    print("The answer should be 2.")
    print("There are {} common letters in the words ({}) and ({}).".format(num, word1, word2))
