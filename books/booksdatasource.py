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
    def __str__(self) -> str:
        return self.surname + "," + self.given_name + ",(" +str(self.birth_year) + "-"+ str(self.death_year) +")"
    def __repr__(self) -> str:
        return self.__str__()
    def given_name(self):
        return self.given_name
    def birth_year(self):
        return self.birth_year
    def death_year(self):
        return self.death_year
    def surname(self):
        return self.surname

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

    def __str__(self) -> str:
        return self.title + "," + str(self.publication_year) + "," + str(self.authors)
    def __repr__(self) -> str:
        return self.__str__()
    def title(self):
        return self.title
    def authors(self):
        return self.authors
    def publication_year(self):
        return self.publication_year

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        #want to parse csv for all info needed for below methods (4 things for each other, 3 for each book)     
        #wrote code not considering having to iterate through lines
        #any reason publication_year should be int? 
        # in response to this I think comparison would be easier for date sort, but not necessarily
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
        self.book_list = []
        self.author_list = []
        with open(books_csv_file_name) as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                input_authors = self.parse_authors_from_csv_entry(row[2])
                for a in input_authors:
                    if(a not in self.author_list):
                        self.author_list.append(a)
                input_book = Book(row[0],int(row[1]),input_authors)
                self.book_list.append(input_book)
        pass
    def parse_authors_from_csv_entry(self, input_entry):
        #TODO add comments explaining what on gods green earth is going on here. 
        and_substring = 'and'
        author_list = []
        if and_substring in input_entry:
            and_offset = 4
            pre_and_substring = input_entry[:input_entry.index(and_substring)]
            post_and_substring = input_entry[input_entry.index(and_substring) + and_offset:]
            pre_string_author = self.author_from_string(pre_and_substring)
            author_list.append(pre_string_author)
            if(and_substring in post_and_substring):
                #BROOOOOOOOOOOOO RECURSION AND IT WORKS! RECURSIVE STRING SANITATION!
                author_list.extend(self.parse_authors_from_csv_entry(post_and_substring))
            else:
                post_string_author = self.author_from_string(post_and_substring)
                author_list.append(post_string_author)
        else:
            input_author = self.author_from_string(input_entry)

            author_list.append(input_author)
        return author_list
    def author_from_string(self, input_string):
        author  = Author(input_string[input_string.index(" ")+1:input_string.index("(")-1], input_string[:input_string.index(" ")], (input_string[input_string.index("(")+1 : input_string.index("-")]), (input_string[input_string.index("-")+1 : input_string.index(")")]))
        return author



    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        output_list = []
        input_text = search_text.lower()
        for a in self.author_list:
            last_name = a.surname.lower()
            first_name = a.given_name.lower()
            if(input_text in last_name or input_text in first_name):
                output_list.append(a)
        output_list = sorted(output_list, key = Author.given_name)
        output_list = sorted(output_list, key = Author.surname)
        return output_list

        pass


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
        input_text = search_text.lower()
        output_list = []
        for b in self.book_list:
            title = b.title.lower()
            if(input_text in title):
                output_list.append(b)
        if(sort_by == "year"):
            output_list = sorted(output_list, key = Book.publication_year)
        else:
            output_list = sorted(output_list, key = Book.title)
        return output_list    
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
        end_date = 2400 #random future year
        start_date = 0
        if(end_year != None):
            end_date = int(end_year)
        if(start_year != None):
            start_date = int(start_year)
        output_list = []
        for b in self.book_list:
            if(b.publication_year>= start_date and b.publication_year <= end_date):
                output_list.append(b)
        #TODO verify that this not only seems to work but actually works, done with test2.csv, but further tests would be appreciated
        output_list = sorted(output_list, key = Book.title)
        output_list = sorted(output_list, key=Book.publication_year)
        
                
        return output_list

    def all_books(self):
        return self.book_list
    def all_authors(self):
        return self.author_list

