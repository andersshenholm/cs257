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

2 things:
1) This query lists total medals awarded to athletes of an noc (ex. If a team of 4 wins a relay race, their noc's gold medal count increases by 4)
2) This query assumes that every noc has either won a gold medal (WHERE results.medal = 'Gold') or has for at least one event not won a medal ("OR results.medal IS NULL"). It works properly for this dataset. However, if a new noc comes on the scene and only wins silver and bronze, they won't be listed with other 0-time gold medal winners.
*/


SELECT COUNT (results.medal), results.noc 
FROM results
WHERE results.medal = 'Gold'
OR results.medal IS NULL
GROUP BY results.noc
ORDER BY COUNT(results.medal) DESC;

