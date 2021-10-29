#!/usr/bin/env python3
'''
    olympics-api.py
    Anders Shenholm 
    28 October 2021

    This is a simple API for accessing my olympics database
    
    TODO:
    1. could improve by giving print outs if an argument doesnt correspond to any games or noc
    
'''
import sys
import argparse
import flask
import json
import psycopg2
import config

app = flask.Flask(__name__)

#opens connection to the olympics database
def connect_to_olympics():
    try:
        connection = psycopg2.connect(database=config.database, user=config.user, password=config.password)
    except Exception as e:
        print(e)
        exit()
    return connection

    
@app.route('/')
def hello():
    return "Hi, welcome to my API. You can use the extensions /nocs, /games, /medalists/games/{games_id}, and /help "
     
    
@app.route('/nocs')
def get_nocs():
    ''' returns a JSON list of dictionaries, each of which represents one
     National Olympic Committee, alphabetized by NOC abbreviation. 
     Each dictionary will have data for noc abbreviation and noc name
    '''
    #taking data
    connection = connect_to_olympics()
    try: 
        cursor = connection.cursor()
        query = ('''SELECT nocs.noc, nocs.region
        FROM nocs''')
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    
    #formatting data
    nocs_list = []
    for row in cursor:
        nocs_list.append({'noc': row[0], 'name': row[1]})

    connection.close()
    nocs_list = sorted(nocs_list, key=lambda x: x['noc'])
    return json.dumps(nocs_list)
    
    
  
@app.route('/games')
def get_games():
    ''' a JSON list of dictionaries, each of which represents one
    Olympic games, sorted by year. Each dictionary will have data for id, year, season, and city
    '''
    #taking data
    connection = connect_to_olympics()
    try: 
        cursor = connection.cursor()
        query = ('''SELECT games.id, games.year, games.season, games.city 
        FROM games''')
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    
    
    #formatting data
    games_list = []
    for row in cursor:
        games_list.append({'id': row[0], 'year': row[1], 'season': row[2], 'city': row[3]})
        
    connection.close()
    games_list = sorted(games_list, key=lambda x: x['year'])
    return json.dumps(games_list)


@app.route('/medalists/games/<games_id>')
def get_medalists(games_id):
    '''
        returns a JSON list of dictionaries, each representing one athlete
        who earned a medal in the specified games. Each dictionary entry includes data on  athlete_id, athlete_name, athlete_sex, sport, event, and medal.
        
        Note: Athlete id's in my database are assigned to each instance of an 
        athlete at a games, so athletes who have competed at multiple games have that many id's
    '''
    #collecting optional noc parameter
    noc = flask.request.args.get('noc')
    
    #other steps
    connection = connect_to_olympics()
    medalists_list = []
    games_search_string = "'" + games_id + "'"
    
    #searching with optional noc argument
    if noc:
        noc_search_string = "'" + noc.upper() + "'"
        try: 
            cursor = connection.cursor()
            #first 6 values are for printout, next 3 are for searching by games, last is for searching by athlete noc
            query = ('''SELECT athletes.id, athletes.name, athletes.sex, events.sport, results.event, results.medal, games.id, games.games, athletes.games, athletes.noc
            FROM athletes, results, events, games
            WHERE athletes.id = results.athlete_id
            AND results.event = events.event
            AND results.medal IS NOT NULL
            AND games.id = %s
            AND games.games = athletes.games
            AND athletes.noc = %s
            ''' % (games_search_string, noc_search_string))
            cursor.execute(query)
        except Exception as e:
            print(e)
            exit()
            
    #searching without noc argument - almost identical       
    else:
        try: 
            cursor = connection.cursor()
            #first 6 values are for printout, next 3 are for searching by games
            query = ('''SELECT athletes.id, athletes.name, athletes.sex, events.sport, results.event, results.medal, games.id, games.games, athletes.games, athletes.noc
            FROM athletes, results, events, games
            WHERE athletes.id = results.athlete_id
            AND results.event = events.event
            AND results.medal IS NOT NULL
            AND games.id = %s
            AND games.games = athletes.games
            ''' % games_search_string)
            cursor.execute(query)
        except Exception as e:
            print(e)
            exit()
        
    
    #making list to be returned
    for row in cursor:
        medalists_list.append({'athlete_id': row[0], 'athlete_name': row[1], 'athlete_sex': row[2], 'sport': row[3], 'event': row[4], 'medal': row[5]})

    connection.close()
    
    return json.dumps(medalists_list)


@app.route('/help')
def get_help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    #all this code runs the api where the user specifies
    parser = argparse.ArgumentParser('A flask API for accessing my olympics database')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
    
