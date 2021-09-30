import booksdatasource
#from what I can tell this is the best option for processing cli arguments
import argparser

parser = argparse.ArgumentParser(description='Process booksdatasource requests')
parser.add_argument('authorsearch', 'as', help='searches by author')
parser.add_argument('titlesearch', 'ts', help='searches by title')
parser.add_argument('datesearch', 'ds', help='searches by date')
parser.add_argument('-t', '--sorttitle', help='sorts books by title')
parser.add_argument('-d', '--sortdate', help='sorts books by date')

args = parser.parse_args()

def as(search_string):
    searched_authors[] = booksdatasource.authors 
    return_string = ""
    for each_author in authorlist:
        if each_author in booksdatasource.authors(search_string)
        return_string += each_author
        #here we need to get books written by some author. Parse from csv doc or is this somehow attached to authors in booksdatasource?

authorsearch = as

def