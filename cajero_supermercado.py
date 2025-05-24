#V 1.0.1
Productos = {
    "Leche": 10,
    "Carne": 15,
    "Jugo": 5,
    "Pan": 3
}
Membresiasdicc = {
    "Bronze": 0.05,
    "Silver": 0.10,
    "Gold": 0.20
}
#Declarando algunas variables para despues
Total = 0
Carrito = []
Comprando = False

Carrito.append(input(f"Actualmente tenemos {list(Productos.keys())}, que desea: ".title()))

#Bucle para llenar el carrito de compra
while Comprando == False:
    Carrito.append(input(f"Que mas desea? {list(Productos.keys())} ".casefold()))
    SeguirComprando = input("Desea seguir comprando? ".casefold())
    
    if SeguirComprando == "no":
        break

#Calcular el precio de todos los productos en el carrito
while Comprando == False:
    if Carrito[0] in Productos:
        ValorDelCarrito = Productos[Carrito[0]]
        Total += ValorDelCarrito
        Carrito.pop(0)
        if Carrito == []:
            break

#Aplicando descuentos de membresias
MembresiaDelUsuario = input(f"Cual es su membresia? {list(Membresiasdicc.keys())}".casefold())

if MembresiaDelUsuario in Membresiasdicc:
    Descuento = Membresiasdicc[MembresiaDelUsuario]
else:
    print("Membresia no valida, no se aplicara descuento")
    
    #Calcular descuentos
PrecioFinal = Total - (Total * Descuento)
print(f"Al tu tener una membresia {MembresiaDelUsuario} se te aplicara un descuento del {Descuento}%")
EleccionFinal = input((f"Tenga en cuenta que pagara un total de {Total}$ menos el {Descuento}% serian {PrecioFinal}$, Confirmar la compra? ".casefold()))
if EleccionFinal == "si":
    print(f"Gracias por su compra, ha gastado {PrecioFinal}$")
    exit()
    
