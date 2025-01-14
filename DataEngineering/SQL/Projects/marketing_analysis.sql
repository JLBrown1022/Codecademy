-- Marketing Analysis --
WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT ft.user_id,
    ft.first_touch_at,
    pv.utm_source,
		pv.utm_campaign
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp;

--1 How many campaigns and sources does CoolTShirts use? 
-- Which source is used for each campaign?

-- Use three queries:

-- * one for the number of distinct campaigns,
-- * one for the number of distinct sources,
-- * one to find how they are related

-- Number of distinct campaigns
SELECT COUNT(DISTINCT campaigns) AS distinct_campaigns
FROM page_visits
;
-- Number of distinct sources
SELECT 
COUNT(DISTINCT utm_source) AS utm_counts
FROM page_visits
;
-- Relationship between campaigns and sources
SELECT campaigns, utm_source, COUNT(*) AS frequency
FROM page_visits
GROUP BY campaigns, utm_source
ORDER BY frequency DESC
LIMIT 10
;
-- 2 Find the distinct values of the page_name column
--   and display the count for each page name.
SELECT page_name, COUNT(*) as page_count
FROM page_visits
GROUP BY page_name
ORDER BY page_count DESC
LIMIT 10
;
-- 3 How many first touches is each campaign responsible for?
-- 3 How many first touches is each campaign responsible for?
WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT pv.campaigns,
    COUNT(*) AS first_touch_count
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id 
    AND ft.first_touch_at = pv.timestamp
    AND pv.page_name = 'home'
    AND pv.campaigns IN (
        SELECT campaigns
        FROM page_visits
        WHERE page_name = 'home'
        GROUP BY campaigns
    )
GROUP BY pv.campaigns
ORDER BY first_touch_count DESC
-- LIMIT 10
;
-- 4 How many last touches is each campaign responsible for?

--   * identify the campaigns responsible for each last touch
--   * display the count of last touches for each campaign.
WITH last_touch AS (
    SELECT user_id,
        MAX(timestamp) as last_touch_at
    FROM page_visits
    GROUP BY user_id)
    SELECT pv.campaigns,
        COUNT(*) AS last_touch_count
    FROM last_touch lt
    JOIN page_visits pv
        ON lt.user_id = pv.user_id
        AND lt.last_touch_at = pv.timestamp
        AND pv.page_name = 'purchase'
        AND pv.campaigns IN (
            SELECT campaigns
            FROM page_visits
            WHERE page_name = 'purchase'
            GROUP BY campaigns
        )
        GROUP BY pv.campaigns
        ORDER BY last_touch_count DESC
        -- LIMIT 10
;
-- 5 To find how many visitors make a purchase count the 
--   distinct users who visited the page named 4 - purchase
SELECT COUNT(DISTINCT user_id) AS purchase_count
FROM page_visits
WHERE page_name = '4 - purchase'
;
-- 6 How many last touches on the purchase page is 
--   each campaign responsible for?

WITH last_touch AS (
    SELECT user_id,
        MAX(timestamp) as last_touch_at
    FROM page_visits
    GROUP BY user_id)
    SELECT pv.campaigns,
        COUNT(*) AS last_touch_count
    FROM last_touch lt
    JOIN page_visits pv
        ON lt.user_id = pv.user_id
        AND lt.last_touch_at = pv.timestamp
        AND pv.page_name = '4 - purchase'
        AND pv.campaigns IN (
            SELECT campaigns
            FROM page_visits
            WHERE page_name = '4 - purchase'
            GROUP BY campaigns
        )
        GROUP BY pv.campaigns
        ORDER BY last_touch_count DESC
        -- LIMIT 10
;
-- 7 Given your findings, which are the five best campaigns
--   to re-invest and why?
--   * identify the five best campaigns based on the number of last touches
--   * explain the reasons behind the best campaigns.

WITH last_touch AS (
    SELECT user_id,
        MAX(timestamp) as last_touch_at
    FROM page_visits
    GROUP BY user_id)
    SELECT pv.campaigns,
        COUNT(*) AS last_touch_count
    FROM last_touch lt
    JOIN page_visits pv
        ON lt.user_id = pv.user_id
        AND lt.last_touch_at = pv.timestamp
        AND pv.page_name = '4 - purchase'
        AND pv.campaigns IN (
            SELECT campaigns
            FROM page_visits
            WHERE page_name = '4 - purchase'
            GROUP BY campaigns
        )
        GROUP BY pv.campaigns
        ORDER BY last_touch_count DESC
        LIMIT 5
;
