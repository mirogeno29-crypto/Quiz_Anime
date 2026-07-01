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
    
Animes = {
    
"Mirai nikki" : clases.Mirai_Nikki,   
"evangelion" : clases.Shin_Seiki_Evangelion,
"Jojos": clases.JoJo_no_Kimyou_na_Bouken,
"Kimetsu no yaiba": clases.Kimetsu_no_Yaiba,
"Kobayashi": clases.Kobayashi_san_Chi_no_Maid_Dragon,
"Bokuno heroe": clases.Boku_no_Hero_Academia,
"Monogatari": clases.Monogatari,
"One piece": clases.Wan_Piisu,
"Shingeki no Kyojin": clases.Shingeki_no_Kyojin,
"Jujutsu kaisen": clases.Jujutsu_Kaisen,
}    
    
    
def comparacion_palabras_multiples(nombre_usuario, nombre_ingles, nombre_japones):
    similitud_japones = SequenceMatcher(None, nombre_usuario.lower(),nombre_ingles.lower()).ratio()
    similitud_ingles = SequenceMatcher(None, nombre_usuario.lower(),nombre_japones.lower()).ratio()
    if similitud_japones >= 0.8 or similitud_ingles >=0.8:
        return True
    else:
        return False    
    

def duracion_op(Anime):
    sonido = pygame.mixer.Sound(Anime.ruta)
    duracion = sonido.get_length()
    return duracion

def reproductor(anime,inicio,final):
    pygame.mixer.music.load(anime.ruta)
    pygame.mixer.music.play(start= inicio)
    time.sleep(final)
    pygame.mixer.music.stop()

# ejecuat todo lo de william y de vuelve correcto o incorrecto si el usuario acerto o no
def Reproductor_op(Anime):
    duracion = int(duracion_op(Anime))
    inicio  = random.randint(0,duracion-10) 
    final  = 10
    while True:
     reproductor(Anime,inicio,final)
     op_usuario = input("ingrese el nombre del opening, ingrese 's' para aumentar el tiempo: ")
     op_usuario = op_usuario.lower()
     if  comparacion_palabras_multiples(op_usuario,Anime.nombre_ingles,Anime.nombre_japones):
        print("CORRECTO")
        print("if 1")
        return True
     elif op_usuario == "s":
         print("if 2")
         if (inicio + final) < duracion-8:
             final += 10
             print("if 3")
         elif inicio > 0:
              inicio -= 10
              final = duracion - inicio
              print("if 4")
              if inicio < 0:
                  print("if 5")
                  inicio = 0
                  final = duracion
              
     else:
        print("INCORRECTO")
        return False          
               
               
               
               
def ejecucion():
    Correctas = 0
    incorrectas = 0
     
    
def prueba():
    a = Reproductor_op(Animes["Mirai nikki"])
    print(a)
