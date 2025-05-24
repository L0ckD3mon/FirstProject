#V 1.0.1
Products = {
    "Leche": 10,
    "Carne": 15,
    "Jugo": 5,
    "Pan": 3
}
Membership = {
    "Bronze": 0.05,
    "Silver": 0.10,
    "Gold": 0.20
}
#Declarando algunas variables para despues
total = 0
car = []
buying = True

car.append(input(f"Actualmente tenemos {list(Products.keys())}, que desea: ".title()))

#Bucle para llenar el carrito de compra
while buying == True:
    car.append(input(f"Que mas desea? {list(Products.keys())} ".casefold()))
    keepBuying = input("Desea seguir comprando? ".casefold())
    
    if keepBuying == "no":
        buying = False

#Calcular el precio de todos los productos en el carrito
while buying == False:
    if car[0] in Products:
        carValue = Products[car[0]]
        total += carValue
        car.pop(0)
        if car == []:
            break
            
#Aplicando descuentos de membresias
userMembership = input(f"Cual es su membresia? {list(Membership.keys())}".casefold())

if userMembership in Membership:
    discount = Membership[userMembership]
else:
    print("Membresia no valida, no se aplicara descuento")
    
    #Calcular descuentos
finalPrice = total - (total * discount)
print(f"Al tu tener una membresia {userMembership} se te aplicara un descuento del {discount}%")
finalChoice = input((f"Tenga en cuenta que pagara un total de {total}$ menos el {discount}% serian {finalPrice}$, Confirmar la compra? ".casefold()))
if finalChoice == "si":
    print(f"Gracias por su compra, ha gastado {finalPrice}$")
    exit()
    
