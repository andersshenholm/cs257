/*
Specific Queries:

List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. These entities, by the way, are mostly equivalent to countries. But in some cases, you might find that a portion of a country participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation.

*/
SELECT nocs.noc
FROM nocs
ORDER BY nocs.noc;

/*
List the names of all the athletes from Kenya. If your database design allows it, sort the athletes by last name.
*/

SELECT DISTINCT athletes.name
FROM athletes
WHERE athletes.noc='KEN';

/*
List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.
*/

SELECT athletes.name, results.games, results.event, results.medal
FROM results, athletes
WHERE results.athlete_id = athletes.id
AND athletes.name = 'Gregory Efthimios "Greg" Louganis' 
AND (medal = 'Gold' OR medal = 'Silver' OR medal = 'Bronze')
ORDER BY results.games;

/*
List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.


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
