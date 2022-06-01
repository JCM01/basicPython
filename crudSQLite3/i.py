import sqlite3
conn = sqlite3.connect('estudiantes.db')

try:

    conn.execute("INSERT INTO ESTUDIANTE (ID,NOMBRE,ASIGNATURA,DIRECCION,CLASE) "
             "VALUES (1, 'John', '001', 'Bangalore', 'A')")
    conn.execute("INSERT INTO ESTUDIANTE (ID,NOMBRE,ASIGNATURA,DIRECCION,CLASE) "
             "VALUES (2, 'Naren', '002', 'Hyd', 'B')")
    print(conn)
except:
  print("An exception occurred")

conn.commit()
conn.close()