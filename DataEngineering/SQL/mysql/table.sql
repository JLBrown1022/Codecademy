


SELECT * FROM table_name, table_name2 WHERE table_name.id = table_name2.id
;
-- 2 Tables are sometimes referred to as relations. Here the table is celebs.

--   A column is a set of data values of a particular type. Here, id, name, and age are the columns.

--   A row is a single record in a table. 
--   The first row in the table might have element values or attributes:
--   * An id
--   * A name
--   * An age

--   All data stored in a relational database is of a certain data type. A 
--   data type is an attribute that specifies the type of data that the object 
--   can hold: integer data, character data, monetary data, date and time data, 
--   binary strings, and so on.
--   Some of the most common data types are:

--   * INTEGER, a positive or negative whole number
--   * TEXT, a text string
--   * DATE, the date formatted as YYYY-MM-DD
--   * REAL, a decimal value

-- 3 A SQL statement is text that the database recognizes as a valid command. 
--   Statements always end in a semicolon ;

-- 3.1 CREATE TABLE is a clause. Clauses perform specific tasks in SQL. Clauses:
--   * are written in capital letters. 
--   * can also be referred to as commands.

-- 3.2 table_name refers to the name of the table that the command is applied to.

-- 3.3 (column_1 data_type, column_2 data_type, column_3 data_type) is a  
--     parameter. A parameter is a list of columns, data_types, or values that  
--     are passed to a clause as an argument
--     *  The parameter is a list of column names and the associated data type

-- 4  CREATE statements allow us to create a new table in the database

--      CREATE TABLE celebs (
--         id INTEGER,
--         name TEXT,
--         age INTEGER
--       )
--      ;

-- 4.1 CREATE TABLE is a Clause that tells SQL you want to create a new table. 
--      The Clause is followed by the name of the table and a list of parameters
-- 4.2 celebs is the name of the table.
-- 4.3 (id INTEGER, name TEXT, age INTEGER) is a list of parameters defining 
--     each column, or attribute in the table and its data type. The parameters 
--     are id, name, and age.
--     * id is the first column in the table. It stores values of data type INTEGER
--     * name is the second column in the table. It stores values of data type TEXT
--     * age is the third column in the table. It stores values of data type INTEGER

-- 5  INSERT INTO is a clause that adds new row or rows to a table

--      INSERT INTO celebs (id, name, age) VALUES (1, 'Justin Bieber', 22)
--      ;

-- 6  SELECT statements are used to fetch data from a database

--      SELECT * FROM celebs
--      ;
-- 7  The ALTER TABLE statement adds a new column to a table. You can use this 
--    command when you want to add columns to a table. The statement below adds 
--    a new column twitter_handle to the celebs table.

--      ALTER TABLE celebs ADD COLUMN twitter_handle TEXT;

-- 8  UPDATE is a clause that changes the values of existing rows in a table

--      UPDATE celebs SET age = 23 WHERE id = 1
--      ;
--      UPDATE data_table 
--      SET column_age = to_this_value 
--      WHERE column_id = is_this_value
--      ;

-- X  The DROP TABLE statement deletes a table and all of its data

--      DROP TABLE celebs
--      ;

-- X  DELETE FROM is a clause that removes rows from a table

--      DELETE FROM celebs WHERE id = 1
--      ;

-- 10 Constraints that add information about how a column can be used are 
--    invoked after specifying the data type for a column. They can be  
--    used to tell the database to collect or reject inserted data that  
--    does not meet certain restriction

--    CREATE TABLE celebs (
--      id INTEGER PRIMARY KEY, 
--      name TEXT UNIQUE,
--      date_of_birth TEXT NOT NULL,
--      date_of_death TEXT DEFAULT 'Not Applicable'
--   )
--   ; 

-- 10.1 PRIMARY KEY columns can be used to uniquely identify the row. 
--      Attempts to insert a row with an identical value will result in a 
--      constraint violation which will not allow you to insert the new row

-- 10.2 UNIQUE columns have a different value for every row. It is similar 
--      to PRIMARY KEY except a table can have many different UNIQUE columns

-- 10.3 NOT NULL columns must have a value. Attempts to insert a row without 
--      a value for a NOT NULL column is a constraint violation and the new 
--      row will not be inserted

-- 10.4 DEFAULT columns take an additional argument that will be the assumed 
--      value for an inserted row if the new row does not specify a value for 
--      that column
