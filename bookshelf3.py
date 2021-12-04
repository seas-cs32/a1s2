import seuss14

def main():
    # Create a string object with a line from The Cat in the Hat
    the_line = 'The Cat in the Hat!'
    print(the_line)
    the_line = seuss14.my_replace(the_line, 'Hat', '\N{top hat}')
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
    shelf = seuss14.my_replace(shelf, [textbook], ['\N{open book}'])
    print(shelf)

if __name__ == '__main__':
    main()