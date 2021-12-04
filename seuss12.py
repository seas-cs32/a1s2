# specify the interface for my_replace
#     specify the implementation of my_replace

with open('CatInTheHat-excerptE.txt') as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Having some fun with text substitution
        # call my_replace on the_line, specifying ‘Cat’ is replaced by '\N{cat face with wry smile}'
        # call my_replace on the_line, specifying 'Hat' is replaced by '\N{top hat}'

        print(the_line, end='')

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break
