import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("ActividadEscuela.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS alumno (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS materia (clave_materia INTEGER PRIMARY KEY, nombre TEXT NOT NULL, clave INTEGER NOT NULL, FOREIGN KEY(clave) REFERENCES alumno(clave));")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    conn.close()

continuar = True

while continuar:
    print("Proporcione los datos del alumno, entre la clave 0 (cero) para terminar...")
    campo_clave = int(input("Clave del alumno: "))
    if campo_clave == 0:
        continuar = False
    else:
        campo_nombre = input("Nombre del alumno: ")
        try:
            with sqlite3.connect("ActividadEscuela.db") as conn:
                mi_cursor = conn.cursor()
                valores = {"clave":campo_clave, "nombre":campo_nombre}
                mi_cursor.execute("INSERT INTO alumno VALUES(:clave,:nombre)", valores)
            print("*** Registro agregado exitosamente ***")
            print("")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

print("Se concluyó la carga de registros")

continuar = True

while continuar:
    print("Proporcione los datos de la materia, entre la clave 0 (cero) para terminar...")
    campo_clave_materia = int(input("Clave de la materia: "))
    if campo_clave_materia == 0:
        continuar = False
    else:
        campo_nombre = input("Nombre de la materia: ")
        campo_clave = input("Clave del alumno: ")
        try:
            with sqlite3.connect("ActividadEscuela.db") as conn:
                mi_cursor = conn.cursor()
                valores = {"clave_materia":campo_clave_materia, "nombre":campo_nombre, "clave":campo_clave}
                mi_cursor.execute("INSERT INTO materia VALUES(:clave_materia,:nombre,:clave)", valores)
            print("*** Registro agregado exitosamente ***")
            print("")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

print("Se concluyó la carga de registros")