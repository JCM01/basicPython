import sqlite3
conn = sqlite3.connect('estudiantes.db')
conn.execute("UPDATE ESTUDIANTE set ASIGNATURA = 005 where ID = 1")
conn.commit()
cursor = conn.execute("SELECT * from ESTUDIANTE")
print(cursor.fetchall())
conn.close()