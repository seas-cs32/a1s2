with open('CatInTheHat-excerptE.txt') as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Having some fun with text substitution
        # my code to replace ‘Cat’ with '\N{cat face with wry smile}'
        # my code to replace 'Hat' with '\N{top hat}'

        print(the_line, end='')

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break
