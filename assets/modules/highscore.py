import MySQLdb


def insertWinner(winnerName, winnerScore):
    #  Open connection to database
    db = MySQLdb.connect(host="37.187.108.9",
                         port=3306,
                         user="prj2user",
                         passwd="projectwachtwoord",
                         db="db_project_2")
    #  Create cursor
    cursor = db.cursor()
    #  Query to execute
    query = "INSERT INTO highscores (name, score) VALUES (%s, %s)"
    winnerArgs = (winnerName, winnerScore)
    #  Execute query
    cursor.execute(query, winnerArgs)
    #  Commit query into database
    db.commit()
    #  Close database connection
    db.close()


def selectHighscores():
    #  Open connection to database
    db = MySQLdb.connect(host="37.187.108.9",
                         port=3306,
                         user="prj2user",
                         passwd="projectwachtwoord",
                         db="db_project_2")
    #  Create cursor
    cursor = db.cursor()
    #  Query to execute
    query = "SELECT name, score FROM highscores ORDER BY score DESC LIMIT 10"
    #  Execute query
    cursor.execute(query)
    #  Fill result variable with query result
    result = cursor.fetchall()
    #  Close database connection
    db.close()
    #  Return result
    return result
