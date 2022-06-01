import sqlite3
conn = sqlite3.connect('estudiantes.db')
conn.execute("DELETE from ESTUDIANTE where ID = 2;")
conn.commit()
cursor = conn.execute("SELECT * from ESTUDIANTE")
print(cursor.fetchall())
conn.close()