# link: https://replit.com/join/xtlnjqzamj-frida-paulinapa

clitotales = 0 #clientes totales
clisi = 0 #clientes qeu no compraron
clino = 0 #clientes que no compraron
vavendidas = {"Varita de Saúco" : 0, "Varita de espino" : 0, "Varita de sauce" : 0, "Varita de acebo": 0} #Varitas vendidas

while True:
  print(" ")
  entra = input("¿Entro un cliente? (si/no): ")
  if entra == "si":
    break
    
  clitotales += 1
  
  comprar_algo = input("¿Compro algo? (si/no): ")

  if comprar_algo == "si":
    clisi +=1
    print(" ")
    print("Existen las siguientes varitas:")
    print(" ")
    print("1) Varita de saúco")
    print("2) Varita de espino")
    print("3) Varita de sauce")
    print("4) Varita de acebo")
    varita_comprada= input("¿Que varrita compró? Elige(1, 2, 3 o 4)")
    
    if varita_comprada in ['1', '2', '3', '4']:
      varita_elegida = {
        '1': 'Varita de saúco', 
        '2': 'Varita de espino', 
        '3':  'Varita de sauce', 
        '4': 'Varita de acebo'
      }[varita_comprada]
      
      vavendidas[varita_elegida] +=1
    else: 
      print("Opcion no valida. No se registrara la compra")
  else: 
    clino += 1

print(" ")
print(f"Clientes totales: {clitotales}")
print(f"Clientes que compraon: {clisi}")
print(f"Clientes que no compraron: {clino}")
print(" ")
print("Hoy se vendieron")
print(f"{vavendidas['Varita de saúco']} varitas de sauco")
print(f"{vavendidas['Varita de espino']} varitas de espino")
print(f"{vavendidas['Varita de sauce']} varitas de sauce")
print(f"{vavendidas['Varita de acebo']} varitas de acebo")
