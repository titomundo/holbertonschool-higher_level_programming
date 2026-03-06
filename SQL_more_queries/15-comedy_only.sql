-- 15-comedy_only
-- Returns all shows related to a genre
SELECT title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = show_id
INNER JOIN tv_genres ON tv_genres.id = genre_id
WHERE name = 'Comedy'
ORDER BY title ASC;
