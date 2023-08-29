#MENU DE OPCIONCIONES
#1. Ingresar producto de bodega
#2. Verificar los productos en bodega
#3. Buscar un producto en la bodega
#4. editar un producto en la bodega
#5. retirar un producto bodega
#6. Salir
#producto: nommbre, codigo, descripcion, foto, precio, cantidadEnBodega,fechaEntradaBodega

opcion=0
print ("1. Ingresar producto de bodega")
print ("2. Verificar los productos en bodega")
print ("3. Buscar un producto en la bodega")
print ("4. editar un producto en la bodega")
print ("5. retirar un producto bodega")
print ("6. Salir")
print ("*******************************************")

productos=[]

while(opcion !=6):
    opcion=0
    print ("1. Ingresar producto de bodega")
    print ("2. Verificar los productos en bodega")
    print ("3. Buscar un producto en la bodega")
    print ("4. editar un producto en la bodega")
    print ("5. retirar un producto bodega")
    print ("6. Salir")
    print ("*******************************************")
    producto={}
    opcion=int(input("Digita la opcion deseada: "))
    if opcion==1:
        producto["nombre"]= input("Digita el nombre del producto: ")
        producto["codigo"]= int(input("Digita el codigo del producto: "))
        producto["descripcion"]= input("Digita la descripcion del producto: ")
        producto["foto"]= input("Digita la URL del producto: ")
        producto["precio"]= float(input("Digita el precio del producto: "))
        producto["stock"]= int(input("Digita el stock del producto: "))
        producto["fechaEntradaBodega"]= input("Digita la fecha de entrada: ")
        productos.append(producto)
        
    elif opcion==2:
        for productoSeleccionado in productos:
            print(f"codigo: {productoSeleccionado['codigo']}")
            print(f"nombre: {productoSeleccionado['nombre']}")
            print(f"descripcion: {productoSeleccionado['descripcion']}")
            print(f"foto: {productoSeleccionado['foto']}")
            print(f"cantidad en bodega: {productoSeleccionado['stock']}")
            print(f"fecha de entrada: {productoSeleccionado['fechaEntradaBodega']}\n")
        
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        print("opcion invalida, vuelve a intentarlo \n")
    