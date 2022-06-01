# Creating table into database!!!
import sqlite3
# Connect to sqlite database
conn = sqlite3.connect('estudiantes.db')
# cursor object
cursor = conn.cursor()
# drop query
cursor.execute("DROP TABLE IF EXISTS estudiantes")
# create query
query = """CREATE TABLE ESTUDIANTE(
        ID INT PRIMARY KEY NOT NULL,
        NOMBRE CHAR(20) NOT NULL, 
        ASIGNATURA CHAR(20), 
        DIRECCION CHAR(50), 
        CLASE CHAR(20) )"""
cursor.execute(query)
# commit and close
conn.commit()
conn.close()





