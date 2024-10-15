SELECT name FROM people
JOIN stars ON people.id = stars.person_id
WHERE NOT name="Kevin Bacon" AND movie_id IN (SELECT movies.id FROM movies
JOIN stars ON movies.id=stars.movie_id
JOIN people ON stars.person_id=people.id
WHERE person_id =
(SELECT people.id FROM people WHERE people.name = "Kevin Bacon" AND people.birth = "1958"));
