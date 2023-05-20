import pyfiglet as py
import json as j
from typing import List, Dict

# Imprimir el nombre en grande
bienvenida = py.figlet_format(" CELLS-HOUSE ")
print(bienvenida)
# Imprimir el eslogan debajo del nombre
print("Los mejores dispositivos")
cesta: List[Dict[str, int]] = []
#Areas de la teinda 
samsung_telefonos= [   
                    {"Nombre": "Samsung S23 Ultra", 
                    "Proveedor": "Samsung",       
                    "Fecha de ingreso": "8/03/2023", 
                    "detalles": "Amoled de 6,8, Snapdragon 8 gen 2, Camara de 200 mp", 
                    "precio": 1700.00,       
                    "unidades Disponibles": 8 
                    },  
                   { "Nombre": "Samsung Buds",  
                    "Proveedor": "Samsung", 
                    "Fecha de ingreso": "8/03/2023",                        
                    "detalles": "Cancelación de ruido,  Bluetoot5.0 ,color Negro",        
                    "precio": 65.00,        
                    "unidades": 10    
                    },
                    {
                    "Nombre": "Tablet Samsung",
                    "Proveedor": "Samsung",
                    "Fecha de ingreso": "05/05/2023",
                    "detalles": "Tablet con 500 gb de almacaenamiento, Procesador Dimensity X , Cámara de 64 mp",
                    "precio": 635.00,
                    "unidades": 6
                    },
                    {
                    "Nombre": "Samsungn A51,",
                    "Proveedor": "Samsung Store",
                    "Fecha de ingreso": "10/01/2023",
                    "detalles": "Cámara principal de de 48 mp , Color Celeste  ",
                    "precio":285.00,
                    "Unidades":9
                    }
            ]
                        
diccionario1 = {}
for item in samsung_telefonos:
    
    diccionario1[item["Nombre"]] = item
apple_telefonos=  [
                {
                    "Nombre": "IPhone 14",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "15/05/2023",
                    "detalles": "Camara trasera con 12 Mp con teleobjetivo, gran angular y ultra gran angular, Camara frontal de 12 MP, 512 GB de Almacenamiento, 6 GB de Ram, Pantalla de 6.7 Pulgadas  ",
                    "precio": 1400.00,
                    "unidades": 5
                },
                {
                    "Nombre": "IPhone 11",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "12/05/2023",
                    "detalles": "Camara principal dual de 12MP y frontal de 12 MP, Pantalla 6.1 Pulgadas, 256 de Almacenamiento, 4 GB de Ram  ",
                    "precio": 820.00,
                    "unidades": 9
                },
                {
                 "Nombre": "IPhone 13",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "10/05/2023",
                    "detalles": "Camara principal dual de 12 Mp y frontal de 12 Mp, Almacenamiento de 512 GB, 4 GB de Ram, Pantalla de 6.1 Pulgadas,",    
                    "precio": 1200.00,
                    "unidades": 9
                },
                {
                    "Nombre": "Iphone 14 pro max",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "pantalla oled 6.1 pulgadas, camara de 13 Megapixeles",
                    "precio": 1500.00,
                    "unidades": 5
                },
                {
                    "Nombre": "Iphone 13 pro max",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "08/05/2023",
                    "detalles": "pantalla oled 6.1 pulgadas, camara de 13 Megapixeles, 512 GB de almacenamiento, 6 GB de Ram,",
                    "precio": 1400.00,
                    "unidades": 9
                },
                {
                    "Nombre": "Iphone 12 pro max",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "7/05/2023",
                    "detalles": " Pantalla oled 6.1 pulgadas, camara de 13 Megapixeles, 256 GB de almacenamiento, 6 GB de Ram,",
                    "precio": 1200.00,
                    "unidades": 4
                }
                
            ]
diccionario2 = {}
for item in apple_telefonos:
    diccionario2[item["Nombre"]] = item
xiaomi_telefonos=    [
                {
                    "Nombre": "Xiaomi 12T Pro", 
                    "Proveedor": "Xiaomi",
                    "Fecha de ingreso": "02/05/2023",
                    "detalles": "Camara de 200 MP, 12 GB de Ram, 1 TB GB de Almacenamiento, Pantalla de 6.67 Pulgadas, Procesador Snapdragon 888",
                    "precio": 1000.00,
                    "unidades":17
                },
                {
                    "Nombre": "Xiaomi Redmi Note 11",
                    "Proveedor": "Xiaomi",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Camara principal de 50 MP, 6 GB de Ram, 128 GB de Almacenamiento, Pantalla de 6.43 Pulgadas, Procesador Snapdragon 680",
                    "precio": 300.00,
                    "Unidades":20
                },
                {
                    "Nombre": "Xiaomi Redmi Note 10 Pro",
                    "Proveedor": "Xiaomi",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Pantalla de 6.67 a 120Hz con HDR 10, Procesador  Qualcomm Snapdragon 732G, 8 de memoria Ram, 128 GB de almacenamiento, Camara principal de 108 Mp, UGA 8 Mp, 5 Mp telemacro,Profundidad 2 Mp.  ",
                    "precio": 260.00,
                    "Unidades": 5
                },
                {
                    "Nombre": "Poco X3 Pro",
                    "Proveedor": "Xiaomi",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Camara principal de 48 Mp, UGA 8, Macro de 2 Mp y profundidad de 2 Mp, Pantalla Gorilla Glass 6.67 Pulgadas de 120Hz a 240Hz, Qualcomm Snapdragon 860, 8 GB de Ram, 256 GB de Almacenamiento. ",
                    "precio": 282.85,
                    "Unidades":17
			    }
            ]
                
diccionario3={}       
for item in xiaomi_telefonos:
    diccionario3[item["Nombre"]] = item
                
                
samsung_accesorios = [
                    {        
                    "Nombre": "Cargador Samsung ", 
                    "Proveedor": "Amazon",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Cargador Original, Carga Rápida ,colores Blanco y Negro",        
                    "precio": 40.00,        
                    "unidades": 12   
                    },
                    {        
                    "Nombre": "Audifonos Samsung Gama baja", 
                    "Proveedor": "Amazon",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Audifonos Alambricos,color Blanco",        
                    "precio": 12.00,        
                    "unidades": 15   
                    },
                    {
                    "Nombre": "Airpods Pro",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "29/04/2023",
                    "detalles": "Cancelación de ruido,  Bluetoot5.0 ,color Blanco",
                    "precio": 200.00,
                    "unidades": 10
                    },
                    {        
                    "Nombre": "Cargador Samsung ", 
                    "Proveedor": "Amazon",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Cargador Original, Carga Rápida ,colores Blanco y Negro",        
                    "precio": 40.00,        
                    "unidades": 10   
                    }    
                ]

diccionario4={}
for item in samsung_accesorios:
    diccionario4[item["Nombre"]] = item   
apple_accesorios=   [
                {
                    "Nombre": "Cargadores Iphone",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "10/05/2023",
                    "detalles": "Carga máxima de 20 W, Carga rápida, Carga inalámbrica, color Blanco",
                    "precio": 50.00,
                    "unidades": 20
                },
                {
                    "Nombre": "Airpods Pro",
                    "Proveedor": "Apple",
                    "Fecha de ingreso": "29/04/2023",
                    "detalles": "Cancelación de ruido,  Bluetoot5.0 ,color Blanco",
                    "precio": 200.00,
                    "unidades": 10
                },
                {        
                    "Nombre": "Protector de Pantalla iPhone, 8,8PLUS.X,XS;XSMAX,11,11pro,11proMax,12,12pro,12proMax,13,13pro,13proMax,14,14pro,14proMax ", 
                    "Proveedor": "Shein",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Protector de pantalla de privacidad, anti rayones, ante golpes",        
                    "precio": 6.00,        
                    "unidades": 30   
                },
                {        
                    "Nombre": "Funda iPhone, 8,8PLUS.X,XS;XSMAX,11,11pro,11proMax,12,12pro,12proMax,13,13pro,13proMax,14,14pro,14proMax  ", 
                    "Proveedor": "Shein",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Proteje de golpes de gran altura, No daña su carcasa, proteje de rayones",        
                    "precio": 10.00,        
                    "unidades": 30   
                }, 
            ]    
diccionario5={}
for item in apple_accesorios:
    diccionario5[item["Nombre"]] = item
xiaomi_accesorios= [
    {        
                    "Nombre": "Cargador Xiaomi ", 
                    "Proveedor": "XiaomiStore",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Cargador Original MI, Carga Rápida 67W ,colores Blanco",        
                    "precio": 34.99,        
                    "unidades": 10   
                    },

                {        
                    "Nombre": "Cargador Xiaomi ", 
                    "Proveedor": "XiaomiStore",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Cargador Original MI, Carga Rápida 10W ,colores Blanco",        
                    "precio": 13.89,        
                    "unidades": 10   
                    },

                {        
                    "Nombre": "Cargador Xiaomi ", 
                    "Proveedor": "XiaomiStore",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Cargador Original MI, Carga Rápida 33W ,colores Blanco",        
                    "precio": 20.63,        
                    "unidades": 10   
                    },

                {        
                    "Nombre": "Cargador Xiaomi ", 
                    "Proveedor": "XiaomiStore",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Cargador Original MI, Carga Rápida 120W ,colores Blanco",        
                    "precio": 65.00,        
                    "unidades": 10   
                    },

                {        
                    "Nombre": "Protector de Pantalla Xiaomi, Note 10,10pro,11,11pro,12,12,pro ", 
                    "Proveedor": "Shein",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Protector de pantalla de privacidad, anti rayones, ante golpes",        
                    "precio": 6.00,        
                    "unidades": 30   
                    },

                {        
                    "Nombre": "Funda Xiaomi, Note 10,10pro,11,11pro,12,12,pro ", 
                    "Proveedor": "Shein",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Proteje de golpes de gran altura, No daña su carcasa, proteje de rayones",        
                    "precio": 10.00,        
                    "unidades": 30   
                    },

                {        
                    "Nombre": "Auriculares Xiaomi Buds 3 ", 
                    "Proveedor": "Amazon",       
                    "Fecha de ingreso": "9/04/2023",       
                    "detalles": "Inalambricos, Bluetooth 5.2, con cancelacion de ruidos, color blancos",        
                    "precio": 59.99,        
                    "unidades": 10   
                    }
            ]
diccionario6={}
for item in xiaomi_accesorios:
    diccionario6[item["Nombre"]] = item

Telefonos= [samsung_telefonos,apple_telefonos,xiaomi_telefonos]
Accesorios= [samsung_accesorios,apple_accesorios,xiaomi_telefonos]
Areas = [Telefonos,Accesorios]
def programa_Admin():
        while True:
            print("\nBienvenido a la zona de almacenamiento de la tienda.")
            print("¿Qué acción desea realizar?")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Ver productos en la tienda")
            print("4. Crear Nueva Area")
            print("5. Salir")
            accion = int(input("Ingrese la opción deseada: "))
            if accion == 1:
                print("En que area desea agregar el producto?")
                opcionesarea= {"1. Teléfonos", "2. Accesorios", "3. Salir"}
                for i in opcionesarea:
                    print(i)
                opcion_area_elegida = input("Ingrese la opción deseada: ")
                while True:
                    if opcion_area_elegida == "1":
                        print("¿En que categoria desea agregar el producto?")
                        opcioncategoriav = ("1. Teléfonos Samsung", "2. Teléfonos Apple", "3. Teléfonos Xiaomi", "4. Salir")
                        for i in opcioncategoriav:
                            print(i)
                        opcion_categoria_elegida = input("Ingrese la opción deseada: ")
                        if opcion_categoria_elegida == "1":
                            print("Catálogo de Teléfonos Samsung")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            samsung_telefonos.append(producto)
                            print("Producto agregado exitosamente.")
                            print(producto)
                        elif opcion_categoria_elegida == "2":
                            print("Catálogo de teléfonos Apple")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            apple_telefonos.append(producto)
                            print("Producto agregado exitosamente.")
                        elif opcion_categoria_elegida == "3":
                            print("Catálogo de teléfonos Xiaomi")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            xiaomi_telefonos.append(producto)
                            print("Producto agregado exitosamente.")
                        elif opcion_categoria_elegida == "4":
                            return
                        else:
                            print("Opcion invalida")
                            
                    elif opcion_area_elegida == "2":
                        print("Menu de Accesorios")
                        print("Elija en que categoria desea agregar el producto")
                        opcionarea2= ("1.Accesorios Samsung", "2. Accesorios Apple", "3. Accesorios Xiaomi", "4. Salir")
                        for i in opcionarea2:
                            print(i)
                        
                        opcion_categoria_elegida = input("Ingrese la opción deseada: ")

                        if opcion_categoria_elegida == "1":
                            print("Menu de Accesorios Samsung")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            samsung_accesorios.append(producto)
                            print("Producto agregado exitosamente.")
                        elif opcion_categoria_elegida == "2":
                            print("Menu de Accesorios Apple")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            apple_accesorios.append(producto)
                            print("Producto agregado exitosamente.")     
                        elif opcion_categoria_elegida == "3":
                            print("Menu de Accesorios Xiaomi")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            xiaomi_accesorios.append(producto)
                            print("Producto agregado exitosamente.") 
                        elif opcion_categoria_elegida == "4":
                            return
                        else:
                            print("Opcion invalida")
                    break
            elif accion == 2:
                print("En qué area desea ingresar?")
                opcionborrar= ("1. Teléfonos", "2. Accesorios", "3. Salir")
                for i in opcionborrar:
                    print(i)
                while True:
                    opcion_area_elegida = input("Ingrese la opción deseada: ")
                    while True:
                            if opcion_area_elegida == "1":
                                print("¿En que categoria desea eliminar el producto?")
                                opcioncategoriav = {"1. Teléfonos Samsung", "2. Teléfonos Apple", "3.Teléfonos Xiaomi", "4. Salir"}
                                for i in opcioncategoriav:
                                    print(i)
                                opcion_categoria_elegida = input("Ingrese la opción deseada: ")
                                if opcion_categoria_elegida == "1":
                                    print("Lista de Teléfonos Samsung")
                                    for i in samsung_telefonos:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del samsung_telefonos[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(samsung_telefonos, indent=4))
                                    break
                                elif opcion_categoria_elegida == "2":
                                    print("Lista de Teléfonos Apple")
                                    for i in apple_telefonos:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del apple_telefonos[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(apple_telefonos, indent=4))
                                    break
                                elif opcion_categoria_elegida =="3":
                                    print("Lista de Teléfonos Xiaomi")
                                    for i in xiaomi_telefonos:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del xiaomi_telefonos[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(xiaomi_telefonos, indent=4))
                                    break
                                elif opcion_categoria_elegida =="4":
                                    return
                                else:
                                    print("Opcion invalida")
                            elif opcion_area_elegida == "2":
                                print("Lista de Accesorios")
                                print("Elija en que categoria desea agregar el producto")
                                opcioneselectro = ("1.Accesorios Samsung", "2.Accesorios Apple", "3. Accesorios Xiaomi", "4. Salir")
                                for i in opcioneselectro:
                                    print(i)
                                input("Ingrese la opción deseada: ")

                                if opcioneselectro == "1":
                                    print("Lista de Accesorios Samsung")
                                    for i in samsung_accesorios:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del samsung_accesorios[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(samsung_accesorios, indent=4))
                                    break
                                elif opcioneselectro == "2":
                                    print("Lista de Accesorios Apple")
                                    for i in apple_accesorios:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del apple_accesorios[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(apple_accesorios, indent=4))
                                    break
                                elif opcioneselectro == "3":
                                    print("Lista de Accesorios Xiaomi")
                                    for i in xiaomi_accesorios:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del xiaomi_accesorios[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(xiaomi_accesorios, indent=4))
                                    break
                                elif opcioneselectro == "4":
                                    return
                                
                            else: print("Opcion invalida")
            elif accion == 3:
                print("Que accion desea realizar")
                while True:
                    opcionesmostrartienda= ["1.mostrar todos los productos", "2. Mostrar productos de un area en especifico", "3. Mostrar productos de una categoria especifica", "4. Salir"]
                    for i in opcionesmostrartienda:
                        print(i)
                    eleccion=input("Ingrese la opción deseada: ")
                    if eleccion == "1":
                        print("Mostrando todos los productos")
                        print(j.dumps(Areas, indent=4))
                    elif eleccion == "2":
                        print("Area que desea visualizar")
                        categorias = {"1. Teléfonos", "2.Accesorios"}
                        for i in categorias:
                            print(i)
                        eleccion = input("Ingrese la opción deseada: ")
                        if eleccion == "1":
                            print("Mostrando todos los productos de la categoria Teléfonos")
                            print(j.dumps(Telefonos, indent=4))
                            break
                        elif eleccion == "2":
                            print("Mostrando todos los productos de la categoria de Accesorios")
                            print(j.dumps(Accesorios, indent=4))
                            break
                        else: print("Opcion invalida")
                    elif eleccion == "3":
                        print("Mostrando productos por categoria")
                        while True:
                            categoria = {"1. Teléfonos Samsung", "2. Teléfonos Apple","3. Telefonos Xiaomi", "4. Accesorios Samsung", "5. Accesorios Apple", "6.Accesorios Xiaomi", "7. Salir"}
                            for i in categoria:
                                print(i)
                            eleccion = input("Ingrese la opción deseada: ")
                            if eleccion == "1":
                                print("Mostrando todos los teléfonos de Samsung")
                                print(j.dumps(samsung_telefonos, indent=4))
                                break
                            elif eleccion =="2":
                                print("Mostrando todos los teléfonos de Apple")
                                print(j.dumps(apple_telefonos, indent=4))
                                break
                            elif eleccion =="3":
                                print("Mostrando todos los Teléfonos de Xiaomi")
                                print(j.dumps(xiaomi_telefonos, indent=4))
                                break
                            elif eleccion =="4":
                                print("Mostrando todos los Accesorios de Samsung")
                                print(j.dumps(samsung_accesorios, indent=4))
                                break
                            elif eleccion =="5":
                                print("Mostrando todos los Accesorios de Apple")
                                print(j.dumps(apple_accesorios, indent=4))
                                break
                            elif eleccion =="6":
                                print("Mostrando todos los Accesorios de Xiaomi")
                                print(j.dumps(xiaomi_accesorios, indent=4))
                                break
                            elif eleccion =="7":
                                return
                            
                            else: print("Opcion invalida")
                        return
                    elif eleccion == "4":
                        return  
                    else: print("Opcion invalida")     
            elif accion == 4:
                New_Area = input("Agregue nueva área -> ")
                Areas.append( New_Area )
                #Crear nueva Area
                
            elif accion == 5:
                return

            else: print("Opcion invalida")
def programaGerente():
    print("Que accion desea realizar")
    while True:
        opcionesmostrartienda= ["1.mostrar todos los productos", "2. Mostrar productos de un area en especifico", "3. Mostrar productos de una categoria especifica", "4. Salir"]
        for i in opcionesmostrartienda:
            print(i)
        eleccion=input("Ingrese la opción deseada: ")
        if eleccion == "1":
            print("Mostrando todos los productos")
            print(j.dumps(Areas, indent=4))
        elif eleccion == "2":
            print("Area que desea visualizar")
            categorias = {"1. Teléfonos", "2. Accesorios"}
            for i in categorias:
                print(i)
            eleccion = input("Ingrese la opción deseada: ")
            if eleccion == "1":
                print("Mostrando todos los productos de la categoria Teléfonos")
                print(j.dumps(Telefonos, indent=4))
                break
            elif eleccion == "2":
                print("Mostrando todos los productos de la categoria Accesorios")
                print(j.dumps(Accesorios, indent=4))
                break
            else: print("Opcion invalida")
        elif eleccion == "3":
            print("Mostrando productos por categoria")
            while True:
                categoria = {"1. Teléfonos Samsung", "2. Teléfonos Apple","3. Teléfonos Xiaomi", "4. Accesorios Samsung", "5. Accesorios Apple", "6. Accesorios Xiaomi", "7. Salir"}
                for i in categoria:
                    print(i)
                eleccion = input("Ingrese la opción deseada: ")
                if eleccion == "1":
                    print("Mostrando todos los productos de la categoria Teléfonos Samsung")
                    print(j.dumps(samsung_telefonos, indent=4))
                    break
                elif eleccion =="2":
                    print("Mostrando todos los productos de la categoria Teléfonos Apple")
                    print(j.dumps(apple_telefonos, indent=4))
                    break
                elif eleccion =="3":
                    print("Mostrando todos los productos de la categoria Teléfonos Xiaomi")
                    print(j.dumps(xiaomi_telefonos, indent=4))
                    break
                elif eleccion =="5":
                    print("Mostrando todos los productos de la categoria Accesorios Samsung")
                    print(j.dumps(samsung_accesorios, indent=4))
                    break
                elif eleccion =="6":
                    print("Mostrando todos los productos de la categoria Accesorios Xiaomi")
                    print(j.dumps(xiaomi_accesorios, indent=4))
                    break
                elif eleccion =="7":
                    return
                                
                else: print("Opcion invalida")
            return
        elif eleccion == "4":
            menu_principal()
        else: print("Opcion invalida")
def programa_vendedor():
    print("Que accion desea realizar")
    while True:
        opcionesventa: List[str] = ["1.Agregar producto al carrito", "2.Eliminar producto del carrito", "3.Finalizar compra", "4.Salir"]
        for i in opcionesventa:
            print(i)
        eleccion: str = input("Ingrese la opción deseada: ")
        if eleccion == "1":
            print("A que area desea ingresar ? ")
            areas= ["1. Teléfonos", "2.Accesorios", "3. Salir"]
            for i in areas:
                print(i)
            eleccion = input("Ingrese la opción deseada: ")
            if eleccion == "1":
                categorias={"1. Teléfonos Samsung", "2. Teléfonos Apple","3. Teléfonos Xiaomi", "4.Salir"}
                for i in categorias:
                    print(i)
                eleccion = input("Ingrese la opción deseada: ")
                if eleccion == "1":
                    print("Inventario de Teléfonos Samsung")
                    productos = list(diccionario1.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario1[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            cesta.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "2":
                    print("Inventario de Teléfonos Apple")
                    productos = list(diccionario2.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario2[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            cesta.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "3":
                    print("Inventario de Teléfonos Xiaomi")
                    productos = list(diccionario3.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario3[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            cesta.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "4":
                    return 
            elif eleccion == "2":
                categorias2={"1. Accesorios Samsung", "2. Accesorios Apple", "3. Accesorios Xiaomi", "4.Salir"}
                for i in categorias2:
                    print(i)
                eleccion = input("Ingrese la opción deseada: ")
                if eleccion == "1":
                    print("Inventario de Accesorios Samsung")
                    productos = list(diccionario2.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario2[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            cesta.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "2":
                    print("Inventario de Accesorios Apple ")
                    productos = list(diccionario5.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario5[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))
                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            cesta.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "3":
                    print("Inventario de Accesorios Xiaomi")
                    productos = list(diccionario6.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario6[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            cesta.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "4":
                    return 
            elif eleccion == "3":
                return
        elif eleccion == "2":
            print("Borrar Articulos del Carrito")
            while True:
                print(j.dumps([item for item in cesta], indent=4))
                eleccion_producto = input("¿Qué item deseas eliminar del carrito? (Ingresa 'q' para salir): ")
                if eleccion_producto.lower() == 'q':
                    break
                try:
                    eleccion_producto = int(eleccion_producto) - 1
                    eliminado = cesta[eleccion_producto]
                    del cesta[eleccion_producto]
                    print(f"El item {eliminado} ha sido eliminado del carrito.")
                except (ValueError, IndexError):
                    print("Entrada inválida. Ingresa un número de la lista o 'q' para salir.")
        elif eleccion == "3":
            msj = py.figlet_format("Fin de la compra")
            print(msj)
            total = 0
            for i, item in enumerate(cesta):
                precio = item["precio"]
                total += precio
                print(f"{i+1}. {item['Nombre']} - ${precio:.2f}")
            print(f"Total: ${total:.2f}")
            break
def menu_principal():
        while True:
            opciones = ["1. Administrador", "2. Gerente", "3. Empleado", "4. Salir"]
            print("Bienvenido al programa, ¿En qué nivel de acceso desea ingresar?")
            for i in opciones:
                print(i)
            inicio = input()
            if inicio == "1":
                while True:
                    print("Elija una opción\n")
                    opciones1 = ["1. Iniciar sesión", "2. Volver al menú"]
                    for i in opciones1:
                        print(i)
                    selector = input("Ingrese una opción: ")
                    if selector == "1":
                        while True:
                            user_ = "Mauricio"
                            password_ = "Hakuna Matata"
                            print('Introducir datos de administrador o escriba "s" para volver al menú')
                            print('Nombre de Usuario:')
                            user = input()
                            if user == "s":
                                menu_principal()
                            print('Contraseña:')
                            pwd = input()
                            if user == user_ and pwd == password_:
                                msj = py.figlet_format("Administrador:")
                                print(msj)
                                print("Bienvenido administrador, ¿qué desea hacer hoy?")
                                programa_Admin()
                                break
                            else:
                                print("Usuario o contraseña incorrecto")
                        break
                    elif selector == "2":
                        menu_principal()
                    else:
                        print("Dato ingresado no aceptado, inténtelo otra vez")
            elif inicio == "2":
                while True:
                    print("Ingrese datos gerenciales")
                    gerente = "Ana"
                    contraseñagerente = "Los tigres del norte"
                    gerent = input("Ingrese usuario: ")
                    if gerent == "s":
                        menu_principal()
                    contra = input("Ingrese contraseña: ")
                    if gerent == gerente and contra == contraseñagerente:
                        msj = py.figlet_format("Gerente:")
                        print("Bienvenid@ Generente")
                        programaGerente()
                        break
                    else:
                        print("Datos erróneos")
            elif inicio == "3":
                print("Bienvenido Empleado")
                class user:
                    def __init__(self, nom, pwd):
                        self.nom = nom
                        self.pwd = pwd

                t1 = user("Alicia", "Metanme en arroz")
                t2 = user("Nestor", "no estoy")
                t3 = user("Jonathan", "Mangito con Sal")
                t4 = user("Juan",   "playa y arena")
                trabajadores = [t1, t2, t3,t4]

                n = input("Ingrese su usuario o escriba s para volver al menú principal: ")
                if n == "s":
                    menu_principal()
                p = input("Ingrese contraseña: ")
                if p == "s":
                    menu_principal()

                k = 0

                for i in range(len(trabajadores)):
                    if trabajadores[i].nom == n and trabajadores[i].pwd == p:
                        print("************************************************")
                        print(trabajadores[i].nom, "- BIENVENIDO AL PERFIL  DE TRABAJADORES")
                        print("************************************************")
                        k = 1
                        programa_vendedor()
                        break

                if k == 0:
                    print("Intente nuevamente")
            elif inicio == "4":
                break
            else:
                print("Dato ingresado no aceptado, inténtelo otra vez")

menu_principal()
