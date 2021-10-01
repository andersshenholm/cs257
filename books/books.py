import booksdatasource
import sys
import argparse
class Books:
    def __init__(self):
        self.data_source = booksdatasource.BooksDataSource("books1.csv")
        parser = argparse.ArgumentParser(description= "Commands for searching and sorting for books")
        parser.add_argument('--authorsearch', '-a', help = 'searches for authors whose names contain the given string', nargs = '+')
        parser.add_argument('--titlesearch', '-t', help = 'searches for books with titles that contain the given string' )
        parser.add_argument('--datesearch', '-d', help = 'searches for books which were published between the two given dates' )
        parser.set_defaults(authorsearch = '')
        args = parser.parse_args()
        if(args.authorsearch):
            output_list = []
            for a in args.authorsearch:
                output_list.append(self.data_source.authors(a))
            print(output_list)

       
b = Books() 