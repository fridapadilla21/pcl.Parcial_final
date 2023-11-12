# codigo de replit: https://replit.com/join/sjowyitcwu-frida-paulinapa
nombre = input("Coloca tu nombre: ")
while True:
  print(" ")
  llamado = input("Llama a Alexa: ").split()
  
  c= llamado.count('alexa')
  if c == 1:
    print(f"¡Hola {nombre}!")
    break
  elif c > 1:
    print(f"Tranqui {nombre} solo di mi nombre una vez")
  else:
    print(f"No dijiste mi nombre {nombre}")
