-- 13-count_shows_by_genre
-- Lists all the genres in the database with the total of shows linked to that genre
SELECT name as genre, COUNT(id) as number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON id = genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
