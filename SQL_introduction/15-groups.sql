-- 15-groups
-- Calculates the number of times a same score appears in the table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;
