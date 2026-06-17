import pygame 
import random
import time
pygame.mixer.init()


class op:
 def seleccion_cancion_azar(): 
  nombre_openings = {
 "Mirai nikki":  "audios anime/Mirai Nikki.mp3",   
  "Evangelion":   "audios anime/Evangelion.mp3",
  "jojos" : "audios anime/jojo op2.mp3",
  "Kimetsu no yaiba" : "audios anime/kimetsu no yaiba.mp3",
  "Mis kobayashi" : "audios anime/Miss Kobayashi's Dragon Maid.mp3",
  "My heroe academia" : "audios anime/My heroe academia.mp3",
  "Nekomonogatari" : "audios anime/Nekomonogatari.mp3",
  "one piece" : "audios anime/one piece.mp3",
  "Shingeki no kyojin" : "audios anime/shingeki no kiojin.mp3",
  "jujutsu" : "audios anime/JUJUTSU KAISEN Opening.mp3",}
  claves = nombre_openings.keys()
  claves = list(claves)
  op_azar = random.choice(claves)
  return nombre_openings[op_azar]

 def calcular_duracion_cancion(cancion):
    audio = pygame.mixer.Sound(cancion)
    duracion = audio.get_length()
    duracion = int(duracion)
    return duracion

 def reproductor_incremento():
    cancion = op.seleccion_cancion_azar()
    duracion = op.calcular_duracion_cancion(cancion)
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
        decremento +=10
        print("ejecutar")
        pygame.mixer.music.play(start=inicio-decremento)
        time.sleep(aumento)
        pygame.mixer.music.stop()
    
     
