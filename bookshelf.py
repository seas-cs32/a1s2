def my_replace(s, old, new):
    """Returns a string replacing all occurrences of old with new."""
    i = 0           # tracks where we are in the input string
    j = len(old)    # skip-ahead amount for index calculations
    new_s = s[0:0]  # the new string we're building

    while i < len(s):
        if s[i:i+j] == old:
            new_s = new_s + new
            i += j
        else:
            new_s = new_s + s[i:i+1]
            i += 1

    return new_s


def main():
    # Create a string object with a line from The Cat in the Hat
    the_line = 'The Cat in the Hat!'
    print(the_line)
    the_line = my_replace(the_line, 'Hat', '\N{top hat}')
    print(the_line)

    # Create a representation of the objects on my shelf
    stuffed_lion = '\N{lion face}'
    kids_pic = 'kids.jpg'
    textbook = 'cs50y.scriv'
    favorite_cd = 'BornToRun.mp3'
    novel = 'CatInTheHat.txt'

    # Create a sequence object that represents my shelf
    shelf = [stuffed_lion, kids_pic, textbook, favorite_cd, novel]
    print(shelf)

    # Make it look like our textbook has been opened on my shelf
    shelf = my_replace(shelf, [textbook], ['\N{open book}'])
    print(shelf)

if __name__ == '__main__':
    main()