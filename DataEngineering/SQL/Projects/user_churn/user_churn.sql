
-- ## Calculating Churn Rates ## --
--0 The dataset provided to you contains one SQL table, subscriptions. 
--  Within the table, there are 4 columns:

--  * id - the subscription id
--  * subscription_start - the start date of the subscription
--  * subscription_end - the end date of the subscription
--  * segment - this identifies which segment the subscription owner belongs to

-- Codeflix requires a minimum subscription length of 31 days, so a user 
-- can never start and end their subscription in the same month

--1 look at the first 100 rows of data in the subscriptions table
SELECT * FROM subscriptions AS subscriptions LIMIT 10

--2 Determine the range of months of data provided. Which 
--  months will you be able to calculate churn for?

SELECT MIN(subscription_start) AS earliest_start,
       MAX(subscription_end) AS latest_end
FROM subscriptions

-- 3 Calculate the churn rate for both segments (87 and 30) over the first 3 
-- months of 2017. To get started, create a temporary table of months.
WITH month AS (
  SELECT '2017-01-01' AS first_day
  UNION
  SELECT '2017-02-01' AS first_day
  UNION
  SELECT '2017-03-01' AS first_day
)

--4 Create a temporary table, cross_join, from subscriptions and your months. 
--  Be sure to SELECT every column
, cross_join AS (
  SELECT *
  FROM subscriptions
  CROSS JOIN month
)

--5 Create a temporary table, status, from the cross_join table you created. 
--  This table should contain:
 
-- * id selected from cross_join
-- * month as an alias of first_day
-- * is_active_87 created using a CASE WHEN to find any users from 
-- * segment 87 who existed prior to the beginning of the month. This is 1 
--   if true and 0 otherwise.
-- * is_active_30 created using a CASE WHEN to find any users from 
-- * segment 30 who existed prior to the beginning of the month. This is 1 
--   if true and 0 otherwise.
, status AS (
  SELECT id,
         month,
         CASE
            WHEN subscription_start <= month THEN 1
            ELSE 0
         END AS is_active_87,
        CASE
            WHEN subscription_start <= month THEN 1
            ELSE 0
         END AS is_active_30
    FROM cross_join












adsa













