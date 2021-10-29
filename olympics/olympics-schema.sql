/*
Anders Shenholm 10/14/21
here is where I store sql commands for processing olympics data
The database design assumes that an athletes height, weight, sex, age, team, and noc can change between different games. 

Setting up database:
*/
CREATE TABLE nocs (
    id integer,
    noc text,
    region text,
    notes text
);

CREATE TABLE events (
    id integer,
    event text,
    sport text
);

CREATE TABLE games (
    id integer,
    games text,
    year integer,
    season text,
    city text
);

CREATE TABLE athletes (
    id integer,
    name text,
    sex text,
    age integer,
    height float,
    weight float,
    team text, 
    noc text,
    games text
);


CREATE TABLE results (
    id integer,
    athlete_id integer,
    noc text,
    games text,
    event text,
    medal text
    
);



/*
next

\copy athletes FROM 'athletes.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy events FROM 'events.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy games FROM 'games.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy results FROM 'results.csv' DELIMITER ',' CSV NULL AS 'NA'
\copy nocs FROM 'nocs.csv' DELIMITER ',' CSV NULL AS 'NA'

