-- 10-genre_id_by_show
-- Returns the TV Shows with at least one genre linked
SELECT title, genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
