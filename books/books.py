import booksdatasource
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