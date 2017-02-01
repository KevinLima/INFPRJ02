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

def retrieve_questions():
    array_vullen = "SELECT id, vraag_cat, vraag, vraag_goed, antwoord1, antwoord2, antwoord3 FROM vragen"

    data = connector(array_vullen)
    #print(data)  # Result van één query printen
    # print(connector(array_vullen1))  # Result van een query (afhankelijk van andere queries) printen

    qlist = []
    #if 0 <= index < len(list):

    for x in data:
        if x[6] is not None:
            list = [
                x[0],
                x[1],
                x[2],
                x[3],
                [x[4],
                 x[5],
                 x[6]]
            ]
        else:
            list = [
                x[0],
                x[1],
                x[2],
                x[3],
                [x[4],
                 x[5]]
            ]
        qlist.append(list)

    #print(qlist)
    return qlist


