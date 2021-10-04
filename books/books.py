'''
    books.py
    10/2/2021

    Simon Hempel-Costello, Anders Shenholm
'''
import booksdatasource
import sys
import argparse
class Books:

    def __init__(self):
        args = self.get_arguements('books1.csv')
        self.handle_arguements(args)
    def get_arguements(self, file_string):
        self.data_source = booksdatasource.BooksDataSource(file_string)
        parser = argparse.ArgumentParser('handle books commands')
        subparsers = parser.add_subparsers(description = 'commands')
        #Break parsing into 3 subparsers for explicity in code definition
        title_parser = subparsers.add_parser('titlesearch',help = 'Given a search string S, print a list of books whose titles contain S (case-insensitive). Books may be sorted by title (by default) or by publication year.')
        title_parser.add_argument(
            'titlesearch',
            help = 'search for books which have names that contain the following character string',
            default  = '',
            nargs='?',

        )
        #call for date sort
        title_parser.add_argument(
            '-y',
            help = 'sort books by year',
            default  = '',
            action='store_true'

        )
        #parsing for author search
        author_parser = subparsers.add_parser('authorsearch',help = 'Given a search string S, print a list of authors whose names contain S (case-insensitive)')
        author_parser.add_argument(
            'authorsearch',
            #sorry for inconsistency here with the "" vs ', I wanted to show posession and didn't want to deal with the symbol stuff for python
            help = "Given a search string S, print a list of authors whose names contain S (case-insensitive). For each such author, print a list of the author's books.",
            default  = '',
            nargs='?',

        )
        #parsing for date search
        date_search = subparsers.add_parser('datesearch',help = 'Given a range of years A to B, print a list of books published between years A and B')
        date_search.add_argument(
            'datesearch',
            help = "Given a range of years A to B, print a list of books published between years A and B. If a start date is not given, it searches for books that are before the end date, and if an end date is not given, then it searches for books after the start date.If neither are given, all books will be published in increasing order of date",
            default  = '',
            nargs='?',
        )
        date_search.add_argument(
            '--startdate','-s',
            help = 'date to start the list with',
            default = None, 

        )
        date_search.add_argument(
            '--enddate','-e',
            help = 'date to end the list with',
            default = None
        )
        args = parser.parse_args()
        return args
    def handle_arguements(self, arguments):
        #Each of the three programmed in options, help is built into argsparse for python
        if('titlesearch' in arguments):
            self.titlesearch_return(arguments)
        elif('authorsearch' in arguments ):
            self.authorsearch_return(arguments)
        elif('datesearch' in arguments):
            self.datesearch_return(arguments)
        else:
            raise ValueError('some command must be inputted, please enter one of (titlsearch, datesearch, authorsearch, --help) to continue')
    def titlesearch_return(self, arguments):
        #if -y is called, sort by date, otherwise sort by title
        if(arguments.y):
            print(self.data_source.books(arguments.titlesearch, sort_by='year'))
        else:
            print(self.data_source.books(arguments.titlesearch))
    def authorsearch_return(self, arguments):
        #Print out the authors and the books they wrote
        author_list = self.data_source.authors(arguments.authorsearch)
        for a in author_list:
            print(str(a) + " Books Written:" + str(self.data_source.search_books_by_author(a)))
    def datesearch_return(self, arguments):
        #Print out the books between the given years
        print(self.data_source.books_between_years(arguments.startdate, arguments.enddate))
if __name__ == '__main__':
    b = Books()
