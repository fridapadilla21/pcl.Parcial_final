#link de replit https://replit.com/join/xznjlwnmnq-frida-paulinapa

contador = 0
lecturas= int(input("¿Cuantas lecturas tienes? "))

lecorrectas = 0
leincorrectas = 0

while contador < lecturas:
  contador += 1
  temp = int(input(f"Inserta la temperatura {contador}: "))
  if 10 <= temp <= 40:
    lecorrectas += 1
  else:
    leincorrectas += 1
