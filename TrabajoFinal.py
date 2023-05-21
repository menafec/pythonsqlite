
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
import sqlite3


conexion = sqlite3.connect('Listas.db')
c = conexion.cursor()
nombreTabla = 'Datos'
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nombreTabla,))
existe = c.fetchone()

if existe is not None:
    print("La tabla (Datos) ya existe")
else:
    c.execute('''CREATE TABLE IF NOT EXISTS Datos(ID INTEGER PRIMARY KEY, Nombre text, ApePa text, ApeMa text, Correo text, Numero text, Leer text, Musica text, Videojuegos text,Obligacion text, Estado text)''')
    print("La tabla (Datos) se ha creado")

conexion.commit()
c = conexion.cursor()


def BorrarContenido():
    nombreVar.set("")
    APaternoVar.set("")
    AMaternoVar.set("")
    CorreoVar.set("")
    NumeroMovilVar.set("")
    Estados.set("")
    Leer.set(False)
    Musica.set(False)
    VideoJuegos.set(False)
    Obligacion.set(None)

def guardar_datosBSD():

    conexion = sqlite3.connect('Listas.db')
    c = conexion.cursor()

    c.execute('''SELECT COUNT (*) FROM Datos''')
    ID = c.fetchone()[0]
    ID = ID + 1

    Nombre = nombreVar.get()
    APaterno = APaternoVar.get()
    AMaterno = AMaternoVar.get()
    Correo = CorreoVar.get()
    Numero = NumeroMovilVar.get()
    SelecEstados = Estados.get()
    LeerOp = "Si" if Leer.get() == True else "No"
    MusicaOp = "Si" if Musica.get() == True else "No"
    VideoJuegosOp = "Si" if VideoJuegos.get() == True else "No"
    Obli = Obligacion.get()

    if not Nombre or not APaterno or not AMaterno or not Correo or not Numero or not LeerOp or not MusicaOp or not VideoJuegosOp or not Obli or not SelecEstados:
        messagebox.showinfo("ERROR", "Las casillas deben estar llenas para guardar.")
    else:
        NuevosDatos = [(ID,Nombre, APaterno, AMaterno, Correo, Numero, LeerOp, MusicaOp, VideoJuegosOp,Obli, SelecEstados)]
        c.executemany ('INSERT INTO Datos VALUES (?,?,?,?,?,?,?,?,?,?,?)', NuevosDatos)
        conexion.commit()
        BorrarContenido()
        conexion.close()

def guardar_datosCSV():

    with open("Listas2.csv", "r") as file:
        file.readlines
    
    Nombre = nombreVar.get()
    APaterno = APaternoVar.get()
    AMaterno = AMaternoVar.get()
    Correo = CorreoVar.get()
    Numero = NumeroMovilVar.get()
    SelecEstados = Estados.get()
    LeerOp = "Si" if Leer.get() == True else "No"
    MusicaOp = "Si" if Musica.get() == True else "No"
    VideoJuegosOp = "Si" if VideoJuegos.get() == True else "No"
    Obli = Obligacion.get()

    if not Nombre or not APaterno or not AMaterno or not Correo or not Numero or not LeerOp or not MusicaOp or not VideoJuegosOp or not Obli or not SelecEstados:
        messagebox.showinfo("ERROR", "Las casillas deben estar llenas para guardar.")
    else:
        with open("Listas2.csv","a") as file:
            file.write(f'{Nombre},{APaterno},{AMaterno},{Correo},{Numero},{LeerOp},{MusicaOp},{VideoJuegosOp},{Obli},{SelecEstados}\n') 
        BorrarContenido()
        TablaDatos.insert(parent="", index="end", iid=random.randint(0,1000), text=random.randint(0,1000), values=(Nombre, APaterno, AMaterno, Correo, Numero, LeerOp, MusicaOp, VideoJuegosOp,Obli,SelecEstados))


raiz = Tk()
raiz.title("Listas en Base de Datos")


mainFrame = ttk.Frame(raiz)
mainFrame.grid(column=0, row=0)
FrameInicial = ttk.Frame(mainFrame)
FrameInicial.grid(column=0,row=0)
Izquierda = ttk.Frame(FrameInicial, relief="raised", width= 30, height= 20)
Izquierda.grid(column=0, row=0, sticky=(W), padx=10, pady=10)
Derecha = ttk.Frame(FrameInicial, relief="raised", width= 30, height= 20)
Derecha.grid(column=1, row=0, sticky=(W), padx=10, pady=10)
FrameDatos1 = ttk.Frame(Izquierda, relief="raised", width= 20, height= 20)
FrameDatos1.grid(column=0, row=0, sticky=(W), padx=10, pady=10)
FrameDatos2= ttk.Frame(Izquierda, relief="raised", width= 20, height= 20)
FrameDatos2.grid(column=0, row=1, padx=10, pady=10)
FrameDatos3= ttk.Frame(Izquierda, relief="raised", width= 20, height= 20)
FrameDatos3.grid(column=0, row=2, padx=10, pady=10)
FrameDatos4 = ttk.Frame(Derecha, relief="raised", width= 20, height= 20)
FrameDatos4.grid(column=0, row=0, sticky=(N,W), padx=10, pady=10)
FrameDatos5= ttk.Frame(Derecha,  relief="raised", width= 20, height= 20)
FrameDatos5.grid(column=0, row=1, padx=10, pady=10)


nombreVar = StringVar()
APaternoVar = StringVar()
AMaternoVar = StringVar()
CorreoVar = StringVar()
NumeroMovilVar = StringVar()
Leer = BooleanVar()
Musica = BooleanVar()
VideoJuegos = BooleanVar()
Obligacion = StringVar(value=0)
Estados = StringVar()


NombreEntry = ttk.Entry(FrameDatos1, textvariable=nombreVar, width=26, ).grid(column=1, row=0,pady=5)
APaternoEntry = ttk.Entry(FrameDatos1, textvariable=APaternoVar, width=26).grid(column=1, row=1,pady=5)
AMaternoEntry = ttk.Entry(FrameDatos1, textvariable=AMaternoVar, width=26).grid(column=1, row=2,pady=5)
CorreoEntry = ttk.Entry(FrameDatos1, textvariable=CorreoVar, width=26).grid(column=1, row=3,pady=5)
NumeroEntry = ttk.Entry(FrameDatos1, textvariable=NumeroMovilVar, width=26).grid(column=1, row=4,pady=5)

ttk.Label(FrameDatos1, text= "Nombre: ", width="15", anchor="w").grid(column=0, row=0, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "A. Paterno: ",  width="15", anchor="w").grid(column=0, row=1, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "A. Materno: ",  width="15", anchor="w").grid(column=0, row=2, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "Correo: ",  width="15", anchor="w").grid(column=0, row=3, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "Movil: ",  width="15",anchor="w").grid(column=0, row=4, pady= 5, sticky=(E))

CheckLeer = ttk.Checkbutton(FrameDatos2, text="Leer", variable=Leer,width="10").grid(column=0,row=0,pady=5, sticky=(W))
CheckMusica = ttk.Checkbutton(FrameDatos2, text="Musica", variable=Musica, width="10").grid(column=1,row=0,pady=5, padx=5, sticky=(W))
CheckVJ = ttk.Checkbutton(FrameDatos2, text="Videojuegos", variable=VideoJuegos, width="10").grid(column=2,row=0,pady=5, padx=5, sticky=(W))

ttk.Button(FrameDatos3, text="Guardar", command=guardar_datosCSV).grid(column=0, row=0, sticky=(E))
ttk.Label(FrameDatos3, text="En Archivo CSV",).grid(column=0, row=1, sticky=(E))
ttk.Button(FrameDatos3, text="Guardar", command=guardar_datosBSD).grid(column=1, row=0, sticky=(E))
ttk.Label(FrameDatos3, text="En Archivo BSD",).grid(column=1, row=1, sticky=(E))
ttk.Button(FrameDatos3, text="Borrar", command=BorrarContenido).grid(column=2, row=0,sticky=(E))

RadioEst = ttk.Radiobutton(FrameDatos4, text="Estudiante", variable=Obligacion, value="Estudiante", width="12").grid(column=0, row=0, sticky=(N)) 
RadioEmp = ttk.Radiobutton(FrameDatos4, text="Empleado", variable=Obligacion, value="Empleado", width="12").grid(column=0 , row=1, sticky=(N)) 
RadioDesemp = ttk.Radiobutton(FrameDatos4, text="Desempleado", variable=Obligacion, value="Desempleado", width="12").grid(column=0, row=2, sticky=(N)) 

ttk.Label(FrameDatos5, text= "Estados: ",  width="15",anchor="w").grid(column=0, row=0, sticky=(E))
comboEstados = ttk.Combobox(FrameDatos5, textvariable=Estados, state="readonly")
comboEstados.grid(column=1, row=0)
comboEstados['values'] = ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila", 
                        "Colima", "Chiapas", "Chihuahua", "Ciudad de Mexico", "Durango", "Guanajuato", 
                        "Guerrero", "Hidalgo", "Jalisco", "Mexico", "Michoacan", "Morelos", "Nayarit", 
                        "Nuevo Leon", "Oaxaca", "Puebla", "Queretaro", "Quintana Roo", "San Luis Potosi", 
                        "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatan", "Zacatecas")



Tabla = Tk()
Tabla.title("Tabla Lista de Datos (Base de Datos)")

FrameTabla = ttk.Frame(Tabla)
FrameTabla.grid(column=0, row=0)

TablaDatos = ttk.Treeview(FrameTabla, columns=("nombre", "a_paterno", "a_materno", "correo", "movil", "ocupacion", "aficionLeer", "aficionMusica", "aficionVideojuegos", "estado"))

TablaDatos.heading("#0", text="ID")
TablaDatos.heading("nombre", text="Nombre")
TablaDatos.heading("a_paterno", text="Apellido paterno")
TablaDatos.heading("a_materno", text="Apellido materno")
TablaDatos.heading("correo", text="Correo")
TablaDatos.heading("movil", text="Móvil")
TablaDatos.heading("ocupacion", text="Ocupación")
TablaDatos.heading("aficionLeer", text="Lee")
TablaDatos.heading("aficionMusica", text="Escucha música")
TablaDatos.heading("aficionVideojuegos", text="Juega videojuegos")
TablaDatos.heading("estado", text="Estado")
TablaDatos.column("#0", width=50)
TablaDatos.column("nombre", width=100)
TablaDatos.column("a_paterno", width=120)
TablaDatos.column("a_materno", width=120)
TablaDatos.column("correo", width=200)
TablaDatos.column("movil", width=100)
TablaDatos.column("ocupacion", width=120)
TablaDatos.column("aficionLeer", width=100)
TablaDatos.column("aficionMusica", width=120)
TablaDatos.column("aficionVideojuegos", width=120)
TablaDatos.column("estado", width=120)

with open('Listas2.csv', 'r') as file:
    lineas = file.readlines()
    for i, linea in enumerate(lineas):
        lista = linea.strip().split(",")
        TablaDatos.insert(parent="", index="end", iid = i, text = i, values=(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9]))

TablaDatos.pack()

raiz.mainloop()