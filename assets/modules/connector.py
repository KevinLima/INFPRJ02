import MySQLdb


def connector():
    db = MySQLdb.connect(host="37.187.108.9", port=3306, user="", passwd="", db="")
    cursor = db.cursor()
    cursor.execute("""SELECT naam FROM tabel""")
    result = cursor.fetchall()
    return result


print(connector())
