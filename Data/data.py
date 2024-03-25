'''
Please make sure before using the code that you have a local instance of MySqlServer running.
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

# Maybe add id as key for every, useful to create certain tasks for user
# Creates table named words where all words from data.txt are saved
def createTable(cursor : MySQLCursor):
    query = "CREATE TABLE IF NOT EXISTS words (nominative VARCHAR(255), inessive VARCHAR(255), word_type INT);"
    logging.info(msg="Successfully Created Table")
    cursor.execute(query)
    mydb.commit()

# Fills words with content from data.txt (must only be called ones)
def fillDB(filename, cursor : MySQLCursor):
    cursor.execute("USE CaseDB")
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            nominative, inessive, word_type = data[0], data[1], data[2]
            #Check text file for column names
            query ="INSERT INTO words(nominative, inessive, word_type) VALUES (%s, %s, %s);"
            cursor.execute(query,(nominative,inessive, word_type))
            mydb.commit()
    logging.info(msg="Successfully filled Database")
            
# Returns Everything that is is 
def retrieveData(cursor : MySQLCursor):
    logging.info(msg="Start retrieving everything")
    cursor.execute("USE CaseDB;")
    query = "SELECT * FROM words LIMIT 0, 1000;"
    cursor.execute(query)
    for (nominative, inessive, word_type) in cursor:
        print(nominative, inessive, word_type)
    logging.info(msg="Successfully retrieved everything")

# Returns all words from certain word type
def retrieveType(cursor : MySQLCursor, word_type):
    logging.info(msg="Start retrieving type")
    cursor.execute("USE CaseDB")
    query = "SELECT * FROM words WHERE word_type = %s"
    result = cursor.execute(query, word_type)
    logging.info(msg="Successfully retrieved type")
    return result

#returns n number of test cases (is called in tests_page.py)
def retrieveRandomCase(cursor: MySQLCursor, numberOfTestCases):
    pass


#Sample Usage
if (__name__ == '__main__'):
    global mydb
    mydb = createDB()
    cursor = mydb.cursor()
    #cursor.execute("DROP TABLE words")
    #createtable(cursor)
    #filldb('Data/data.txt', cursor)
    retrieveData(cursor)
    #print(retrievedata(cursor))
    mydb.close()
    

