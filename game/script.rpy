# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define carlos = Character("Carlos")
define Juan = Character("Juan")
define rosa = Character("Rosa")
define unkown = Character("???") 

define Luis = Character("Luis")
#Image of Carlos the Guard
image carlos_ch = "carlos/carlos_neutral.png"
image carlos_ch_angry = "carlos/carlos_angry.png"
image carlos_ch_poker_face = "carlos/carlos_porker_face.png"
image carlos_ch_happy ="carlos/carlos_happy.png"
image carlos_ch_concern = "carlos/carlos_concerned.png"

#Image of Juan the main character
image Juan_main_ch = "Juan/Juan_neutral.png"

#Image of Rosa the milf
image rosa_anger = "rosa/rosa_furiosa.png"
image rosa_serious = "rosa/rosa_seria.png"
image rosa_sorprise = "rosa/rosa_sorprendida.png"

#load music assets


image bg_mall = "bg/mall.jpg"

transform half_size:
    zoom 0.39
    left

transform double_size:
    zoom 3.0
    right
        

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

  

    Juan "Bueno siendo sincero mi padre humano tenía razón sobre que debí estudiar otra carrera en mi país natal, no pude encontrar trabajo de lo que estudie. La parte más estresante fue que la gran mayoría de las ofertas laborales pedían que tuvieran una experiencia mayor a la de 5 años"    

    Juan "¿COMO CHINGADOS UN UNIVERSITARIO QUE RECIEN SE GRADUA PUEDE CONSEGUIR TAL COSA? Ya ni hablemos que los sueldos que daban esas empresas eran muy inferiores al que deberían dar en realidad."

    Juan "Es por eso que un mi tío me convenció de tratar de ir al otro lado a experimentar el sueño americano. Actualmente vivo en Volcadera haciendo cualquier tipo de trabajo como vigilante, barrendero, lavaplatos entre otras cosas"

    Juan "Caminando por un Wallmart cercano a mi departamento me encontré al primo de un viejo amigo de la universidad al parecer mi amigo Daniel también vive aquí y anda buscando un vigilante para un bar donde el es el dueño."

    Juan "No me gusta para nada trabajar de eso me frustra demasiado, pero esa suscripción ala cuenta de onlydinos de ese parasaurio azul femboy no se va a pagar solo."


    scene bg_mall

    play music "Nintendo Wii - Mii Channel Theme.ogg"
    show Juan_main_ch at half_size

    Juan "Y veme aquí entrando directamente hacia la plaza de Volcadera uno de los mayores lugares donde hay mayor ocurrencia y donde prosperan varios negocios, diría que  podría competir  con aquel barrio ubicado en Skin Row creo que se llamaba Little Troodon"
    Juan "Creo que me estoy desviando vine específicamente por ese empleo. Aunque Admito que el lugar esta bonito, esos 4 pisos lleno de decoraciones góticas y el jardín de en medio da buena vibra "
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    Juan "Ando usando un elevador circular que esta ubicado junto a las salidas en el 2do piso"

    Juan "*Lo malo es que como esta pequeño y es muy usado (a pesar que haya escaleras)  lo que hace que inevitablemente huela mucho obo. Tio agradezco desde el fondo de mi alma que me hayas invitado a tus partidas de yugidino en la frikiplaza de nuestra ciudad para poder desarrollar inmunidad a este hedor"

    Juan "*Lo bueno es que el elevador tiene clima y reproduce música de Nintendo. Conociendo como es la empresa no me sorprendaria que la compañía los demande por"

    unkown "Tu si que eres muy grosero"

    Juan ": ¿Quién dijo eso? *Giro mi cabeza hacia la derecha e izquierda y no veo absolutamente  nada* Deben ser los nervios o estoy desarrollando ezquisofrenia, por si las dudas voy a descansar mas y dejar de pasármela todo el dia viendo las funas que hay en X."

    Juan "Bueno parece que el elevador bajo, es hora de salir"

    Juan "Estoy en la planta baja a mi alrededor hay puestos de comidas como un snootbucks, taco shell, un  tomboyters entre otros puestos de comida y justamente en medio esta mi destino"
    # These display lines of dialogue.

    play  music "Soft Jazz Relaxing Music.ogg"

    Juan "Ya estoy dentro y pues el bar se ve muy lindo con esa decoración que tiene. Me percato que al lado derecho está sentado un guardia Anquilosaurio color café con cara de pocos amigos que se me queda viendo raro. Al lado suyo esta un velociraptor color naranja más amigable le preguntare sobre donde esta Daniel"


    Juan "Buenas sabes de casualidad ¿Dónde puedo encontrar Daniel? Es un tiburón color azul con manchas blancas en la frente que me cito para el puesto de"
    # This ends the game.

    Luis "Hmmm.. ¿Daniel? Daniel no me suena ¿No te referias a Daniela? Puedes preguntarle a la Jefa. Su oficina se encuentra ala derecha subiendo esas escaleras."

    Juan "Muchas gracias. *Curioso siempre pensé que Daniel era hijo único y no me sorprende el hecho de que no sea el verdadero jefe del local. A Daniel siempre le gustaba presumir cosas que no tenia*"

    Juan "Subo las escaleras y llego a la oficina. Toco la puerta y"

    unkown "Carlos ya te dije que no planeare en renovar tu contrato si sigues con esa actitud"

    Juan "Disculpe mi nombre es Juan vino a buscar a Daniel sobre la solicitud de Vigilante debido a que"

    unkown " Esa voz… Adelante pasa"
    return
