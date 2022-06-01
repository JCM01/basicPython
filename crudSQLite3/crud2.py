import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('tienda.db')

        return con

    except Error:

        print(Error)

'''
def sql_table(con):

    cursorobj = con.cursor()

    cursorobj.execute("create table clientes(id integer primary key, nombre text, telefono text)")

    con.commit()

con = sql_connection()

sql_table(con)'''

def crud():

    while True:

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[R] Listar clientes     ")
        print("[C] Añadir cliente      ")
        print("[U] Modificar cliente   ")
        print("[D] Borrar cliente      ")
        print("[E] Salir               ")
        print("========================")

        option = input("> ")

        if option == 'r':
            print("Listando los clientes...\n")

            def sql_fetch(conn):

                conn = sqlite3.connect('CLIENTES.db')
                cursor = conn.execute("SELECT * from CLIENTES")
                print(cursor.fetchall())

        if option == 'c':
            print("Añadiendo un cliente...\n")

            def sql_insert(con, entities):
                cursorObj = con.cursor()

                cursorObj.execute(
                    'INSERT INTO cliente(id, nombre, apellido, ciudad, fecha) VALUES(null, ?, ?, ?, ?)', datos)

                con.commit()

            sql_insert(con, datos)
            print("Cliente añadido correctamente\n")

        if option == 'u':
            print("Modificando un cliente...\n")


        if option == 'd':
            print("Borrando un cliente...\n")

            print("Cliente borrado correctamente\n")
        if option == 'e':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")


crud()