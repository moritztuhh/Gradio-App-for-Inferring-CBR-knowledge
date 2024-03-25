'''
Before using the code, please make sure that you have a local instance of MySqlServer is running.
Maybe the connection part has to be adjusted depending on the Server

This file contains useful functions to work with the data

The Server should have a Database named CaseDB
'''
import mysql.connector
from mysql.connector.cursor import MySQLCursor
import logging

logging.getLogger().setLevel(logging.INFO)

# Returns a connection to local instance of MySQL Server (Must be called)
def createDB():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="test1234",
        database = "CaseDB"
    )
    logging.info(msg="Successfully Connected")
    return mydb

# Creates table named words where all words from data.txt are saved
def createTable(cursor : MySQLCursor):
    query = "CREATE TABLE IF NOT EXISTS words (nominative VARCHAR(255), inessive VARCHAR(255), word_type INT);"
    cursor.execute(query)

    logging.info(msg="Successfully Created Table")

    mydb.commit()

# Fills words with content from data.txt (must only be called ones)
def fillDB(filename, cursor : MySQLCursor):
    cursor.execute("USE CaseDB")
    with open(filename, 'r') as file:
        for line in file:
            # Delete , and split lines apart into 3 columns
            data = line.strip().split(',')
            nominative, inessive, word_type = data[0], data[1], data[2]
            
            # Insert into db
            query ="INSERT INTO words(nominative, inessive, word_type) VALUES (%s, %s, %s);"
            cursor.execute(query,(nominative,inessive, word_type))

            # Commit changes
            mydb.commit()
    logging.info(msg="Successfully filled Database")
            
# Returns first 1000 words from table words
def retrieveData(cursor : MySQLCursor):
    logging.info(msg="Start retrieving everything")

    # Select every word from 0 to 1000
    cursor.execute("USE CaseDB;")
    query = "SELECT * FROM words LIMIT 0, 1000;"
    cursor.execute(query)

     # Fetch all the selected rows
    result = cursor.fetchall()

    logging.info(msg="Successfully retrieved everything")
    return result 

# Returns all words from certain word type
def retrieveType(cursor : MySQLCursor, word_type):
    logging.info(msg="Start retrieving type")

    # Select every word with word_type
    cursor.execute("USE CaseDB")
    query = "SELECT * FROM words WHERE word_type = %s"
    cursor.execute(query, word_type)

    # Fetch all the selected rows
    result = cursor.fetchall()

    logging.info(msg="Successfully retrieved type")
    return result

# Returns n number of test cases randomized(is called in tests_page.py)
def retrieveRandomCase(cursor: MySQLCursor, numberOfTestCases:int):
    logging.info(msg="Start retrieving random cases")
    cursor.execute("USE CaseDB;")
    
    # Query to retrieve 15 random words
    query = f"SELECT nominative, inessive FROM words ORDER BY RAND() LIMIT {numberOfTestCases};"
    cursor.execute(query)
    
    # Fetch all the selected rows
    random_words = cursor.fetchall()
    
    # 2D array to store nominative and inessive forms
    words_2d_array = []
    
    # Iterate through each row and append nominative and inessive forms to the 2D array
    for row in random_words:
        nominative = row[0]
        inessive = row[1]
        words_2d_array.append([nominative, inessive])
    
    logging.info(msg="Successfully retrieved random words")
    return words_2d_array


#Sample Usage
if (__name__ == '__main__'):
    global mydb
    mydb = createDB()
    cursor = mydb.cursor()
    cursor.execute("DROP TABLE words")
    createTable(cursor)
    fillDB('Data/data.txt', cursor)
    random_words = retrieveRandomCase(cursor, str(15))
    print(random_words)
    mydb.close()
    

