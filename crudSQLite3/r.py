import sqlite3
conn = sqlite3.connect('estudiantes.db')
cursor = conn.execute("SELECT * from ESTUDIANTE")
print(cursor.fetchall())

conn.close()