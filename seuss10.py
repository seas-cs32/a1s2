with open('CatInTheHat-excerptE.txt') as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Having some fun with text substitution
        the_line = the_line.replace('Cat', '\N{cat face with wry smile}')
        the_line = the_line.replace('Hat', '\N{top hat}')

        print(the_line, end='')

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break
