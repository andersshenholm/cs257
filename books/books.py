'''
    books.py
    10/11/2021

    Simon Hempel-Costello, Anders Shenholm
    Revised by Simon Hempel-Costello, Anders Shenholm
'''
import booksdatasource
import argparse

class BooksSearch:

    def __init__(self, file_string):
        self.data_source = booksdatasource.BooksDataSource(file_string)

    def titlesearch_return(self, arguments):
        #if -y is called, sort by date, otherwise sort by title
        if(arguments.year):
            book_list = self.data_source.books(arguments.titlesearch, sort_by='year')
        else:
            book_list = (self.data_source.books(arguments.titlesearch))
            
        if book_list:
            return self.return_list(book_list, post_text= '\n')
        else:
            return 'no books in the database include the string \'' + arguments.titlesearch + '\' \n'
        
    #Print out the authors and the books they wrote
    def authorsearch_return(self, arguments):
        author_list = self.data_source.authors(arguments.authorsearch)
        output_string = ''
        for a in author_list:
            output_string+= str(a) + ', Books Written:' + str(self.data_source.search_books_by_author(a)) + '\n'
        if output_string:
            return output_string
        else:
            return 'no authors in the database include the string \'' + arguments.authorsearch + '\' \n'
            
    #Print out the books between the given years
    def datesearch_return(self, arguments):
        if arguments.startdate or arguments.enddate:
            books_between_dates = self.data_source.books_between_years(arguments.startdate, arguments.enddate)
            if books_between_dates:
                return self.return_list(books_between_dates, post_text='\n')
            else:
                return 'no books in the database were published between the years ' + str(arguments.startdate) + ' and ' + str(arguments.enddate) + ' inclusive \n '
        else:
            return('error: the command datesearch requires at least one of the tags -s, -e in the form: \npython3 books.py datesearch -s [START YEAR] -e [END YEAR]')
            

    def return_list(self,in_list, pre_text = '', post_text = '' ):
        output_string= ''
        for a in in_list:
            output_string += (str(pre_text) + str(a) + str(post_text))
        return output_string

class BooksInterface():
    
    def __init__(self) -> None:
        self.help_help = 'display '
        self.titlesearch_help = 'python3 books.py titlesearch [SEARCH STRING] (-y) --- search books by title. Use -y to order books by year' 
        self.authorsearch_help = 'python3 books.py authorsearch [SEARCH STRING] --- search for authors and books they have written'
        self.datesearch_help = 'python3 books.py datesearch -s [START YEAR] -e [END YEAR] --- search books by publication date'
        #these aren't shown to the user in this version
        self.date_sort_help = 'sort books by year instead of title'
        self.start_date_help = 'date to start the list with'
        self.end_date_help = 'date to end the list with'

    def get_arguments(self):
        parser = argparse.ArgumentParser('handle books commands')
        subparsers = parser.add_subparsers(description = 'commands')
        
        #Break parsing into subparsers for explicity in code definition
        title_parser = subparsers.add_parser('titlesearch', help = self.titlesearch_help)
        title_parser.add_argument(
            'titlesearch',
            help = self.titlesearch_help,
            default  = '',
            nargs='?',
        )
        #call for date sort
        title_parser.add_argument(
            '-y', '--year',
            help = self.date_sort_help,
            default  = '',
            action='store_true'
        )
        
        #parsing for author search
        author_parser = subparsers.add_parser('authorsearch',help =self.authorsearch_help)
        author_parser.add_argument(
            'authorsearch',
            help = self.authorsearch_help,
            default  = '',
            nargs='?',
        )
        
        #parsing for date search
        date_parser = subparsers.add_parser('datesearch',help = self.datesearch_help)
        date_parser.add_argument(
            'datesearch',
            help = self.datesearch_help,
            default  = '',
            nargs='?',
        )
        #start date parsing
        date_parser.add_argument(
            '-s', '--startdate',
            help = self.start_date_help,
            default = None, 
        )
        #end date parsing
        date_parser.add_argument(
            '-e','--enddate',
            help = self.end_date_help,
            default = None
        )
        
        args = parser.parse_args()
        return args

if __name__ == '__main__':
    book_interface = BooksInterface()
    arguments = book_interface.get_arguments()
    book_search = BooksSearch('books1.csv')
    output = ''
    
    if('titlesearch' in arguments):
        output = book_search.titlesearch_return(arguments)
    elif('authorsearch' in arguments ):
        output = book_search.authorsearch_return(arguments)
    elif('datesearch' in arguments):
        output = book_search.datesearch_return(arguments)
    else:
        raise ValueError('some command must be inputted, please enter one of (titlesearch, datesearch, authorsearch, --help) to continue')
    print(output)
