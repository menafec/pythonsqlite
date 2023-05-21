import sqlite3

conexion = sqlite3.connect('Ejemplo.db')

c = conexion.cursor()

c.execute("INSERT INTO acciones VALUES ('01/ene/2023', 'compra', 'INV', 800, 42.50)")
c.execute("INSERT INTO acciones VALUES ('11/sep/2001', 'compra', 'INV', 200, 15)")
c.execute("INSERT INTO acciones VALUES ('29/dic/2017', 'compra', 'INV', 71, 14.50)")
c.execute("INSERT INTO acciones VALUES ('21/may/2020', 'compra', 'INV', 32, 12)")
c.execute("INSERT INTO acciones VALUES ('18/abr/2002', 'compra', 'INV', 180, 25.10)")

conexion.commit()
conexion.close()