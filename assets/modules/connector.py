import MySQLdb


def connector(query):
    db = MySQLdb.connect(host="37.187.108.9",
                         port=3306, user="prj2user",
                         passwd="projectwachtwoord",
                         db="db_project_2")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][1]


array_vullen = "SELECT id, vraag, vraag_goed, antwoord1, antwoord2, antwoord3 FROM vragen ORDER BY RAND() LIMIT 1"
array_vullen1 = "SELECT vraag FROM vragen WHERE id = %s", (array_vullen)
array_vullen2 = "SELECT antwoord1, antwoord2, antwoord3 FROM vragen WHERE id = %s", (array_vullen)
array_vullen3 = "SELECT vraag_goed FROM vragen WHERE id = %s", (array_vullen)

print(connector(array_vullen))  # Result van één query printen
# print(connector(array_vullen1))  # Result van een query (afhankelijk van andere queries) printen
