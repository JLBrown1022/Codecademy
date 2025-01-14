-- Twitch --

-- 1 Start by getting a feel for the stream table and the 
--  chat table.

--  Select the first 20 rows from each of the two tables.
SELECT *
FROM stream
LIMIT 10
;
SELECT *
FROM chat
LIMIT 10
;
-- 2 What are the unique game names in stream table
SELECT DISTINCT game
FROM stream
;
-- 3 What are the unique channels in the stream table
SELECT DISTINCT channel 
FROM stream
;
-- Aggregate Functions: --

-- 4 What are the most popular games in the stream table?
--   Create a list of games and their number of viewers using 
--   GROUP BY
SELECT game, COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC
;
-- 5 Where are these LoL stream viewers located?
--   Create a list of countries and their number of LoL (League of Legends) viewers 
--   using WHERE and GROUP BY
SELECT country, COUNT(*)
FROM stream
WHERE game IS 'League of Legends'
GROUP BY 1 -- country
ORDER BY 2 DESC -- COUNT(*)
;
-- 6 The player column contains the source (device) the user is using 
--   to view the stream (site, iphone, android, etc).

-- 6.1 Create a list of players (devices) and the number of streamers for each
SELECT player, COUNT(*)
FROM stream
GROUP BY player
ORDER BY COUNT(*) DESC
;
-- 7 Create a new column named 'genre' for each of the games.

--   Group the games into their genres: 
--   * Multiplayer Online Battle Arena (MOBA), 
--   * First Person Shooter (FPS), 
--   * Survival,
--   * Other.

--   Using CASE, your logic should be:
--   * If League of Legends → MOBA
--   * If Dota 2 → MOBA
--   * If Heroes of the Storm → MOBA
--   * If Counter-Strike: Global Offensive → FPS
--   * If DayZ → Survival
--   * If ARK: Survival Evolved → Survival
--   * Else → Other

--   Use GROUP BY and ORDER BY to showcase only the unique 
--   game titles and their respective genres.
SELECT game,
       CASE
           WHEN game IN ('League of Legends', 'Dota 2', 'Heroes of the Storm') THEN 'MOBA'
           WHEN game IS 'Counter-Strike: Global Offensive' THEN 'FPS'
           WHEN game IN ('DayZ', 'ARK: Survival Evolved') THEN 'Survival'
           ELSE 'Other' 
           END AS genre
FROM stream
GROUP BY game, genre DESC
;
-- OR
SELECT game,
 CASE
  WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC
;
-- 9 SQLite comes with a strftime() function - a very powerful function 
--  that allows you to return a formatted date.

--- It takes two arguments: strftime(format, column)

SELECT time,
   strftime('%S', time) -- Returns time's seconds
FROM stream
GROUP BY 1
LIMIT 10
;
-- 10 Write a query that returns two columns:

-- *  The hours of the time column
-- *  The view count for each hour
-- *  Then filter the result with only the users in your 
--    country using a WHERE clause

SELECT strftime('%H', time) AS hour, COUNT(*) AS view_count
FROM stream
WHERE country = 'US'
GROUP BY hour
ORDER BY hour ASC
;
-- 11 The stream table and the chat table share a column: device_id. 
--    Join the two tables on that column
SELECT *
FROM stream AS s
JOIN chat AS c 
ON s.device_id = c.device_id
LIMIT 10
;
SELECT s.time
FROM stream s
JOIN chat c ON s.device_id = c.device_id
LIMIT 10
;





