'''
convert.py - This program converts csv data from the olympics database to csv files used by my pqsl database

Anders Shenholm 10/21/21
'''
import csv

def main():
    fill_nocs()
    fill_athletes_events_tables()
    
#taking all required data from noc_regions.csv
def fill_nocs():
    nocs_file = open('nocs.csv', 'w');
    with open('noc_regions.csv', newline='') as file:
        nocs_reader = csv.reader(file)
        nocs_writer = csv.writer(nocs_file)
        
        nocs_reader.__next__()

        #filling nocs.csv (noc, region, notes)
        for row in nocs_reader:
            nocs_writer.writerow([row[0], row[1], row[2]])
        
    nocs_file.close()
    
#taking all required data from athletes_events.csv    
def fill_athletes_events_tables():
    
    athletes_file = open('athletes.csv', 'w');
    results_file = open('results.csv', 'w');
    games_file = open('games.csv', 'w');
    events_file = open('events.csv', 'w');
    
    athletes_writer = csv.writer(athletes_file)
    results_writer = csv.writer(results_file)
    games_writer = csv.writer(games_file)
    events_writer = csv.writer(events_file)
        
    athletes_dict = {}
    games_dict = {}
    events_dict = {}

    #ids for athletes and results csv rows. These are set to negative one so that iteration happens each time the program confirms a new entry
    athletes_id = -1
    results_id = -1

    with open('athlete_events.csv', newline='') as file: 
        
        reader = csv.reader(file)
        
        #skips reader ahead to avoid header
        reader.__next__()

        for row in reader: 
            
            #checking that athletes are unique. An athlete in this database is an instance of one person at one games. (a competitor has as many entries in athletes.csv as games they've competed in)
            if str(row[1]+row[8]) not in athletes_dict:
                athletes_id +=1
                #filling athletes.csv (id, name, sex, age, height, weight, team, noc, games)
                athletes_writer.writerow([athletes_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
                athletes_dict[str(row[1]+row[8])] = 0

            
            #filling games.csv (games, year, season, city)
            if str(row[8]) not in games_dict:
                games_writer.writerow([row[8], row[9], row[10], row[11]])
                games_dict[str(row[8])] = 0
                
            #filling events.csv (event, sport)
            if str(row[13]) not in events_dict:
                events_writer.writerow([row[13], row[12]])
                events_dict[str(row[13])] = 0
                
            #filling results.csv (id, athlete_id, noc, games, event, medal)
            results_id+=1
            results_writer.writerow([results_id, athletes_id, row[7], row[8], row[13], row[14]])
            
    athletes_file.close()
    results_file.close()
    games_file.close()
    events_file.close()
            
main()
