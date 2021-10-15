/*
Anders Shenholm 10/14/21
here is where I store sql commands for processing olympics data
The database design assumes that an athletes height, weight, sex, age, team, and noc can change between different games. 


Setting up database:

CREATE TABLE teams (
    id integer,
    noc text,
    team text,
    notes text
);

CREATE TABLE events (
    id integer,
    sport text,
    event text
);

CREATE TABLE games (
    id integer,
    games text,
    year text,
    season text,
    city text
);

CREATE TABLE athletes (
    id integer,
    name text,
    sex text,
    age text,
    height text,
    weight text,
    team text, 
    noc text,
    games text
);


CREATE TABLE results (
    id integer,
    name text,
    games text,
    event text,
    medal text
    
);

CREATE TABLE athletes_results (
    results_id integer,
    athletes_id integer

);

then

\copy athletes FROM 'athletes.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy events FROM 'events.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy games FROM 'games.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy athletes_results FROM 'athletes_results.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy results FROM 'results.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy teams FROM 'teams.csv' DELIMITER ',' CSV NULL AS 'NA'


Specific Queries:

List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. These entities, by the way, are mostly equivalent to countries. But in some cases, you might find that a portion of a country participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation.

SELECT teams.noc
FROM teams
ORDER BY teams.noc;


List the names of all the athletes from Kenya. If your database design allows it, sort the athletes by last name.

SELECT DISTINCT athletes.id, athletes.name 
FROM athletes
WHERE athletes.noc='KEN'
ORDER BY athletes.id;


List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.

SELECT results.name, results.games, results.event, results.medal
FROM results
WHERE results.name = 'Gregory Efthimios "Greg" Louganis' 
AND (medal = 'Gold' OR medal = 'Silver' OR medal = 'Bronze')
ORDER BY results.games;

List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
result has an athlete - athlete has a noc


------WORK IN PROGRESS----------

SELECT teams.noc, 
FROM teams, results, athletes
ORDER BY teams.noc;

WHERE results.medal = 'Gold'
AND results.name
search results
IF medal = 'Gold' 
    important name = name
    important games = games
    
search athletes:
if important name = name
   and important games = games


*/