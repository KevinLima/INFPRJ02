import MySQLdb


def connector(query):
    db = MySQLdb.connect(host="37.187.108.9",
                         port=3306, user="prj2user",
                         passwd="projectwachtwoord",
                         db="db_project_2")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


array_vullen = "SELECT id, vraag, vraag_goed, antwoord1, antwoord2, antwoord3 FROM vragen"
array_vullen1 = "SELECT vraag FROM vragen WHERE id = %s", (array_vullen)
array_vullen2 = "SELECT antwoord1, antwoord2, antwoord3 FROM vragen WHERE id = %s", (array_vullen)
array_vullen3 = "SELECT vraag_goed FROM vragen WHERE id = %s", (array_vullen)


data = connector(array_vullen)
print(data)  # Result van één query printen
# print(connector(array_vullen1))  # Result van een query (afhankelijk van andere queries) printen

qlist = []
#if 0 <= index < len(list):

for x in data:
    if x[5] is not None:
        list = [
            x[0],
            x[1],
            x[2],
            [x[3],
             x[4],
             x[5]]
        ]
    else:
        list = [
            x[0],
            x[1],
            x[2],
            [x[3],
             x[4]]
        ]
    qlist.append(list)

print(qlist)


