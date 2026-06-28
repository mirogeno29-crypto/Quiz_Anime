import funciones
funciones.limpiar_pantalla()


while True:
 jugar = input("bienevenido al Quiz de anime ¿desea jugar? 1.si 2.no: ")
 if jugar == "1" or jugar == "si":
  funciones.limpiar_pantalla()
  funciones.reproductor_final()
 elif jugar == "2" or jugar == "no":
  print("Felicitaciones haz dado un paso para dejar de ser virgen")
  break
         
     