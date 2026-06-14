import pygame 
import os 
import random
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

def canciones(cancion):
 pygame.mixer.init()
 pygame.mixer.music.load(nombre_openings[cancion])
 pygame.mixer.music.play()

 while pygame.mixer.music.get_busy():
    pass

def reproducir_op_azar():
 contador_positivo = 0
 contador_negativo = 0
 while True:
  print(f"has acertado: {contador_positivo}")
  print(f"has fracasado: {contador_negativo}")
  op_azar = random.choice(claves)
  canciones(op_azar)
  cancion = input("ingrese la cancion: ")
  if cancion == op_azar:
      print("correcto")
      contador_positivo +=1
  else:
     print("incorrecto")
     contador_negativo += 1
