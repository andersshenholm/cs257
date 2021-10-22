'''
olympics.py
This is a command line program that allows users to search the olympics database with a few specific queries

Anders Shenholm 10/21/21


'''

import argparse
import psycopg2
import config

#TODO: 
#close connections, cursors, all that
#add comments/organize code


def get_args():
    parser_description = "this object parses command line arguments for the olympics database search"
    athletes_help = "Search for all athletes in an NOC using an NOC as search team"
    ranknocs_help = "Return a list of all NOC's ordered by gold medal count, descending"
    medals_help = "Search for all medals won by an athlete, using athlete name as a search team"
    
    parser = argparse.ArgumentParser(description=parser_description)
    
    #this parser allows one of the three below arguments
    search_commands = parser.add_mutually_exclusive_group(required=True)
    search_commands.add_argument('-m', '--medals', metavar = 'STRING', nargs='*', type=str, help=medals_help)
    search_commands.add_argument('-a', '--athletes', metavar = 'STRING', nargs=1, help=athletes_help)
    search_commands.add_argument('-r', '--ranknocs', action='store_true', help=ranknocs_help)
    
    args = parser.parse_args()
    return args

#implementing the athletes method (search athletes by noc name)
def athletes(connection, args):
    try: 
        search_string = "'" + args.athletes[0] + "'"
        cursor = connection.cursor()
        query = ('''SELECT DISTINCT athletes.name
        FROM athletes 
        WHERE athletes.noc ILIKE %s;''' % search_string)
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    if cursor.rowcount != 0:
        for row in cursor:
            print(row[0])
    else:
        print("There is no noc in the database that matches that input. \nUsage: python3 olympics.py -a STRING")
    
    print()
 
 #implementing the medals method (search medals by athlete name)
 #this method could be improved by allowing separate ordered strings (i.e. the database recognizes -m michael fred phelps, but not -m michael phelps. This would be an issue for most users)
def medals(connection, args):
    try:
        
        #search_string is formatted so that any athlete whose name contains the search string will be included
        search_string = "'%" + ' '.join(args.medals) + "%'"
        cursor = connection.cursor()

        query = ('''SELECT athletes.name, results.games, results.event, results.medal 
        FROM results, athletes 
        WHERE athletes.name ILIKE %s 
        AND athletes.id = results.athlete_id
        AND (medal = 'Gold' OR medal = 'Silver' OR medal = 'Bronze') 
        ORDER BY results.games; ''' % search_string)
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
        
    if cursor.rowcount != 0:
        for row in cursor:
            print(row[0] + " | " + row[1] + " | " + row[2] + " | " + row[3])
    else:
        print("There is no athlete in the database that matches that input. \nUsage: python3 olympics.py -m STRING")
    
    print()
    
#implementing the ranknocs method (return noc, gold medal count in order of gold medal count)
def ranknocs(connection):
    try:
        gold_collector = connection.cursor()
        gold_query = '''SELECT results.noc, results.games, results.event
        FROM results
        WHERE results.medal = 'Gold'
        '''

        noc_collector = connection.cursor()
        #The nocs should all be listed in the nocs_regions file, but they're not (i.e. SGP is in athletes_events but not nocs_regions). That's why we use the results table to collect nocs. 
        noc_query = '''SELECT DISTINCT results.noc
        FROM results
        '''

        gold_collector.execute(gold_query)
        noc_collector.execute(noc_query)
        
    except Exception as e:
        print(e)
        exit()
        
    
    event_winners = {}
    nocs = {}

    for row in gold_collector:
        if row[1]+row[2] not in event_winners:
            event_winners[row[1]+row[2]] = row[0] 
            #labels each unique event with the name of the winning noc

    
    for row in noc_collector:
        nocs[row[0]] = 0
        #fills the dictionary with all nocs
    
    for event in event_winners:
        nocs[event_winners[event]] += 1
        #adds to an noc's gold medal tally for each event they won
    
    #everything below this point is done to format the output
    
    print_list = []
    
    for item in nocs:
        print_list.append(item + ": " + str(nocs[item]))
    
    #sorting by medal count - we assume noc's contain 3 characters
    print_list = sorted(print_list, key=lambda x: int(x[5:]), reverse=True)
    for item in print_list:
        print(item)

    
def main():
    #opening connection to the olympics database
    try:
        connection = psycopg2.connect(database=config.database, user=config.user, password=config.password)
    except Exception as e:
        print(e)
        exit()
    
    args = get_args()
    
    #calling appropriate methods
    if args.medals:
        medals(connection, args)
    if args.ranknocs == True:
        ranknocs(connection)
    if args.athletes:
        athletes(connection, args)
    
main()