SELECT title FROM movies
JOIN ratings ON movies.id = ratings.movie_id
JOIN stars ON movies.id = stars.movie_id
WHERE person_id = (SELECT id FROM people WHERE name = "Chadwick Boseman")
ORDER BY rating DESC
LIMIT 5;
