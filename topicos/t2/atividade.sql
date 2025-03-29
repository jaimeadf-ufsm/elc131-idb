-- 1. Exibir nomes de artistas que contracenaram em filmes. Só deve ser exibido o nome se todos os seus filmes forem anteriores a 1950
SELECT person.person_name FROM person WHERE person.person_id IN (SELECT movie_cast.person_id FROM movie_cast NATURAL JOIN movie GROUP BY movie_cast.person_id HAVING MAX(movie.release_year) < 1950); 
 
-- 2. Exibir a quantidade de atores que contracenaram em mais do que 5 filmes
SELECT COUNT(*) FROM (SELECT 1 FROM movie_cast GROUP BY movie_cast.person_id HAVING COUNT(*) > 5) AS t; 
 
-- 3. Exibir os nomes de personagens que são nomes de filmes.
SELECT movie_cast.character_name FROM movie_cast WHERE movie_cast.character_name IN (SELECT movie.title FROM movie);