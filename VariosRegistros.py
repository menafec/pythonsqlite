import sqlite3
import time

conexion = sqlite3.connect ('Ejemplo.db')
c = conexion.cursor()

'''
movimientos = [ ('24/nov/2016', 'venta', 'HPC', '50', '20.01'), ('25/nov/2016',
'compra', 'SNY', '100', '7.18'),
('26/nov/2016', 'compra', 'XBX', '75',' 5.33')]

c.executemany('INSERT INTO acciones VALUES (?,?,?,?,?)', movimientos)
conexion.commit()

for row in c.execute ("SELECT * FROM acciones"):
    print(row)
'''
'''
for row in c.execute("SELECT * FROM acciones WHERE operacion = 'compra' "):
    print(row)
'''
fecha = time.ctime()
operacion = 'compra'
simbolo = 'RAP'
cantidad = '80'
precio = '33.33'

movimientos = [(fecha, operacion, simbolo, cantidad, precio)]

c.executemany ('INSERT INTO acciones VALUES (?,?,?,?,?)', movimientos)
conexion.commit()

conexion.close()