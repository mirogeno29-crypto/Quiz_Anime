import pygame 
import clases
import random
import time
from difflib import SequenceMatcher
import os
from colorama import Fore, Style, init
pygame.mixer.init()

def limpiar_pantalla():
    
    os.system("cls" if os.name == "nt" else "clear")
 
def op_azar():
    
    muchas_clases = {
        
    "monogatari":clases.monogatari,
    "Bokuno Heroe":clases.Boku_no_Hero_Academia,
    "jojos": clases.JoJo_no_Kimyou_na_Bouken,
    "jujutsu_kaisen": clases.Jujutsu_Kaisen,
    "Mirai_Nikki": clases.Mirai_Nikki,
    "One piece": clases.Wan_Piisu,
    "Kobayashi": clases.Kobayashi_san_Chi_no_Maid_Dragon,
    "evanegelion": clases.Shin_Seiki_Evangelion,
    "Shingeki no Kyojin":clases.Shingeki_no_Kyojin,
    "Kimetsu no yaiba": clases.Kimetsu_no_Yaiba,}
    clave = random.choice(list(muchas_clases))
    valor = muchas_clases[clave]
    return valor

def duracion_op(op):
    sonido = pygame.mixer.Sound(op.ruta)
    duracion = sonido.get_length()
    return duracion

def reproductor(op,inicio,final):
    pygame.mixer.music.load(op)
    pygame.mixer.music.play(start= inicio)
    time.sleep(final)
    pygame.mixer.music.stop()

#Reproduce solo 10 segundos de la cancion al azar 
def reproductor_primario(op,inicio):
    #Datos 
    ruta = op.ruta
    final = 10
    
    #ejecucion
    print("ejecucion 1") 
    reproductor(ruta,inicio,final)
    
    
#Reproduce 20 segundos hacia adelante hasta que no hay mas tiempo y empieza a reproducir hacia atras
#hasta que tampoco hay mas tiempo    
def Reproductor_secundario(op,inicio,duracion,final,decremento):
    #Datos
     ruta = op.ruta
     final = final
     falta_terminar = duracion-inicio
     decremento = decremento
     duracion = duracion
     
     #ejecucion
     if final < falta_terminar:
        print("ejecucion 2")
        reproductor(ruta,inicio,final)
        final +=10
     elif final+decremento < duracion:
          print("ejecucion 3")
          reproductor(ruta,inicio-decremento,final)
          decremento += 10
     else:
          return
     
     
     #condiciones


#Reproduce todo el opening completo     
def Reproductor_terciario(op,duracion): 
    ruta = op.ruta
    print("ejecucion 4")
    reproductor(ruta,0,duracion)
         
def reproductor_final():
    #Datos 
    clase_opening = op_azar()
    duracion = int(duracion_op(clase_opening))
    inicio = random.randint(0,duracion-10)
    op_nombres = [clase_opening.nombre_ingles,clase_opening.nombre_ingles]
    final = 10
    decremento = 10
    Correcto = 0
    Incorrecto = 0
    
    #ejecucion
    op_usuario = input("ingrese el nombre del op, o ingrese  s para alargar el audio")
    if op_nombres == "s":
     #Reproductor primario
     reproductor_primario(clase_opening,inicio)
     #reproductor secundario
     Reproductor_secundario(clase_opening,inicio,duracion,final,decremento)
     #Reproductor terciario
     Reproductor_terciario(clase_opening,duracion)
    elif op_usuario in op_nombres:
        print("Correcto")
        
      
     