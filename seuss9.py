with open('CatInTheHat-excerptE.txt') as my_open_book:
#with open('CatInTheHat-excerptS.txt') as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Having some fun with text substitution
        #the_line = the_line.replace('Cat', 'Gato')
        #the_line = the_line.replace('Cat', '\u0047')
        #the_line = the_line.replace('Cat', '\U00000047')
        #the_line = the_line.replace('Cat', '\U0001F63C')
        the_line = the_line.replace('Cat', '\N{cat face with wry smile}')

        print(the_line, end='')

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break
