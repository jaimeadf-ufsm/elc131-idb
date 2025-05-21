SELECT COUNT(*) FROM movie;

SELECT COUNT(*) FROM person;

SELECT COUNT(*) FROM movie_cast;

SELECT COUNT(DISTINCT release_year) FROM movie;

SELECT MIN(release_year) FROM movie;

SELECT MAX(release_year) FROM movie;

SELECT COUNT(DISTINCT cast_order) FROM movie_cast;


SELECT * FROM movie CROSS JOIN person;

SELECT * FROM movie NATURAL JOIN movie_cast
WHERE cast_order = 1 AND release_year > 2000;

SELECT * FROM movie JOIN movie_cast USING (movie_id)
JOIN person USING (person_id)
WHERE cast_order = 1 AND (release_year = 1990 OR release_year = 2000);

SELECT title FROM movie UNION ALL
SELECT character_name FROM movie_cast

SELECT title FROM movie EXCEPT
SELECT character_name FROM movie_cast;