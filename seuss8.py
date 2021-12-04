with open('CatInTheHat-excerptE.txt') as my_open_book:
#with open('CatInTheHat-excerptS.txt') as my_open_book:
    while True:
        the_line = my_open_book.readline()
        print(the_line, end='')

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break
