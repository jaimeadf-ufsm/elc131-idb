-- 1. Exibir a quantidade de filmes lançados em cada ano. Ordenar o resultado por ano.
SELECT movie.release_year, COUNT(*) FROM movie GROUP BY movie.release_year ORDER BY movie.release_year; 
 
-- 2. Exibir o nome dos filmes que tenham mais do que 20 personagens no elenco.  Mostrar a quantidade de personagens.
SELECT movie.title, COUNT(*) FROM movie JOIN movie_cast ON movie.movie_Id = movie_cast.movie_id GROUP BY movie.movie_Id HAVING COUNT(*) > 20; 
 
-- 3. Para cada ator, mostrar seu nome, e os anos do seu primeiro e do seu último filme lançados
SELECT person.person_name, MIN(movie.release_year), MAX(movie.release_year) FROM person JOIN movie_cast ON person.person_id = movie_cast.person_id JOIN movie ON movie_cast.movie_id = movie.movie_Id GROUP BY person.person_id; 