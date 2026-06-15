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

 def calcular_duracion_cancion():
    audio = pygame.mixer.Sound(op.seleccion_cancion_azar())
    duracion = audio.get_length()
    return duracion

 def reproductor_incremento():
    inicio = random.randint(0, int(op.calcular_duracion_cancion() / 2))
    pygame.mixer.music.load(op.seleccion_cancion_azar())
    pygame.mixer.music.play(start=inicio)

    time.sleep(10)
    pygame.mixer.music.stop()
    
     
