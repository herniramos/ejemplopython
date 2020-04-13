"""4. Dada una lista con preguntas que se responden por ’si’ o ’no y sus respuestas correctas, armar
un juego que muestre cada una de las preguntas al jugador, verifique si es correcta o no e
incremente el puntaje en caso de acertar. Se debe seleccionar en forma aleatoria la pregunta
a mostrar y eliminarla una vez que ya la mostraron. El juego finaliza cuando no hay más
perguntas en la lista. Un ejemplo de la lista con las preguntas podría ser:
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['
Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', '
no]]"""

import random

preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no' ]]
aleatorio = random.choice(preguntas)
puntaje=0.0
for i in range(len(preguntas)):
    print(aleatorio[0]) 
    respuesta=input(print(" ingrese la respuesta , si o no : " )) 
    if respuesta== aleatorio[1]:
        print("la rta es correcta")
        puntaje+=1
    else:
        print("la respuesta es incorrecta")
    
    aleatorio = random.choice(preguntas)
    preguntas.remove(aleatorio)
    
    print("____________________________________")

    print("se imprime la lista con la pregunta que ya salio eliminada " ,  preguntas)

print("el puntaje es " , puntaje)




 





