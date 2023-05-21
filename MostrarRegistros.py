import sqlite3

conexion = sqlite3.connect ('Ejemplo.db')
c = conexion.cursor()

c.execute ("SELECT * FROM acciones")

for r in c.execute ("SELECT * FROM acciones"):
    print(r)

conexion.close()