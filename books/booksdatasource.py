#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2021

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2021.
'''

import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        #want to parse csv for all info needed for below methods (4 things for each other, 3 for each book)     
        #wrote code not considering having to iterate through lines
        if (books_csv_file_name[0] == '"'):
           progress = books_csv_file_name.index('"')
           title = books_csv_file_name.substring[1,progress]
           print (title)
        else:
           progress = books_csv_file_name.index(',') + 1
           title = books_csv_file_name.substring[0, progress - 1]
	
        print (title)
        #any reason publication_year should be int? 
        publication_year = books_csv_file_name.substring[progress, books_csv_file_name.index(",", progress)]
        progress = books_csv_file_name.index(",", progress)
        #authors
	#author first name
        #author last name
	#author birthdate
	#author deathdate

	#make a book object
        #make an author object	

        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        dave = Author('dave', 'smith')
        #returning obvious filler value to test unit tests
        return [dave, dave, dave, dave, dave, dave, dave, dave, dave]


    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        dave = Author('dave', 'smith')
        authors = [dave, dave, dave, dave, dave, dave, dave, dave]
        test = Book('this is a test book', 2021, authors )
        return [test, test, test, test, test, test, test, test]

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        dave = Author('dave', 'smith')
        authors = [dave, dave, dave, dave, dave, dave, dave, dave]
        test = Book('this is a test book', 2021, authors )
        return [test,test,test,test,test]
  

