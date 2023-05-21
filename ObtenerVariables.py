import sqlite3

conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()

fecha = ""
cantidad = ""
c.execute('''SELECT fecha, cantidad FROM acciones''')
registros = c.fetchall()
for registro in registros:
    fecha = registro[0]
    cantidad = registro[1]

conexion.close()

print ("Hora y fecha: ", fecha , "Cantidad: ", cantidad) 