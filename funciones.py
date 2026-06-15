import pygame 
import os 
import random
pygame.mixer.init()
#Datos sueltos 





#LISTAS
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
  "jujutsu" : "audios anime/JUJUTSU KAISEN Opening.mp3",
    
}

claves = nombre_openings.keys()
claves = list(claves)
def calcular_duracion_cancion(cancion):
    audio = pygame.mixer.Sound(cancion)
    duracion = audio.get_length()
    return duracion


def reproductor_azar():
 op_azar = random.choice(claves)
 pygame.mixer.music.load(nombre_openings[op_azar])
 pygame.mixer.music.play()

 while pygame.mixer.music.get_busy():
    pass


  
  