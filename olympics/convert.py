#Anders Shenholm 10/14/21
#this program converts csv data from the olympics database to csv files used by my pqsl database
import csv

#tests confirm season is redundant
#tests confirm year is redundant (for this database), though consider tokyo 2020 happening in 2021


def main():
    fill_teams()
    fill_athletes_events_tables()
    

def fill_teams():
    teams_file = open('teams.csv', 'w');
    with open('noc_regions.csv', newline='') as file:
        teams_reader = csv.reader(file)
        teams_writer = csv.writer(teams_file)
        teams_id = 0
        
        teams_reader.__next__()

        #filling teams.csv (noc, region, notes)
        for row in teams_reader:
            teams_writer.writerow([teams_id, row[0], row[1], row[2]])
            teams_id += 1
        

def fill_athletes_events_tables():
    
    athletes_file = open('athletes.csv', 'w');
    results_file = open('results.csv', 'w');
    athletes_results_file = open('athletes_results.csv', 'w');
    games_file = open('games.csv', 'w');
    events_file = open('events.csv', 'w');
    
    athletes_writer = csv.writer(athletes_file)
    results_writer = csv.writer(results_file)
    athletes_results_writer = csv.writer(athletes_results_file)
    games_writer = csv.writer(games_file)
    events_writer = csv.writer(events_file)
        
    athletes_array = []
    games_array = []
    events_array = []

    #ids for each item. These are set to negative one so that iteration happens immediately after the program confirms a new entry
    athletes_id = -1
    results_id = -1
    games_id = -1
    events_id = -1
    
    
    with open('athlete_events.csv', newline='') as file: 
        
        reader = csv.reader(file)
        #skips reader ahead to avoid header
        reader.__next__()

        for row in reader: 
            #filling athletes.csv (name, sex, age, height, weight, team, noc, games)
            if str(row[1]+row[8]) not in athletes_array:
                athletes_id +=1
                athletes_writer.writerow([athletes_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
                athletes_array.append(str(row[1]+row[8]))
                
               
            #filling results.csv (name, games, event, medal)  
            results_id+=1
            results_writer.writerow([results_id, row[1], row[8], row[13], row[14]])
            
            
            #filling athletes_results.csv(results_id, athletes_id)
            athletes_results_writer.writerow([results_id, athletes_id])
            
            #filling games.csv (games, year, season, city)
            if str(row[8]) not in games_array:
                games_id+=1
                games_writer.writerow([games_id, row[8], row[9], row[10], row[11]])
                games_array.append(str(row[8]))
                
            #filling events.csv (sport, event)
            if str(row[13]) not in events_array:
                events_id+=1
                events_writer.writerow([events_id, row[12], row[13]])
                events_array.append(str(row[13]))
            
            
            
main()
