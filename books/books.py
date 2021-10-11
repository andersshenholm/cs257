'''
    books.py
    10/2/2021

    Simon Hempel-Costello, Anders Shenholm
    
    TODO: 
    make help print out more readable
    call books methods
    other code review business
    name "args" more specifically
    
'''

import booksdatasource
import argparse

def main():
    args = get_arguments()
    print(args)
    #call_searches() - need to get data source in somewhere
    #this gives space-separated titles as a single string
    #print(' '.join(args.titlesearch))
    #same with authors
    #print(' '.join(args.authorsearch))
    
    
    #data_source = booksdatasource.BooksDataSource(file_string)

def get_arguments():
    title_help = 'Search books by title: python3 books.py titlesearch/ts [SEARCH STRING] [option] --- options: -y'
    author_help = 'Search for authors and books they have written: python3 books.py authorsearch/as [SEARCH STRING]'
    date_help = 'Search books by date: python3 books.py datesearch/ds [START YEAR] [END YEAR]'
    date_sort_help = 'Search books by title, in chronological order: python3 books.py titlesearch/ts [SEARCH STRING] -y'

    parser = argparse.ArgumentParser()
    command_group = parser.add_mutually_exclusive_group(required=True)
    #the reason i'm not setting specific nargs is to allow searches inlcuding spaces
    command_group.add_argument('-ts', '--titlesearch', nargs='*', help = title_help)
    command_group.add_argument('-as', '--authorsearch', nargs='*', default = '', help = author_help)
    #could be nargs = 2, could also not be
    command_group.add_argument('-ds', '--datesearch', nargs='*', type = int, help = date_help)

    sort_group = parser.add_mutually_exclusive_group(required=False)
    sort_group.add_argument('-y', help = date_sort_help, action='store_true') 
    
    args = parser.parse_args()
    if args.y and args.titlesearch == None:
        print ("you can only use the -y tag with the command -ts/--titlesearch")
        return

    return args
#get_arguments is working, just need to call books methods 

'''
#calls booksdatasource.py methods based on which args are present
def call_searches(args):
    if args.titlesearch != None:
        titlesearch_return(args)

#these specific return methods are mostly leftovers from first draft, but I think they can be changed to  work with the new argparse structure.
def titlesearch_return(args):
    search_string = ' '.join(args.titlesearch)
    #if -y is called, sort by date, otherwise sort by title
    if(args.y):
        print(data_source.books(search_string, sort_by='year'))
    else:
        print(self.data_source.books(search_string))

def authorsearch_return(self, arguments):
    #Print out the authors and the books they wrote
    author_list = self.data_source.authors(arguments.authorsearch)
    for a in author_list:
        print(str(a) + " Books Written:" + str(self.data_source.search_books_by_author(a)))
def datesearch_return(self, arguments):
    #Print out the books between the given years
    print(self.data_source.books_between_years(arguments.startdate, arguments.enddate))
main()


def handle_arguments(self, arguments):
    #Each of the three programmed in options, help is built into argsparse for python
    if('titlesearch' in arguments):
        self.titlesearch_return(arguments)
    elif('authorsearch' in arguments):
        self.authorsearch_return(arguments)
    elif('datesearch' in arguments):
        self.datesearch_return(arguments)
    else:
        raise ValueError('some command must be inputted, please enter one of (titlsearch, datesearch, authorsearch, --help) to continue')

if __name__ == '__main__':
    b = Books()
    '''
