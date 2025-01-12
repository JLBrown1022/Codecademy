--1 What is the March churn rate as a ratio?
--  Use a SELECT statement to calculate the answer
Select 100./2000

--2 CodeFlix started with 3,000 customers. During the 
--  month, 450 of these customers canceled
Select 450./3000

--1 We’ve imported 4 months of data for a company from when they began selling subscriptions. This company has a minimum commitment of 1 month, so there are no cancellations in the first month.

-- The subscriptions table contains:
    -- * id
    -- * subscription_start
    -- * subscription_end

-- Use the methodology provided in the narrative to calculate the churn for January 2017.

--Select * From subscriptions Limit 10
Select 1.0 *
(
    Select Count(*)
    From subscriptions
    Where subscription_start < '2017-01-01'
    And
    (
    subscription_end
    Between '2017-01-01' 
    And '2017-01-31'
    )
) / (
    Select Count(*)
    From subscriptions
    Where subscription_start < '2017-01-01'
    And
    (
    (subscription_end >= '2017-01-01')
    or
    (subscription_end Is NULL)
    )
)
As result;

--3.1 calculate the churn for January 2017
--    using WITH and CASE

With enrollments As (
  Select *
  From subscriptions
  Where subscription_start < '2017-01-01'
  And (
    (subscription_end >= '2017-01-01')
    Or
    (subscription_end Is NULL)
  )
),
status As (
  Select
    Case
      When 
        (subscription_end > '2017-01-31')
        Or
        (subscription_end Is NULL)
      Then 0
      Else 1
    End As is_canceled,
    Case
      When
        subscription_start < '2017-01-01'
      And (
        (subscription_end >= '2017-01-01')
        Or
        (subscription_end Is NULL)
      )
      Then 1
      Else 0
    End as is_active
  From enrollments
)
Select 1.0 * 
  Sum(is_canceled)/Sum(is_active)
From status;

-- Some SQL table schemes will contain a prebuilt table of months. 
-- Ours doesn’t, so we’ll need to build it using UNION
-- We’ll need the first and last day of each month

--4.1 Create the months temporary table using WITH and SELECT 
--    everything from it to see the structure
WITH months AS (
SELECT 
  '2017-01-01' As first_day,
  '2017-01-31' As last_day
UNION
Select
  '2017-02-01' As first_day,
  '2017-02-28' As last_day
Union
Select
  '2017-03-01' As first_day,
  '2017-03-31' As last_day
)
Select * From months;

-- The pattern for creating a temporary table using a CROSS JOIN is:
desired_temp_table AS
(SELECT *
FROM table1
CROSS JOIN table2)

--5.1 Create a cross_join temporary table that is a 
--    CROSS JOIN of subscriptions and months.

-- The pattern for creating a temporary table using 
-- a CROSS JOIN is:

cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),

--6 * Determine Active Status * --
--6.1 Add a status temporary table. This table should have the following 
--    columns:

  -- * id - selected from the cross_join table
  -- * month - this is an alias of first_day from the 
  --   cross_join table. Use the first day of the month 
  --   to represent the month of the data.
  -- * is_active - 0 or 1, derive this column using a 
  --   CASE WHEN statement

-- The is_active column should be 1 if the 
-- subscription_start is before the month’s first_day 
-- and if the subscription_end is either after the 
-- month’s first_day or is NULL.

status AS (
  Select id, first_day AS month,
    CASE 
      WHEN subscription_start < first_day 
      AND (
        subscription_end >= first_day 
        OR
        subscription_end IS NULL
      )
      THEN 1
      ELSE 0
    END AS is_active
    ---7 * Multiple Month: Determine Cancellation Status
    --   We need to add is_canceled to status table
    --   This column will be 1 only during the month 
    --   the user cancels. 

    --7.1 Add an is_canceled column to the status temporary 
    --    table. Ensure that it is equal to 1 in months 
    --    containing the subscription_end and 0 otherwise.

    --    Derive this column using a CASE WHEN statement. 
    --    You can use the BETWEEN function to check if a 
    --    date falls between two others
    CASE 
      WHEN (subscription_end BETWEEN first_day AND last_day)
      THEN 1
      ELSE 0
    END AS is_canceled,
  FROM cross_join
),
--8 * Multiple Month: Sum Active and Canceled Users
--    With the active and canceled status for each
--    subscription for each month, we can aggregate 
--    them.
--    We will GROUP BY month and create a SUM() of 
--    the two columns from the status table, is_active 
--    and is_canceled

--8.1 Add a status_aggregate temporary table. This  
--    table should have the following columns:
--    * month - this is an alias of first_day from the 
--      cross_join table. Use the first day of the month
--      to represent the month of the data.
--    * active_users - this is the SUM() of is_active 
--      for each month.
--    * canceled_users - this is the SUM() of is_canceled
--      for each month.
--    * churn_rate - this is the calculation of 
--      (canceled_users / active_users) * 100 for each 
--      month.
--    You can use the AVG() function to calculate the 
--    average churn rate.
status_aggregate AS (
  Select month,
Sum(is_active) AS active_users,
    Sum(is_canceled) AS canceled_users,
    100.0 * Sum(is_canceled) / Sum(is_active) AS churn_rate
  From status
  Group By month
)
--9 * Multiple Month: Calculate Churn Rate
--    With the status_aggregate table, we can calculate 
--    the churn rate for each month.
--9.1 Add a SELECT statement to calculate the churn rate. The 
--    result should contain two columns
--    * month  - selected from the status_aggregate table
--    * churn_rate - calculated from the status_aggregate table
--      using status_aggregate.canceled and status_aggregate.active
--    * You can use the AVG() function to calculate the 
--      average churn rate.
Select month, 1.0 * canceled_users/active_users AS churn_rate
From status_aggregate;
-- SELECT * FROM cross_join LIMIT 10;
-- SELECT * FROM status_aggregate;



