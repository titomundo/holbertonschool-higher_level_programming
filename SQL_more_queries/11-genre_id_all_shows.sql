-- 11-genre_id_all_shows
-- Returns all the shows with the genre_id
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
