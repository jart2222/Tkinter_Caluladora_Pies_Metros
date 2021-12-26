from tkinter import *
from tkinter import ttk
# El siguiente código configura la ventana principal
# de la aplicación, dándole el título "Pies a metros".

def calculate(*args):
    try:
        value = float(pies.get())
        metros.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root=Tk();
root.title("Pies a metros ");
mainFrame=ttk.Frame(root,padding="3 3 12 12")
mainFrame.grid(column=0,row=0,sticky=(N,W,E,S)) #ubicacion dentro de rooy
# el marco debe expandirse para llenar
# cualquier espacio adicional si se cambia el tamaño de la ventana.
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

#s la entrada para ingresar el número de pies a convertir.

pies=StringVar()
metros = StringVar()
#-------------------------------
pies_entry=ttk.Entry(mainFrame, width=7, textvariable=pies)
pies_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainFrame, text="Pies").grid(column=3, row=1, sticky=W)
#-------------------------------
ttk.Label(mainFrame, text="Es equivalente a: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainFrame, textvariable=metros).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainFrame, text="metros").grid(column=3, row=2, sticky=W)
#------------------------------
ttk.Button(mainFrame, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)


for child in mainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)
pies_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()