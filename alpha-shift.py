# TODO:
# - make it work with lowercase letters, too

def alphaShift(shift):
    for i in range(65,91):
        print(chr(i), end='')
    print()
    for i in range(65, 91):
        z = i + shift
        if z > 90:
            print(chr(z - 26), end='')
        if z <= 90:
            print(chr(z), end='')
    print()

def letterShift(letter, shift):
    z = ord(letter) + shift
    if z > 90:
        L = chr(z - 26)
    if z <= 90:
        L = chr(z)
    return L

if __name__ == "__main__":
    print("Shift alphabet by 13")
    alphaShift(13)
    print("3rd letter from N is {}".format(letterShift('N', 3)) )
