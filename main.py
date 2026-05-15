import pandas as pd # importa la libreria y le asigna el alias pd para que sea mas corto
import os 

df = pd.read_csv("annual.csv") # carga el archivo csv


    
while True:
    print ("--- Menú---")
    print ("1) Mostrar anomalía de temperatura por año (desde 1850 a 2024)")
    print("2) Mostrar la media por año")
    print("3) Mostrar temperaturas de acuerdo a la fuente por año")
    print("4) Mostrar gráfico")
    print("0) Salir del sistema")
        
        
    opcion = input("Opcion: ")
        
    if opcion == "0":
            print (" Saliendo del programa.")
            break
        
    elif opcion == "1": # Mostrar la temperatura promedio entre los años en los que se tiene registro
            print("Este es el dato más importante. No representa la temperatura absoluta, sino la anomalía de temperatura.\n")
            print("Una anomalía es la diferencia respecto a un promedio histórico (línea base).\n ")
            print("Valor 0: El año tuvo la misma temperatura promedio que el periodo de referencia.\n")
            print ("Valor Positivo (>0): El año fue más cálido que el promedio.\n")
            print ("Valor Negativo (<0): El año fue más frío que el promedio.\n")
          
            promedio_global = df["Mean"].mean()
            
            print(f"El promedio de anomalía global térmica es: {promedio_global}\n")    
            
             
    elif opcion =="2":
        anio_buscar = int(input("Ingrese el año que desea buscar: "))
        anio =df[df["Year"] == anio_buscar] # filtra las filas que coinciden con el año
        
        if len(anio) > 0:
            media_resultado = anio["Mean"].mean()
            print(f"La media de ese año es {media_resultado}")
        else:
            print("No se encontró el año.")
            
    elif opcion == "3":
        print ("Seleccione la fuente que desea buscar: ")
        print ("1) gcag: Global Climate Analysis Group (generalmente asociado a NOAA). ")    
        print ("2) GISTEMP: GISS Surface Temperature Analysis (NASA).")
        print ("0) Para salir")
        
        fuente = input("Elige una fuente: ")
        
        if fuente == "0":
            print ("Volviendo al menú anterior.")
            break
        
        elif fuente == "1":
            fuente_gcag = df [df["Source"] == "gcag"] # filtra las filas que coinciden con la fuente
            if len(fuente_gcag) > 0:
                print(f"Los datos aportados por esa fuente son: {fuente_gcag} ")
            
        
        elif fuente == "2":
            fuente_gistemp = df[df["Source"] == "GISTEMP"]     
            if len(fuente_gistemp) >0:
                print(f"Los datos aportados por esa fuente son: {fuente_gistemp} ")
    
    elif opcion == "4":
    
        print("Abriendo el gráfico...")
        
        os.startfile("temp_promedio_global.png") # le dice a windows que abra la imagen
                     
