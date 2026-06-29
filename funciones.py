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
    
def comparacion_palabras_multiples(nombre_usuario, nombre_ingles, nombre_japones):
    similitud_japones = SequenceMatcher(None, nombre_usuario.lower(),nombre_ingles.lower()).ratio()
    similitud_ingles = SequenceMatcher(None, nombre_usuario.lower(),nombre_japones.lower()).ratio()
    if similitud_japones >= 0.8 or similitud_ingles >=0.8:
        return True
    else:
        return False    
    

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

def duracion_op(ruta_op):
    sonido = pygame.mixer.Sound(op.ruta)
    duracion = sonido.get_length()
    return duracion

def reproductor(ruta_op,inicio,final):
    pygame.mixer.music.load(ruta_op)
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
    
    
#Reproduce 10 segundos al azar de la ruta de op que se le pase depues pregunta el nombre del anime y devuelve true si es correcto y false si no
#ademas te da la opcion de extender el audio hasta reproducirlo completo    
def Reproductor_op(ruta_op,nombre_ingles,nombre_japones):
    #Datos
    duracion = duracion_op(ruta_op)
    inicio_azar = random.randint(0,duracion-10) 
    final_aumento = 10
    
    #ejecucion
    reproductor(ruta_op,inicio_azar,final_aumento)
    op_usuario = input("ingrese el nombre del opening, ingrese 's' para aumentar el tiempo")
    if op_usuario == comparacion_palabras_multiples(op_usuario,nombre_ingles,nombre_japones):
        pass

     
def prueba():
    p = comparacion_palabras_multiples("jhytrew","Future Diary","Mirai Nikki")
    print(p)