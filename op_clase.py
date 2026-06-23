import pygame 
import random
import time
from difflib import SequenceMatcher
import os
from colorama import Fore, Style, init
pygame.mixer.init()
def limpiar_pantalla():
       os.system("cls" if os.name == "nt" else "clear")


class op:
 op_azar = None
 correcto = 0
 incorrecto = 0
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
 nombre_openings_copia = nombre_openings.copy()
 nombre_openings_japones = {
    "Mirai Nikki" : "Future Diary",
    "Shin Seiki Evangelion" : "Neon Genesis Evangelion",
    "JoJo no Kimyou na Bouken": "JoJo's Bizarre Adventure",
    "Kimetsu no Yaiba":"Demon Slayer" ,
    "Kobayashi-san Chi no Maid Dragon": "Miss Kobayashi's Dragon Maid",
    "Boku no Hero Academia": "My Hero Academia",
    "Nekomonogatari": "Monogatari Series",
    "Wan Piisu": "One Piece",
    "shingeki no kyojin": "Attack on Titan",
    "Jujutsu Kaisen": "Jujutsu Kaisen"}
 def seleccion_cancion_azar(): 
  claves = op.nombre_openings.keys()
  claves = list(claves)
  op.op_azar = random.choice(claves)
  
  return op.nombre_openings[op.op_azar]

 def calcular_duracion_cancion(cancion):
    audio = pygame.mixer.Sound(cancion)
    duracion = audio.get_length()
    duracion = int(duracion)
    return duracion

 def reproductor_incremento():
    
    
    while True:
     if not op.nombre_openings:
       op.nombre_openings = op.nombre_openings_copia.copy()
       limpiar_pantalla()
       print(f"""
opcion correcta: {op.op_azar}
fin del juego tus puntuaciones son:
{Fore.GREEN}Acertadas: {op.correcto}{Style.RESET_ALL}
{Fore.RED}Incorrectas: {op.incorrecto}{Style.RESET_ALL}
             """)
       return
     cancion = op.seleccion_cancion_azar()
     op.nombre_openings.pop(op.op_azar)
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
      aumentar = (input("ingrese el nombre del anime, si quieres aumentar la duracion de la cancion ingrese 1: "))
      if aumentar == "1":
       aumento += 10
       if falta_de_cancion >= aumento:
        pygame.mixer.music.play(start=inicio)
        time.sleep(aumento)
        pygame.mixer.music.stop()
       elif (aumento+decremento) >=duracion:
          pygame.mixer.music.play()
          time.sleep(duracion)
          pygame.mixer.music.stop()
       else:
         decremento +=10
         pygame.mixer.music.play(start=inicio-decremento)
         time.sleep(aumento)
         pygame.mixer.music.stop()
      else:
         if op.aciertos_op(aumentar,op.op_azar):
            op.correcto +=1
            limpiar_pantalla()
            print(f"""
{Fore.GREEN}¡CORRECTO!{Style.RESET_ALL}
{Fore.GREEN}Acertadas: {op.correcto}{Style.RESET_ALL}
{Fore.RED}Incorrectas: {op.incorrecto}{Style.RESET_ALL}
                  """)
            break
         else:
            op.incorrecto +=1
            limpiar_pantalla()
            print(f"""
{Fore.RED}INCORRECTO{Style.RESET_ALL}
Opcion correcta: {op.op_azar}
{Fore.GREEN}Acertadas: {op.correcto}{Style.RESET_ALL}
{Fore.RED}Incorrectas: {op.incorrecto}{Style.RESET_ALL}
                  
                  """)
            break
 def  aciertos_op(nombre_usuario,nombre_real):
       nombre_usuario = op.convertir_japones_a_ingles(nombre_usuario)
       nombre_usuario = nombre_usuario.lower().strip()
       nombre_real =nombre_real.lower().strip()
       similitud = SequenceMatcher(None,nombre_usuario,nombre_real).ratio()
       if similitud > 0.8:
          return True
       else:
          return False
       
 def convertir_japones_a_ingles(japones):
      japones = japones.lower().strip()
      claves = op.nombre_openings_japones.keys()
      claves = list(claves)
      for i in claves:
       e = i.lower().strip()
       similitud = SequenceMatcher(None,japones,e).ratio()
       if similitud > 0.8:
          return op.nombre_openings_japones[i]
      return japones
    
       
    
      
    
      
 
