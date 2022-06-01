import sqlite3

menu_options = {
    1: 'Crear Tabla Tienda',
    2: 'Añadir Cliente',
    3: 'Ver Clientes',
    4: 'Actualizar Cliente',
    5: 'Quitar Cliente',
    6: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    print('Has cogido\'Opcion 1\'')


def option2():
    print('Has cogido\'Opcion 2\'')


def option3():
    print('Has cogido\'Opcion 3\'')


def option4():
    print('Has cogido\'Opcion 4\'')


def option5():
    print('Has cogido\'Opcion 5\'')


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()

            # Connect to sqlite database
            conn = sqlite3.connect('TIENDA.db')
            # cursor object
            cursor = conn.cursor()
            # drop query
            cursor.execute("DROP TABLE IF EXISTS TIENDA")
            # create query
            query = """CREATE TABLE CLIENTE(
                    ID INT PRIMARY KEY NOT NULL,
                    NOMBRE CHAR(20) NOT NULL, 
                    DIRECCION CHAR(20), 
                    CIUDAD CHAR(50), 
                    TLF CHAR(20) )"""
            cursor.execute(query)
            # commit and close
            conn.commit()
            conn.close()
        elif option == 2:
            option2()
            conn = sqlite3.connect('TIENDA.db')

            conn.execute("INSERT INTO CLIENTE (ID,NOMBRE,DIRECCION,CIUDAD,TLF) "
                         "VALUES (" + input('Dime ID') + ", " + input('Dime nombre') + ", " + input('Dime direccion') + ", " + input('Dime ciudad') + ", " + input('Dime tlf') + "")

            conn.commit()
            conn.close()
        elif option == 3:
            option3()

            conn = sqlite3.connect('CLIENTES.db')
            cursor = conn.execute("SELECT * from CLIENTE")
            print(cursor.fetchall())

            conn.close()
        elif option == 4:
            option4()

            conn = sqlite3.connect('CLIENTES.db')
            conn.execute("UPDATE CLIENTE set DIRECCION = 'Calle Ocaña, 7' where ID = 1")
            conn.commit()
            cursor = conn.execute("SELECT * from CLIENTE")
            print(cursor.fetchall())
            conn.close()
        elif option == 5:
            option5()

            conn = sqlite3.connect('CLIENTES.db')
            conn.execute("DELETE from CLIENTE where ID = 2;")
            conn.commit()
            cursor = conn.execute("SELECT * from CLIENTE")
            print(cursor.fetchall())
            conn.close()
        elif option == 6:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')
