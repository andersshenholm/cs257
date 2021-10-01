import booksdatasource
<<<<<<< HEAD
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
=======
#from what I can tell this is the best option for processing cli arguments
import sys

def parse_args():
    args = sys.argv
    
    if args exactly 2 in length and one arg asks for help, 
        print_usage()
        return
    

    
    authorsearch, titlesearch, datesearch = None, None, None

    commandcount = 0
    if 'titlesearch' in args:
            commandcount+=1
    if 'ts' in args:
            commandcount+=1
    if 'authorsearch' in args:
            commandcount+=1
    if 'as' in args:
            commandcount+=1
    if 'datesearch' in args:
            commandcount+=1
    if 'ds' in args:
            commandcount+=1
    print(commandcount)
    if commandcount != 1:
        print("The books program accepts exactly one command argument. Access the usage document with -h, --help")
       
                  
parse_args()

def print_usage():
     with open("usage.txt") as f:
        print (f.read())



#print(args)
#print("Argument List:", str(sys.argv))
>>>>>>> c86656bb8a2fd2bb1e23a7aba1688e2a5367a4e6
