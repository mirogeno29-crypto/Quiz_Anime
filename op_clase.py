import pygame 
import random
import time
from difflib import SequenceMatcher
import os
pygame.mixer.init()
def limpiar_pantalla():
       os.system("cls" if os.name == "nt" else "clear")


class op:
 op_azar = None
 def seleccion_cancion_azar(): 
  nombre_openings = {
 "Future Diary":  "audios anime/Mirai Nikki.mp3",   
  "Neon Genesis Evangelion":   "audios anime/Evangelion.mp3",
  "JoJo's Bizarre Adventure" : "audios anime/jojo op2.mp3",
  "Demon Slayer" : "audios anime/kimetsu no yaiba.mp3",
  "Miss Kobayashi's Dragon Maid" : "audios anime/Miss Kobayashi's Dragon Maid.mp3",
  "My Hero Academia" : "audios anime/My heroe academia.mp3",
  "Monogatari Series" : "audios anime/Nekomonogatari.mp3",
  "One Piece" : "audios anime/one piece.mp3",
  "Attack on Titan" : "audios anime/shingeki no kiojin.mp3",
  "Jujutsu Kaisen" : "audios anime/JUJUTSU KAISEN Opening.mp3",}
  claves = nombre_openings.keys()
  claves = list(claves)
  op.op_azar = random.choice(claves)
  
  return nombre_openings[op.op_azar]

 def calcular_duracion_cancion(cancion):
    audio = pygame.mixer.Sound(cancion)
    duracion = audio.get_length()
    duracion = int(duracion)
    return duracion

 def reproductor_incremento():
    correcto = 0
    incorrecto = 0
    while True:
     cancion = op.seleccion_cancion_azar()
     duracion = op.calcular_duracion_cancion(cancion)
     print(op.op_azar)
     aumento = 10
     decremento = 0
     inicio = random.randint(0,duracion-10)
     falta_de_cancion= duracion-inicio
     pygame.mixer.music.load(cancion)
     pygame.mixer.music.play(start=inicio)
     time.sleep(aumento)
     pygame.mixer.music.stop()
     while True:
      aumentar = int(input("quieres aumentar la duracion de la cancion 1.si 2.no: "))
      if aumentar == 1:
       aumento += 10
       if falta_de_cancion >= aumento:
        print("ejecutar1")
        pygame.mixer.music.play(start=inicio)
        time.sleep(aumento)
        pygame.mixer.music.stop()
       elif (aumento+decremento) >=duracion:
          print("ejecutar 3")
          pygame.mixer.music.play()
          time.sleep(duracion)
          pygame.mixer.music.stop()
       else:
         aumento += 10
         decremento +=10
         print("ejecutar2")
         pygame.mixer.music.play(start=inicio-decremento)
         time.sleep(aumento)
         pygame.mixer.music.stop()
      elif aumentar == 2:
         op_usario = input("ingrese el nombre del anime: ")
         if op.aciertos_op(op_usario,op.op_azar):
            correcto +=1
            print(f"""¡CORRECTO!
                       Acertadas: {correcto}
                       Incorrectas: {incorrecto}
                  """)
            break
         else:
            incorrecto +=1
            print(f"""INCORRECTO
                   Acertadas: {correcto}
                   Incorrectas: {incorrecto}
                  
                  """)
            break
 def  aciertos_op(nombre_usuario,nombre_real):
       nombre_usuario = nombre_usuario.lower().strip()
       nombre_real =nombre_real.lower().strip()
       similitud = SequenceMatcher(None,nombre_usuario,nombre_real).ratio()
       if similitud > 0.8:
          return True
       else:
          return False
       
 
    
      
 
