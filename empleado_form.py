import pandas as pd #me permite trabajar con estructuras de datos
import sys #me permite trabajar con el sistema operativo
import os #me permite trabajar archivos y parpetas del sistema operativo


from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,QHeaderView, QMessageBox)

#la variable df contiene la tabla de empleados
#la tabla de empleados tiene las siguientes columnas: Nombre, Apellido, Profesion, Sueldo, sueldo_Net
df=pd.DataFrame(columns=["Nombre","Apellido", "Profesion", "Sueldo","sueldo_Neto"])

def crear_app():
    app = QApplication(sys.argv) #crea la aplicacion
    ventana = QWidget() #crea la ventana
    ventana.setWindowTitle("Registro de Empleados") #titulo de la ventana
    ventana.resize(800,600) #tamañado de la ventana (ancho, alto)
    
    layout_principal = QVBoxLayout() #crea el layout principal
    layout_principal.addSpacing(30) #agrega un espacio al layout principal

    layout_formulario = QHBoxLayout() #crea el layout del formulario

    nombre_input =QLineEdit() #crea el input de nombre
    nombre_input.setFixedHeight(40) #fija la altura del input
    nombre_input.setPlaceholderText("Nombre") #texto de ayuda del input
    layout_formulario.addWidget(nombre_input) #agrega el input al layout del formulario

    apellido_input =QLineEdit() #crea el input de nombre
    apellido_input.setFixedHeight(40) #fija la altura del input
    apellido_input.setPlaceholderText("Apellido") #texto de ayuda del input
    layout_formulario.addWidget(apellido_input) #agrega el input al layout del formulario

    Profesion_input =QLineEdit() #crea el input de nombre
    Profesion_input.setFixedHeight(40) #fija la altura del input    
    Profesion_input.setPlaceholderText("Profesion") #texto de ayuda del input
    layout_formulario.addWidget(Profesion_input) #agrega el input al layout del formulario

    sueldo_input =QLineEdit() #crea el input de nombre
    sueldo_input.setFixedHeight(40) #fija la altura del input    
    sueldo_input.setPlaceholderText("Sueldo") #texto de ayuda del input
    layout_formulario.addWidget(sueldo_input) #agrega el input al layout del formulario

    layout_principal.addLayout(layout_formulario) #agrega el layout del formulario al layout principal

    layout_botones=QHBoxLayout() #crea el layout de los botones

    boton_agregar = QPushButton("Agregar") #crea el boton de guardar
    boton_agregar.setFixedHeight(40) #fija la altura del boton
    layout_botones.addWidget(boton_agregar) #agrega el boton al layout de los botones

    boton_exportar = QPushButton("Exportar Excel") #crea el boton de guardar
    boton_exportar.setFixedHeight(40)
    layout_botones.addWidget(boton_exportar) #agrega el boton al layout de los botones

    layout_principal.addLayout(layout_botones) #agrega el layout de los botones al layout principal

    tabla=QTableWidget() #crea la tabla
    tabla.setColumnCount(5) #numero de columnas de la tabla
    tabla.setHorizontalHeaderLabels(["Nombre","Apellido", "Profesion", "Sueldo","sueldo_Neto"]) #nombres de las columnas de la tabla
    layout_principal.addWidget(tabla) #agrega la tabla al layout principal

    tabla.horizontalHeader().setStretchLastSection(True) #ajusta el ancho de la tabla al tamaño de la ventana
    #tabla.horizontalHeader().setSectionResizeMode() #ajusta el ancho de la tabla al tamaño de la ventana
    layout_principal.addWidget(tabla) #agrega la tabla al layout principal


    ventana.setLayout(layout_principal) #agrega el layout principal a la ventana
    ventana.show() #muestra la ventana
    

    def agregar_datos(): #funcion para obtener sueldos
        nombre = nombre_input.text() #obtiene el texto del input de nombre
        apellido = apellido_input.text() #obtiene el texto del input de apellido
        profesion = Profesion_input.text() #obtiene el texto del input de profesion
        
        sueldo = float(sueldo_input.text()) #obtiene el texto del input de sueldo

        if sueldo >0 and sueldo <= 1000:
            sueldo_neto = sueldo*0.8 #calcula el sueldo neto
        elif sueldo >1000 and sueldo <= 4000:
            sueldo_neto = sueldo*0.75 #calcula el sueldo neto
        else:
            sueldo_neto = sueldo*0.65 #calcula el sueldo neto

        nueva_fila = {"Nombre":nombre, "Apellido":apellido, "Profesion":profesion, "Sueldo":sueldo, "sueldo_Neto":sueldo_neto} #crea un diccionario con los datos del empleado
        
        #Aqui guardamos los datos en la memoria
        global df #declara la variable df como global para poder usarla en otras funciones
        df.loc[len(df)] = nueva_fila #agrega la nueva fila al dataframe
       
       #aqui guardamos los archivos a nivel grafico para visualizarlo
        fila = tabla.rowCount() #establece el numero de filas de la tabla
        tabla.insertRow(fila) #inserta una nueva fila en la tabla
        tabla.setItem(fila, 0, QTableWidgetItem(nombre)) #agrega el nombre a la tabla
        tabla.setItem(fila, 1, QTableWidgetItem(apellido))
        tabla.setItem(fila, 2, QTableWidgetItem(profesion))
        tabla.setItem(fila, 3, QTableWidgetItem(f"{sueldo:.2f}")) #agrega el sueldo a la tabla
        tabla.setItem(fila, 4, QTableWidgetItem(f"{sueldo_neto:.2f}")) #agrega el sueldo neto a la tabla
        
        tabla.resizeRowToContents() #ajusta el tamaño de la fila al contenido

        nombre_input.clear() #limpia el input de nombre
        apellido_input.clear() #limpia el input de apellido
        Profesion_input.clear() #limpia el input de profesion
        sueldo_input.clear() #limpia el input de sueldo

    def exportar_excel():
        if os.path.exists("data_empleados.xlsx"):
            os.remove("data_empleados.xlsx")
        df.to_excel("data_empleados.xlsx", index=False, engine="openpyxl") #exporta el dataframe a un archivo excel

    
    boton_exportar.clicked.connect(exportar_excel) #conecta el boton de exportar a la funcion exportar_excel
    boton_agregar.clicked.connect(agregar_datos) #conecta el boton de agregar a la funcion agregar_datos
    sys.exit(app.exec()) #para cerrar la ventana en la X
crear_app() #llama a la funcion crear_app