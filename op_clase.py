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
#[ruta,nombre_japones,nombre_ingles,nombre_cancion,artista_cancion,temporada_utilizo,numero_opening]
 mirai_nikki = ["audios anime/Mirai Nikki.mp3","Mirai Nikki", "Future Diary", "Kuusou Mesorogiwi", "Yousei Teikoku", "Temporada 1", 1]
 shin_seiki_evangelion = ["audios anime/Evangelion.mp3","Shin Seiki Evangelion", "Neon Genesis Evangelion", "A Cruel Angel's Thesis", "Yoko Takahashi", "Temporada 1", 1]
 jojo_no_kimyou_na_bouken = ["JoJo no Kimyou na Bouken", "JoJo's Bizarre Adventure", "Sono Chi no Sadame", "Hiroaki Tommy Tominaga", "Phantom Blood", 1]
 kimetsu_no_yaiba = ["audios anime/kimetsu no yaiba.mp3","Kimetsu no Yaiba", "Demon Slayer", "Gurenge", "LiSA", "Temporada 1", 1]
 kobayashi_san_chi_no_maid_dragon = ["audios anime/Miss Kobayashi's Dragon Maid.mp3","Kobayashi-san Chi no Maid Dragon", "Miss Kobayashi's Dragon Maid", "Aozora no Rhapsody", "fhána", "Temporada 1", 1]
 boku_no_hero_academia = "audios anime/My heroe academia.mp3",["Boku no Hero Academia", "My Hero Academia", "The Day", "Porno Graffitti", "Temporada 1", 1]
 nekomonogatari = ["audios anime/Nekomonogatari.mp3","Nekomonogatari", "Monogatari Series", "Chocolate Insomnia", "Yui Horie", "Kuro", 1]
 wan_piisu = ["audios anime/one piece.mp3","Wan Piisu", "One Piece", "We Are!", "Hiroshi Kitadani", "East Blue", 1]
 shingeki_no_kyojin = ["audios anime/shingeki no kiojin.mp3","Shingeki no Kyojin", "Attack on Titan", "Guren no Yumiya", "Linked Horizon", "Temporada 1", 1]
 jujutsu_kaisen = ["audios anime/JUJUTSU KAISEN Opening.mp3","Jujutsu Kaisen", "Jujutsu Kaisen", "Kaikai Kitan", "Eve", "Temporada 1", 1]
 op_azar = None
 correcto = 0
 incorrecto = 0
 nombre_openings = {
 "Future Dia ry": mirai_nikki,
  "Neon Genesis Evangelion":   shin_seiki_evangelion,
  "JoJo's Bizarre Adventure" : jojo_no_kimyou_na_bouken,
  "Demon Slayer" : kimetsu_no_yaiba,
  "Miss Kobayashi's Dragon Maid" : kobayashi_san_chi_no_maid_dragon,
  "My Hero Academia" : boku_no_hero_academia,
  "Monogatari Series" : nekomonogatari,
  "One Piece" : wan_piisu,
  "Attack on Titan" : shingeki_no_kyojin,
  "Jujutsu Kaisen" : jujutsu_kaisen,}
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
       op.correcto = 0
       op.incorrecto = 0
       op
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
    
       
    
      
    
      
 
