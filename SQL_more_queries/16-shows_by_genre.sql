-- 15-shows_by_genre
-- Returns all shows and all genres linked to that show
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = show_id
LEFT JOIN tv_genres ON tv_genres.id = genre_id
ORDER BY title ASC, name ASC;
