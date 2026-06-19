import pygame 
import random
import time
from difflib import SequenceMatcher
pygame.mixer.init()


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
       pygame.mixer.music.play(start=inicio)
       time.sleep(aumento)
       pygame.mixer.music.stop()
      else:
       while True:
        aumento += 10
        decremento +=10
        print("ejecutar")
        pygame.mixer.music.play(start=inicio-decremento)
        time.sleep(aumento)
        pygame.mixer.music.stop()
 def  aciertos_op(nombre_usuario,nombre_real):
       similitud = SequenceMatcher(None,nombre_usuario,nombre_real)
       if similitud > 0.8:
          correctos += 1
       else:
          incorrectos +=1
       print(f"""
             correctos: {correctos}  
             incorrectos: {incorrectos}
               
               
               """)
    
    
      
 
