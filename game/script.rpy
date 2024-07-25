# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Carlos = Character("Carlos", color="#c8ffc8")
define Juan = Character("Juan", color="#ADD8E6")
define Rosa = Character("Rosa" ,color="#FFC0CB")
define unkown = Character("???" ,color="#90EE90") 
define Luis = Character("Luis", color="#FFA500")
define Maria =Character("Maria")
define Daniela = Character("Daniela",color="#90EE90")
define Don = Character("Don")
define Pegaso = Character("Pegaso")
define Reed =Character("Reed")
define narrator = Character(None, what_italic=True,window_left_padding=10, window_bottom_padding=10, color="#808080", what_color="#808080" )

image chair normal = "chair.png"

#Image of Carlos the Guard
image Carlos neutral= "carlos/carlos neutral.png"
image Carlos angry= "carlos/carlos angry.png"
image Carlos poker_face= "carlos/carlos porker_face.png"
image Carlos happy="carlos/carlos happy.png"
image Carlos concern= "carlos/carlos concerned.png"
image Carlos ice angry = "carlos/icecream carlos angry.png"
image Carlos ice concerne = "carlos/icecream carlos concerned.png"
image Carlos ice happy = "carlos/icecream carlos happy.png"
image Carlos ice neutral = "carlos/icecream carlos neutral.png"
image Carlos ice poker = "carlos/icecream carlos pokerface.png"
image Carlos spin = "carlos/so_long_gei_carlos.png"

#Image of Juan the main character
image Juan neutral= "juan/juan neutral.png"
image Juan surprise= "juan/juan surprised.png"
image Juan suspicious= "juan/juan suspicious.png"
image Juan concerned= "juan/juan concerned.png"
image Juan normal = "juan/juan pre neutral.png"


#Image of Rosa the milf
image Rosa angry= "rosa/rosa furiosa.png"
image Rosa serious= "rosa/rosa seria.png"
image Rosa sorprise= "rosa/rosa sorprendida.png"
image Rosa angry real = "rosa/rosa angry.png"
image Rosa elevator = "rosa/rosa elevator.png"
image Rosa lance = "rosa/rosa_lanzamiento_perfecto.png"
image Rosa smash = "rosa/Rosa_smash.png"
image Rosa beat Daniela = "rosa/kathwack_color.png"
image Rosa climb = "rosa/rosadio.jpg"
image Rosa climb land ="rosa/rosadiobl.png"

#Image of Maria the daughter
image Maria neutral= "maria/maria neutral.png"
image Maria happy= "maria/maria feliz.png"
image Maria sorprise= "maria/maria impactada.png"
image Maria angry= "maria/maria enojada.png"
image Maria sad = "maria/maria sad.png"
image Maria shame = "maria/Maria_shamed.png"

#Image of Luis the Velociraptor
image Luis neutral= "luis/luis neutro.png"
image Luis happy= "luis/luis felih.png"
image Luis angry= "luis/luis nojao.png"
image Luis sad= "luis/luis trite.png"
image Luis fear= "luis/luis cagao.png"
image Luis raqueta = "luis/raqueta_raptor_color_blur.png"
image Luis raqueta space = "luis/raqueta_raptor_color_blur.webp"

#Image of Daniela
image Daniela = "daniela/daniela neutral.png"
image Daniela surprise= "daniela/daniela surprised.png"
image Daniela happy= "daniela/daniela happy.png"
image Daniela hopeless= "daniela/daniela hopeless.png"
image Daniela angry= "daniela/daniela angry.png"


#Image of the grommer 
image Groomer angry= "don/groomer angry.png" 
image Groomer happy= "don/groomer happy.png"
image Groomer neutral= "don/groomer neutral.png"
image Groomer sad= "don/groomer sad.png"


image guardia = "extras/guardia generico/guardia apuntando.png"
image guardia fail ="extras/guardia generico/guardia lanzado.png"

image ballo = "bdf.png"


# style narrator:
#     italic True
    
#load music assets
image bg_stairs:
    "bg/stairs.jpg"

image bg_elevator :
    zoom 0.5
    "bg/elevator.png"
image bg_mall:
    zoom 0.5
    "bg/mall.jpg"

image bg_bar:
    zoom 0.8 
    "bg/restaurant.jpg"

image  bg_office:
    zoom 0.38
    "bg/office.jpg"

image bg_office_rom:
    zoom 2.0
    "bg/officeroom.jpg"

image bg_rosa:
    zoom 2.0
    "rosa/rosa elevator.png"


transform half_size:
    zoom 0.39
    xalign 0.0

transform half_size_right:
    zoom 0.39
    xalign 1.0
    
transform right_position:
    xalign 1.0

transform left_position:
    xalign 1.1

transform half_size_right_luis:
    zoom 0.39
    xalign 1.1
    yalign 2.0


transform left_to_rigth:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

transform left_to_right_min_animation:
    xalign 0.0
    linear 4.0 xalign 1.1


transform double_size:
    zoom 3.0
    xalign 0.0
        
transform half_size_right_less:
    zoom 0.39
    xalign 1.1

transform mini_animation:
    yalign 2.0
    linear 0.2 yalign 1.9
    linear 0.2 yalign 2.0
    linear 0.2 yalign 1.9
    linear 0.2 yalign 2.0

transform mini_talk_animation:
    yalign 0.0
    linear 0.2 yalign 0.7
    linear 0.5 yalign 0.0
    linear 0.2 yalign 0.7
    linear 0.5 yalign 0.0

transform left_minus:
    xalign 0.5

transform left_minus_minus_one:
    xalign -0.5



transform flip_image:
    xzoom -1.0

transform anti_flip:
    xzoom 1.0

# image credits_text:
#     "bg/continuara.png"
#     pause 5.0
#     "bg/credit1.png"
#     pause 5.0
#     "bg/credit2.png"
#     pause 5.0
#     "bg/credit3.png"

image credits_continuara:
    "bg/continuara.png"
image credit:
    "bg/credit1.png"
image creedit_2:
    "bg/credit2.png"
image credit_3:
    "bg/credit3.png"



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Volcaldera Bluffs, 28 de mayo, año 201M2042"

    Juan "Siendo sincero mi padre tenía razón sobre lo de estudiar otra carrera en mi país natal, no pude encontrar trabajo de lo que estudié."
    Juan "La parte más estresante fue ver que la gran mayoría de las ofertas laborales requerían una experiencia mayor a 5 años "    

    Juan "¿COMO CHINGADOS UN UNIVERSITARIO QUE RECIEN SE GRADUA PUEDE CONSEGUIR TAL COSA? "
    Juan "Ya ni hablemos que los sueldos que daban esas empresas eran muy inferiores al que deberían dar en realidad."

    Juan "Es por eso que un mi tío me convenció de tratar de ir al otro lado a experimentar el sueño americano."
    Juan "Actualmente vivo en Volcadera Bluffs, Dinofornia, haciendo cualquier tipo de trabajo como vigilante, barrendero, lavaplatos entre otras cosas."

    Juan "Caminando por un Wallmart cercano a mi departamento me encontré al primo de un viejo amigo de la universidad al parecer mi amigo Daniel también vive aquí y anda buscando un vigilante para un bar donde el es el dueño."

    Juan "No me gusta para nada trabajar de eso me frustra demasiado, pero esa suscripción ala cuenta de onlydinos de ese parasaurio azul femboy no se va a pagar solo."


    scene bg_mall
    with fade

    play music "Nintendo Wii - Mii Channel Theme.ogg"
    show Juan normal at half_size

    show Juan normal at flip_image
    Juan "Y eme aquí, entrando directamente hacia una plaza de Volcaldera Bluffs un bastante movido y lleno de vida."
    Juan "donde prosperan varios negocios, diría que podría competir con aquel barrio ubicado en Skin Row, ¿cómo se llamaba? ¿pequeño… troodon? ah, como sea."
  
    Juan "Creo que estoy divagando mucho, vine específicamente por este empleo. Admito que el lugar esta bonito, esos 4 pisos lleno de decoraciones góticas y el jardín de en medio le dan buena vibra. "
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show Juan normal at left_to_right_min_animation

    Juan "Voy directo a un elevador cuadrado que está ubicado junto a las salidas en el 2do piso"

    scene bg_elevator

    show Juan normal at half_size
    show Juan normal at center

    "Lo malo es que como es pequeño y bastante usado (a pesar de que haya escaleras…)  lo que hace que inevitablemente huela mucho a obo. "
    
    Juan " Tio agradezco desde el fondo de mi alma que me hayas invitado a tus partidas de yu-di-no en la frikiplaza de nuestra ciudad para poder desarrollar inmunidad a este hedor"

    Juan " Lo bueno es que el elevador tiene clima y reproduce música de Nintendo. Conociendo como es la empresa no me sorprendaria que la compañía los demande por"

    unkown "Tu si que eres muy grosero"

    show Juan normal  at flip_image
    Juan "¿Quién dijo eso? "

    "Giro mi cabeza hacia la derecha e izquierda y no veo absolutamente  nada"
    
    Juan "Deben ser los nervios o estoy desarrollando ezquisofrenia, por si las dudas voy a descansar mas y dejar de pasármela todo el dia viendo las funas que hay en X."

    Juan "Bueno parece que el elevador bajo, es hora de salir"

    Juan "Estoy en la planta baja a mi alrededor hay puestos de comidas como un snootbucks, taco shell, un  tomboyters entre otros puestos de comida y justamente en medio esta mi destino"
    # These display lines of dialogue.

    jump conociendo_a_daniela
  
    return

label conociendo_a_daniela:
    play  music "Soft Jazz Relaxing Music.ogg"
    
    scene bg_bar
    with fade

    show Juan normal at half_size
    show Carlos neutral at half_size_right_less  
    show Luis neutral  at  half_size_right_luis 


    Juan "Ya estoy dentro y pues el bar se ve muy lindo con esa decoración que tiene."
    Juan " Me percato que al lado derecho está sentado un guardia Anquilosaurio color café con cara de pocos amigos que se me queda viendo raro."
    Juan " Al lado suyo esta un velociraptor color naranja más amigable le preguntare sobre donde esta Daniel"

    show Juan normal at flip_image
    Juan "Buenas sabes de casualidad ¿Dónde puedo encontrar Daniel? Es un tiburón color azul con manchas blancas en la frente que me cito para el puesto de"
    # This ends the game.

    show Luis neutral at mini_animation

    Luis "Hmmm.. ¿Daniel? Daniel no me suena ¿No te referias a Daniela? Puedes preguntarle a la Jefa. Su oficina se encuentra ala derecha subiendo esas escaleras."

    Juan "Muchas gracias. "

    "Curioso siempre pensé que Daniel era hijo único y no me sorprende el hecho de que no sea el verdadero jefe del local. A Daniel siempre le gustaba presumir cosas que no tenia"

    
    window auto hide
    camera:
        subpixel True xpos 0 
    show Juan normal:
        subpixel True 
        xpos 0.0 
        linear 0.38 xpos 1.14 
    with Pause(0.48)
    show Juan normal:
        xpos 1.14 
    window auto show


    # show Juan normal  at reset 

    
    # show Juan normal at left

    Juan "Subo las escaleras y llego a la oficina. Toco la puerta y"

    
    unkown "Carlos ya te dije que no planeare en renovar tu contrato si sigues con esa actitud"

    Juan "Disculpe mi nombre es Juan vino a buscar a Daniel sobre la solicitud de Vigilante debido a que"

    unkown " Esa voz… Adelante pasa"

    scene  bg_office_rom

    

    show Daniela at half_size

    show Juan normal at half_size
    show Juan normal at left_position
    "Abro la puerta y me encuentro a una chica tiburón de color gris con una camisa verde agua y una falda apretada sentada escribiendo en una laptop"
    
    Juan "Disculpe la molestia nuevamente pero asumo que eres la hermana de Daniel me preguntaba si todavía siguen buscando un vigilante."
    
    Daniela "En realidad, yo soy Daniel"

    Juan "¿Por qué no me sorprende?."

    show Daniela surprise
    Daniela "Muchas cosas han cambia.. Espera ¿Cómo que no te sorprende?"


    Juan "Con todo respeto herman- na, pero se veía desde el espacio. cuando hacíamos equipos de trabajo en la universidad siempre pasabas imágenes del meme de BoyKisser "

    Juan "Asi como también en Halloween hacias cosplay de algún femboy de temporada como Astolfo ya ni hablemos que en tu cuenta de Jurasicbook compartias imágenes de ese tal Darkwaifu."

    show Daniela happy
    Daniela "Puedo ser algo obvia jaja. Pero bueno retomando a lo otro sip sigo buscando un vigilante ¿te interesa el puesto?"

    Juan "Realmente no, pero necesito el dinero"

    show Daniela
    Daniela "Entonces es un si. Mira se por mi primo que no te gusta trabajar de esto pero necesito por esta semana la mayor cantidad de vigilantes en este bar para la noche"

    Daniela "Tendre una reunión con el alcalde para la posible venta de un software y si todo va bien necesitare gente que se encargue de instalar el software en la alcaldía y darle mantenimiento sobre todo a los servidores. Es ahí donde yo te puedo meter"

    Daniela "darte esa oportunidad ¿Qué me dices?"

    Juan "Wow…. quiero decir, ¿Hablas en serio?"

    show Daniela happy

    
    Daniela "¡Por supuesto!, sé exactamente cómo se siente esa frustración de estudiar por varios años y no encontrar empleo de eso."
    
    show Daniela 
    Daniela "De hecho, mi difunto padre me hizo trabajar en este bar como secretaria donde aprendí a cómo manejar todos los gajes de este oficio, así como también le hice algunas mejoras"
    Daniela "como la de implementar una aplicación de escritorio en vez de tener que usar tablas de RhinoreXel para el conteo del inventario. "

    Daniela "Así que, te lo vuelvo a preguntar pequeñín ¿Te interesa el trabajo?"

    Juan "Simón, ¿qué es lo peor que podría pasar? "

    #"bam" with vpunch

    show Daniela happy
    Daniela "¡Bienvenido a bordo Juan!  "
    "Daniela se levanta de su silla y sujeta mi mano"


    Daniela "Ven te presentare con los demás  y de paso ¿por casualidad cual es tu altura y talla? Lo necesito para ver si tengo un uniforme a tu medida"

    Juan "Mido 1.98m  y  peso 77kg "

    show Daniela hopeless
    Daniela "Uy no creo tener uno a esa medida."

    show Daniela happy 
    "Pero primero necesito presentarte con los demás"
    
    jump presentacion
    
    return

label presentacion:
    scene bg_bar 
    with fade

    show Daniela at half_size

    show Juan normal at half_size
    show Juan normal at flip_image

    Juan "Salgo con Daniela de su oficina hacia la sala del bar. Agarro una silla pegado al comedor y me siento. Daniela agarra un vaso y una cuchara del comedor y empieza a dar un aviso"

    
    show Daniela at mini_talk_animation
    show Daniela happy
    Daniela "Escuchen todos. Tenemos un nuevo integrante en nuestro negocio, les presento a Juan un amigo de mi universidad denle todos una calida bienvenida"

    #Remplazar por la etiqueta de todos
    unkown "Bienvenido compañero"


    show Carlos neutral at half_size_right
    
    show Luis neutral at half_size_right_luis


    show Carlos angry 
    Carlos "Bienvenido CoMpAñero. Pinche escuincle"

    " Carlos hace una mueca al decir eso y Daniela observa eso "

    show Daniela angry
    Daniela "Carlos ya te dije que si seguias con esa actitud te meterias en mas problemas"

    show Carlos concern 
    Carlos "¿Cómo cuales señorita?"

    show Daniela at mini_talk_animation
    show Daniela angry
    Daniela "Como conmigo. Te recuerdo  que a cada rato pienso sobre si despedirte ahorita mismo o cumplir con mi palabra de que puedas seguir trabajado aquí hasta que encuentres trabajo en otro lugar"

    show Carlos  neutral
    Carlos "Pero tu padre jamás haría eso, yo estoy aquí desde que el señor Carmillo comenzó este negocio"


    show Daniela angry
    Daniela "Y por eso me he aguantado demasiado tu actitud. Asi que te lo vuelvo a repetir, moderate o sufre las consecuencias"

    show Carlos neutral
    Carlos "Si señorita "

    "Daniela se acerca lentamente hacia mi"

    show Daniela at flip_image
    show Daniela at left_minus
    show Daniela at mini_talk_animation
    show Daniela hopeless

    Daniela "Perdona por eso la gente de aquí suele ser muy amable no dejemos que una manza podrida nos arruine el dia. Pero bueno, ve al piso de arriba en el departamento de Ropa. Diles que necesitas ropa de guardia a esta medida y que Daniela te mando. "

    Juan "Espera pero no traje mucho efectivo para comprar el uni…"

    show Daniela happy
    Daniela "Ntp por eso  yo lo pagare. Varios comerciantes de la zona ya me conocen y tengo varios trueques con ellos. Ten"
     
    " saca un monedero rojo y me entraga un fajo de billetes " 
    Daniela " Se que en teoria trabajas hasta por dentro de 2 horas pero necesito que te quedes aquí para te puedas familiarizar con el entorno del centro comercial y del bar"
    Daniela" Sobre todo de las rutas de escape y del personal. Asi que ten este dinero para que puedas comprarte algo de comida"

    show Juan normal at mini_talk_animation
    Juan "No seria mejor que me dieras algo de lo que sirven del bar y nos ahorramos eso."

    " Daniela hace un gesto con su ojo derecho  "

    show Daniela
    Daniela "Sera mejor que no, nuestro chef no llega hasta dentro de media hora, además de que solo tengo papitas por el momento."
    Daniela "Pero no pasa nada, si no te sientes cómodo puedes traer tu comida al bar y comer en paz ahí."
    Daniela "pero bueno te dejo para que no se te haga tarde, cualquier cosa sabes donde buscarme."

    show Daniela at flip_image
    #show Daniela at left_to_right_min_animation
    " Miro como Daniela se aleja lentamente hacia el horizonte  "

    Juan "Realmente no se me hace del todo raro que Daniel se haya hecho trans. Siempre bromeaba con nuestros amigos de que Daniel siempre tuvo el potencial para ser femboy"

    " Rugido de tripas  "

    Juan "bueno debo apurarme si quiero comer."

    unkown "Los mortales de aquí suelen ser muy raros"

    play  music "Dragon Ball Z prologue music 2 (Buu Saga).ogg" 

    scene  bg_office_rom
    with fade

    show Juan neutral at half_size_right
    show Carlos neutral at half_size_right
    show Luis neutral at half_size_right_luis
    show Daniela at half_size
    # show Daniela at left

    Juan "llega a la oficina, ya con mi uniforme puesto. "

    show Daniela at mini_talk_animation
    Daniela "Bueno caballeros como varios sabran el Alcalde Stoolas vendrá en cualquier dia de la siguiente semana necesito que cada uno de ustedes den su máximo esfuerzo para que este bar  se vea respetable"

    show Daniela hopeless  
    Daniela "Recuerden que algunos lugares del centro comercial tienen rutas de escape por si las cosas se ponen feas asi como de sistemas anti disturbios por si aparece otro borracho a causar disturbios"

    show Daniela
    Daniela "¿Alguna otra pregunta?"

    show Carlos at mini_talk_animation
    Carlos "¿Cuál era el código para cuando surgiera una problema con alguna mujer?"

    show Daniela 
    Daniela "3312. Bueno equipo a trabajar"
    show Daniela at flip_image


    scene bg_mall
    with fade
    jump Conociendo_a_rosa

label Conociendo_a_rosa:
    play music "Nintendo Wii - Mii Channel Theme.ogg"

    show Juan neutral at half_size_right
    with dissolve

    Juan "Me encuentro afuera y sentado en unas sillas cercanas al bar. Miro fijamente hacia el jardín de en medio, Si que el centro comercial se ve lindo de noche con esas luces neon."
    Juan "Noto también que hay un chico anquilosaurio parado al otro lado del jardin mirando fijamente su celular y volteando para todos los lados, alo mejor cito a una chica y esta lo dejo plantado."
    Juan "Pobre tipo."

    show Luis angry at half_size
    show Luis angry at left_minus
    show Carlos angry at half_size
    show Carlos angry at flip_image
    show Carlos angry at left_minus_minus_one
    

    show Luis angry at mini_animation
    Luis "Chingadamadre Carlos ya te dije que no hagas eso"

    Juan "Inclino mi cabeza en dirección al bar y noto que mis 2 compañeros andan discutiendo"

    show Carlos happy 
    Carlos "Tengo hambre, me ire a la heladeria que esta cerca de aquí. Solo cubreme"

    show Luis sad 
    Luis "Por un demonio "

    " Luis hace un gesto de agotamiento "

    
    show Luis at mini_animation
    show Luis neutral 
    Luis "Para eso la jefa nos dio una hora libre para comer. Además acabas de tragarte como 40 tacos de pastor ¿Cómo carajos te puede caber algo mas en el estomago?"

    show Carlos neutral 
    Carlos "Estas en lo correcto plumero, acabo de comer."
    
    show Carlos happy 
    Carlos "pero olvide lo más importante.... el postre, así que si me disculpas iré a comprarme un heladito."

    show Carlos happy at flip_image

    
    " Carlos se mueve rumbo a la salida de enfrente del bar y aparece un humano viejo con bigote y un look similar a waluigi "
    hide Carlos happy 
    with dissolve
    hide Luis neutral
    with dissolve

    show Groomer happy at half_size
    show Groomer happy at flip_image
    show Groomer at mini_talk_animation
    Don "Buenos días jóvenes, de casualidad este es el bar llamado como {i} {b}The blue shift {/b} {/i}? "


    Juan "Emm de hecho si ¿Qué se le ofrece?"

    Don "No nada, esta perfecto, tendre una cita hoy y estoy algo nervioso. Por casualidad me preguntaba ¿sabes cuánto cuesta un Martini aquí?"

    Juan "Uy… Disculpe eso si no se tendría que preguntarle a la jef.. "

    show Daniela at half_size_right
    # show Daniela at right
    show Daniela at flip_image
    with dissolve
    " Daniela aparece delante de mi "


    Daniela "Cuesta aproximadamente como  5 dólares señor"

    show Groomer sad
    " El señor muestra una cara de sorprendido  "

    Don "Esa voz….. "

    show Groomer angry
    
    " cambia la cara a uno de disgusto a uno de nervioso "

    Daniela "¿le pasa algo?"

    show Groomer angry
    Don " No solo que "

    " se empieza a sujetar con el dedo un botón de su camisa  "

    show Groomer neutral at anti_flip
    Don "deje a algo en el carro y no quiero que me lo robe ahorita vengo "
    " El sujeto se mueve lentamente para luego acelerar y susurrar "
    

    Don "Por Jesus Raptor ¿Cómo es posible que haya ese tipo de raritos en este lugar?"
    
    hide Groomer neutral
    with dissolve

    show Daniela at center
    show Daniela at anti_flip 
    show Daniela:
                pos (0.5, 1.05) 


    Juan "¿Y ese milagro que estas tu fuera?"

    show Daniela happy  
    Daniela "Una amiga me hablo para citarme en un local que está en el pasillo de arriba."
    Daniela "Me comento que los miembros de su congregación religiosa les interesa bastante mi aplicación sobre el control de un inventario"

    Juan "¿No seria mejor que ellos fueran directamente a tu local?"

    show Daniela hopeless
    
    show Daniela hopeless:
        subpixel True 
        parallel:
            xpos 0.5 
            linear 0.04 xpos 0.5 
            linear 0.02 xpos 0.5 
        parallel:
            ypos 1.05 
            linear 0.05 ypos 0.94 
            linear 0.05 ypos 1.05 


    Daniela "Seria lo idóneo, pero la mayoría de las iglesias de la ciudad son algo especiales sobre el asunto de la venta de alcohol y desconozco si los mormones entren en esa categoría. Así que más vale prevenir"

    Juan "¿Pero y lo del alcalde?"

    show Daniela
    Daniela "No creo que venga por esta hora, además andaré cerca. Luis tiene mi número por si las dudas. Así que Luis y tu están a cargo del changarro"

    Juan "¿Yo pero es mi primer día  aquí? No sería mejor alguien como Carlos que lleva años trabajando aquí"

    show Daniela angry:
        subpixel True 
        parallel:
            xpos 0.5 
            linear 0.04 xpos 0.5 
            linear 0.02 xpos 0.5 
        parallel:
            ypos 1.05 
            linear 0.05 ypos 0.94 
            linear 0.05 ypos 1.05
    Daniela "¿Y el esta aquí?"
    Juan "Nop"

    show Daniela 
    Daniela "Ahí tienes tu respuesta. Bueno,  me tengo que ir."    

    # hide Daniela with dissolve
    show Daniela at flip_image
    
    window auto hide
    show Daniela:
        subpixel True 
        xpos 0.5 
        linear 1.13 xpos -0.21 
    with Pause(1.50)
    show Daniela:
        xpos -0.21 
    window auto show


    " Veo que Daniela se va y me doy cuenta de una mancha que tiene en la parte trasera de su falda justo en la nalga izq… "

    unkown "Por Afrodita , ¿no se supone que tu deber es vigilar en vez de  andar viendo traseros?"

    show Juan surprise
    Juan "¿Quién dijo eso?"

    unkown "Espera. ¿Puedes escucharme?"

    show Luis neutral at half_size
    show Luis neutral at center
    show Luis neutral at flip_image
    with dissolve

    Luis "¿Decir que amigo?"

    show Juan neutral 
    Juan "No, nada. Debo descansar;  ya estoy escuchando voces otra vez "

    show Juan suspicious
    with Pause(1.5)
    show Juan concerned
    
    # " Juan pone cara de susto "

    show  Luis happy
    Luis "Bueno ire al baño por 5 minutos cualquier cosa me echas un grito"

    
    Juan "Está bien, yo hare guardia"
    hide Luis with dissolve


    window auto hide
    show Juan concerned:
        subpixel True 
        xpos 1.0 
        linear 0.22 xpos 0.74 
    with Pause(0.32)
    show Juan concerned:
        xpos 0.74 
    window auto show


    "Me siento y miro hacia afuera, miro que el chico aquilops se alegra y viene directo al bar. Que bueno!."
    "tal vez su cita está aquí dentro; me alegro por él. Agarró una de las sillas y me pongo enfrente de donde están las cervezas cuando de repente siento un abrazo por mi espalda"

    with vpunch

    show Maria happy at half_size_right
    show Maria happy at flip_image
    Maria "BUENAS"

    show Juan neutral at flip_image
    Juan "¿Hola se te ofrece algo?"

    Maria"No lo se, tu dime"
    " el chico aquilops se ruboriza mientras me lanza una mirada picarona " 
    Maria "después de todo,  tú me citaste aquí chico con melena. "

    Juan "¿citarte?, ¿ de qué hablas?"

    Maria "No te hagas amor"
    "   el me da un beso y empieza a tocar mi mano derecha  " 
    Maria "¡Tú me citaste aquí para finalmente conocernos en persona!."

    Juan "¿de qué hablas?  ni te conozco y yo no bateo de ese lado."

    show Maria angry
    Maria "Soy mujer imbécil, además tu me dijiste por X que te gustaba demasiado que me vistiera así."
    

    show Maria happy
    Maria " Deja de fingir y abrázame."
    "(La chica aquilops trata de darme un fuerte abrazo, pero no lo logra ya que me paro ante la presencia de Carlos)"

    show Carlos ice happy at half_size
    show Carlos ice happy at flip_image
    with dissolve
    Carlos "¿Quién es tu novia novato?"
    " muestra un helado en su mano izquierdo con su cara inexpresiva "


    show Juan neutral at anti_flip
    Juan "NO es mi novia." 
    "(siento como la chica intenta tomarme de las manos)"



    Maria "Me llamo Maria y sip soy su novia."

    show Carlos ice neutral  
    "Carlos pone una expresión seria"


    Carlos "Mira, me da igual lo que hagas escuincle, pero te recomiendo que no andes con menores de edad. Te meterás en muchos problemas"

    show Juan surprise
    Juan "¿ES UNA MENOR?"

    
    show Rosa angry real at center
    with vpunch
    Rosa "¡ALEJATE DE ELLA DEGENERADO!"

    hide Rosa angry real
    
    window auto hide
    camera:
        subpixel True 
        xpos 0 
        linear 0.33 xpos -279 
    show bg_mall:
        subpixel True xpos 0.5 
    with Pause(0.43)
    camera:
        xpos -279 
    window auto show

    #
    show Juan neutral at flip_image
    show Rosa angry at half_size_right_less
    show Rosa angry at flip_image    
    show Rosa angry:
        subpixel True xpos 1.29 


    
    "Entra una aquilops mayor  similar a la tipa que dice ser mi novia  pero más voluptuosa y atractiva"

    show Carlos ice happy 
    Carlos "Buenas señora ¿se le ofrece algo?"

    show Rosa angry at mini_talk_animation
    Rosa "SI!, VINE POR EL DESGRACIADO QUE TRATA DE SEDUCIR A MI HIJA!"

    show Carlos ice poker 
    show Maria sorprise at anti_flip    
    show Maria sorprise:
        subpixel True xpos 0.94 


    Maria " ¿mamá?, ¿cómo supiste que estaría aquí?"

    Rosa "Tu amiga Cynthia me avisó de que no fuiste a su casa a estudiar. Estoy muy decepcionada de ti señorita; no puedo creer que le hicieras eso a Reed en su cumpleaños." 

    show Maria angry
    Maria "¿¡Por qué debería estar SU cumpleaños eh!? ¡Él no es mi padre y nunca lo será!. ¡Estoy feliz estando con alguien que me aprecia de verdad!" 

    
    window auto hide
    show Maria angry:
        subpixel True ypos 0 
        xpos 0.94 
        linear 0.39 xpos 0.91 
    with Pause(0.49)
    show Maria angry:
        pos (0.91, 0) 
    window auto show
    "la chica intentó acercar su mano derecha a la mía pero logré quitarla con éxito"
    
    Juan "Señora escuche yo no soy su novio ni la conozco para empezar."

    show Rosa angry at mini_talk_animation
    Rosa "¿Me ves cara de pendeja? Los vi besarse. Además, en los chats que me pasaron describen EXACTAMENTE a un humano con cabello largo como tú."

    Juan  "¿Cabello Largo? e-espere un momento, ¡creo que me confunde con alguien más!. justo acaba de pasar un sujeto parecido a mi, ¡se lo puedo mostrar con las grabaciones!"

    show Carlos ice angry 
    Carlos "Doña deje al nuevo en paz y deje que se diviertan un rato. No actue como una vieja amargada"

    #DBZ music PLaylis

    play music "DBZ- Battle Music 1.ogg"
    Rosa "¿Cómo me dijiste?"

    Carlos "Que se relaje y no actúe como una vieja amargada "

    hide Juan normal with dissolve
    hide Maria with dissolve

    
    window auto hide
    show Rosa angry:
        subpixel True 
        xpos 1.29 
        linear 0.43 xpos 0.79 
    with Pause(0.53)
    show Rosa angry:
        xpos 0.79 
    window auto show
    hide Carlos ice angry with dissolve

    hide Rosa angry with dissolve

    show Carlos spin at half_size
    show Carlos spin at center    
    show Carlos spin with dissolve:
        subpixel True xpos 0.77 zoom 0.28 
    

    " En ese instante, la madre de la chica aquilops tomó a Carlos por la cola y comenzó a girar con él varias veces hasta finalmente dejarlo ir, arrojándolo a través de una ventana del centro comercial. "
    
    
    show Carlos spin:
        subpixel True crop_relative True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        crop (-0.19, 0.0, 1.0, 1.0) 
        linear 0.34 crop (-0.01, 0.0, 1.0, 1.0) 
    with Pause(0.2)
    show Carlos spin at flip_image 
    show Carlos spin at anti_flip:
        subpixel True crop_relative True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        crop (-0.19, 0.0, 1.0, 1.0) 
        linear 0.34 crop (-0.01, 0.0, 1.0, 1.0) 
    with Pause(0.2)
    show Carlos spin at anti_flip
    show Carlos spin:
        subpixel True crop_relative True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        crop (-0.19, 0.0, 1.0, 1.0) 
        linear 0.34 crop (-0.01, 0.0, 1.0, 1.0) 
    with Pause(0.2)
    show Carlos spin at anti_flip

    
    hide Carlos spin with dissolve 
    
    show Luis neutral at half_size_right_luis 
    show Luis fear 
    Luis "¿Qué es ese ruido?  OH DIOS QUE PASO CON LA VENTANA"


    show Rosa angry at half_size
    show Rosa angry at left 
    show chair normal at double_size
    show chair normal at right    
    show chair normal:
        subpixel True xzoom 0.84 yzoom 0.83 


    Rosa "¡voy a darte el suplex de tu vida SKINNIE!"

    Juan " La mujer anquilosáurido empieza a flexionar sus piernas y.. OH DIOS VIENE DIRECTAMENTE HACIA MI "

    
    window auto hide
    show chair normal:
        subpixel True 
        pos (1.0, 1.0) 
        linear 0.30 pos (0.24, 0.87) 
    with Pause(0.78)
    show chair normal:
        pos (0.24, 0.87) 
    window auto show


    "Luis Trata de lanzarle una silla para bloquear su camino pero falla en el intento. Espera ella se detuvo. "

    
    window auto hide
    show Rosa angry:
        subpixel True 
        parallel:
            xpos 0.0 
            linear 0.36 xpos 0.44 
        parallel:
            ypos 1.0 
            linear 0.11 ypos 0.79 
            linear 0.14 ypos 1.04 
    with Pause(0.46)
    show Rosa angry:
        pos (0.44, 1.04) 
    window auto show


    "OH MIERDA DIO UN FUERTE SALTO Y AGARRO A LUIS DE SU COLA."

    hide Rosa angry
    show Luis raqueta at half_size
    show Luis raqueta at center
    "CARAJO ESTA USANDO A LUIS COMO RAQUETA Y VIENE HACIA MI-."
    
    window auto hide
    show Luis raqueta:
        subpixel True 
        xpos 0.5 
        linear 2.15 xpos 0.69 
    with Pause(2.25)
    show Luis raqueta:
        xpos 0.69 
    window auto show


    "de repente siento como jalan mi mano."

    hide Luis raqueta with dissolve

    show Juan neutral at half_size_right_less    
    show Juan neutral:
        subpixel True xpos 0.96 
    show Maria sad at half_size_right_less
    show Maria sad at flip_image    
    show Maria sad:
        subpixel True xpos 1.22 


    Maria "AMOR VAMONOS DE AQUÍ"

    show Juan surprise at flip_image
    Juan "YO NO SOY TU NOVIO Y NO QUIERO ESTAR CERCA DE TI O DE TU LOCA MADRE….Tal vez si le muestro el video resuelva ese malentendido"

    Maria "Cuando mama se pone así no escucha razones. Tu mejor opción es huir"

    hide Maria with dissolve
    hide Juan neutral with dissolve
    show Luis raqueta space at double_size

    "Empiezo a correr hacia los pasillos del centro comercial cuando de repente veo a esa señora aventar a Luis hacia mi."


    window auto hide
    show Luis raqueta space:
        subpixel True 
        xpos 0.0 
        linear 0.40 xpos 1.15 
    with Pause(1.19)
    show Luis raqueta space:
        xpos 1.15 
    window auto show
    with vpunch


    "tuve que Saltar hacia la pared para evadir el proyectil"

    

    # show Luis raqueta space at center
    Luis  "Arghhh….."
    "Saca un walkie talkie"
    Luis " a-aqui los guardias del bar tenemos un 3312, ¡tenemos un 3312!"
    "se desmaya"

    play music "Shi Wo Yobu Cell Game (Extended).ogg"
    "Sigo corriendo por mi vida seguido del behemoth y su engendro."
    " Trato de arrojarle a mamázilla todos los anuncios y botes de basura que encuentro pero es inútil"
    " Solo la hago enojar mas. Jesús raptor en tu cruz de piedra  si existes te imploro que me ayudes."


    show guardia at half_size
    show guardia at center 
    "logro ver como aparece un guardia del centro comercial, quien trata de darle a la mujer con un taser pero no parece afectarla en lo más mínimo."  
    show Rosa angry at half_size

    
    window auto hide
    show Rosa angry:
        subpixel True 
        xpos 0.0 
        linear 0.4 xpos 1.32 
    with Pause(0.85)
    show Rosa angry:
        xpos 1.32 
    with vpunch
    window auto show
     
    window auto hide
    show guardia fail:
        subpixel True 
        parallel:
            ypos 1.0 
            linear 0.4 ypos 1.75 
        parallel:
            rotate 0.0 
            linear 0.22 rotate 14.0 
            linear 0.35 rotate 67.0 
    with Pause(0.5)
    show guardia fail:
        ypos 1.75 rotate 67.0 
    window auto show
    " aparece Rosa al lado de el y el guardia es aventado como si fuera un pino de boliche "
  



    "MIERDA MIERDA. Trato de correr hacia las escaleras electricas y para mi horror comienzan a fallar soltando chispas por doquier. AHORA NO, AHORA NO"

    jump run_juan
    return

label run_juan:
    unkown "Yo que tu iría por el elevador"

    "Cierto el elevador. Corro hacia el elevador cuando soy interceptado por Maria"
    Juan"¡Alejate de mi!"

    Maria "Relájate hombre, por lo que veo el elevador es la única salida que hay así que aguántate y subamos juntos."

    scene bg_elevator with dissolve 
    camera:
        subpixel True xpos -9 

    show Juan neutral at half_size
    show Juan concerned at center

    show Maria shame  at half_size
    show Maria shame at left
    
    "Me resigno y entramos los dos al elevador. Lo único bueno es que el elevador ya no huele feo.)"

    show Maria sorprise 
    Maria "uh…. Ahora que lo pienso tu voz es algo diferente, y no llevas la playera que me dijiste que traerías."

    show Juan neutral
    Juan "¡Es lo que he tratado de decirte!, me confundiste con alguien más, ¡y ahora tu loca madre quiere matarme!"

    show Maria shame
    Maria "Perdona, de verdad pensé que eras mi novio y no quería pensar sobre la posibilidad de que alguien me mintiera…. otra vez."

    show Juan concerned
    Juan "¿otra vez? "


    " el vidrio del elevador es atravesado por un cinturón "
    with vpunch

    show Juan surprise 
    show Maria sorprise
    Juan "¡¡¡¿ESO ES UN CINTURON?!!!"

    scene bg_rosa    
    camera:
        subpixel True xpos -158 xzoom 1.15 yzoom 1.07 zoom 1.04 
    with vpunch
    " Rosa empieza a jalar el elevador usando un cinturón y una cuerda"


    Rosa "¿A DONDE CREEN QUE VAN ?" 

    scene bg_elevator
    show Juan surprise at half_size
    show Juan surprise at center

    show Maria sprprise  at half_size
    show Maria sorprise at left
    
    "El elevador llega a su destino y se abren las puertas."
    "Salto con maría del elevador justo cuando este es derribado al no soportar la fuerza del dinosaurio"
    with vpunch
    hide Maria sorprise with dissolve
    hide Juan surprise with dissolve

    scene bg_mall       
    show bg_mall:
        subpixel True ypos 2.45 zoom 1.82 


    show Daniela at half_size
    show Daniela at right
    show Daniela at flip_image
    show Juan neutral at half_size
    show Juan neutral at left
    show Juan neutral at flip_image
    show Juan neutral:
        subpixel True xpos 0.21 


    show Maria neutral at half_size
    show Maria neutral at left
    # show Maria neutral at flip_image
    Daniela " ¿Juan? ¿Qué esta pasando?"

    
    Juan "Larga historia, te la cuento luego, pero necesitamos ir hacia la salida antes de que esa loca me mate "

    show ballo at double_size    
    show ballo:
        subpixel True ypos 1.05 


    " corremos con toda nuestra fuerza hacia las salidas cuando de repente,"
    
    window auto hide
    show ballo:
        subpixel True 
        ypos 1.05 
        linear 0.18 ypos -2.65 
    with Pause(0.28)
    show ballo:
        ypos -2.65 
    window auto show


    "vemos que un dinosaurio sale aventado hacia arriba"
     
    "provocando que caiga escombros y parte de la salida sea bloqueada "

    # "Daniela Voltea hacia donde estaba el elevador"

    show Juan surprise
    show Maria sorprise 

    show Daniela surprise
    Daniela "Jesus Raptor. Esa mujer esta usando a los clientes queer como proyectiles"

    scene bg_mall
    show Rosa lance at half_size
    unkown "Por athenea, estan lloviendo jotos "


    scene bg_mall       
    show bg_mall:
        subpixel True ypos 2.45 zoom 1.82 


    show Daniela at half_size
    show Daniela at right
    show Daniela at flip_image
    show Juan neutral at half_size
    show Juan neutral at left
    show Juan neutral at flip_image
    show Juan neutral:
        subpixel True xpos 0.21
    show Maria neutral at half_size
    show Maria neutral at left
 
    Juan "¿Hay alguna otra salida?"

    Daniela "Sip es por la azotea, debemos ir por las escaleras de emergencia; sígueme"
    "Sigo a Daniela con rumbo hacia las escaleras cuando noto una enorme sombra sobre mi"

    hide Maria neutral 
    hide Juan neutral 
    hide Daniela 
    show Rosa smash at half_size    
    show Rosa smash:
        subpixel True pos (0.29, -191) zoom 0.47 


    Rosa "ERES MIO "

    Juan "OH DIOS, OH DIOS "

    show Rosa beat Daniela
    with vpunch

    
    "Daniela agarra un pedazo de madera  que le dio Maria"
    "y le da un home run  en la cabeza de la señora haciendo que esta caiga hacia otro lado"
    hide Rosa beat Daniela

    "Daniela Abre una puerta cercana"
    Daniela "¿QUE ESPERAS ANIMAL? VÁMONOS ANTES DE QUE DESPIERTE"

    scene bg_stairs
    "Sacudo mi cabeza para salir del shock y obedezco a Daniela, bajando las escaleras acompañado de las dos chicas"

    unkown "Hey tu ¿me escuchas verdad?"

    Juan "No otra vez con las voces.."

    unkown "No empieces con tus lloriqueos. Por la situación en la que te encuentras te conviene hacerme caso, puedo darte el poder que necesitas para darle vuelta a esta. encuéntrame en la azotea"

    Juan "Si claro, hacerle caso a una voz en mi cabeza; que gran idea anótala Mario Hug-"

    Daniela "¿Con quien hablas we?"

    unkown "si fuera tu haría caso, mira lo que hay debajo de las escaleras"
    "Volteo hacia abajo y … CARAJO ES ELLA, ME MIRA FIJAMENTE A LOS OJOS Y  COMENZO A  SALTAR DESDE LAS ESCALARAS REBOTANDO"

    # show black    
    # scene Rosa climb
    # show Rosa climb:
    #     subpixel True crop_relative True xzoom 1.07 yzoom 1.01 zoom 0.41 crop (0.0, -0.01, 1.0, 1.0) 

    scene Rosa climb land

    Rosa "WRYYYY"

    "Juan mira fijamente a maría "
    Juan "¿Cómo CARAJOS DETENEMOS A TU MADRE?"

    Maria "Una vez que ella entra en ese estado nada puede detenerla. Ella es imparable hasta conseguir con su objetivo"

    Daniela "Tal vez si tu hablas con ella y le dices como están las cosas, ¡podamos solucionar esto!"

    # "Maria pone una mirada triste"

    scene bg_stairs
    Maria "Ella dejo de escucharme hace tiempo. Desde que las cosas…. se hicieron complicadas en casa."


    Daniela "Tengo una idea, síganme hacia arriba rumbo a la azotea. "

    jump credits

    return

    "Daniela agarra una mano mía y le señala a María que corramos hacia arriba"

    "Corremos lo más rápido que podamos hasta llegar al último piso donde vemos una puerta color verde. Daniela la abre y entramos todo. El lugar está en construcción."

    Daniela "Juan ayúdame a cerrar la puerta no puedo yo sola. Niña busca bloques y demás materiales para poder bloquear la puerta"

    Juan "¿CREES DE VERDAD QUE ESA PUERTA PUEDA DETENER A LA LOCA?"

    Daniela "No se. Se supone que esta puerta esta hecha de uno de los materiales más resistentes que hay sobre la tierra"

    Maria "Ya regresé ,aquí esta lo que encontré "

    Daniela "Perfecto ponlo por aquí"

    "Daniela nos da indicaciones de como acomodar las cosas alrededor de la puerta"
    #añadir musica de reflexion

    jump en_el_techo
    return

label en_el_techo:
    Daniela "Listo. Espero que esto pueda resistir un rato entre lo que llamo a las autoridades "

    " Daniela agarra su teléfono y empieza a llamar al 9/11 "

    " Se escuchan sonidos de gruñidos y garras de la otra puerta, pero luego de un minuto se detienen "

    Juan "Oye tu ¿a qué te referías con que las cosas están complicadas en casa?"

    "Maria Pone una cara triste"

    Maria "Desde que papa murió, tuvimos varios problemas entre los principales tener que pagar muchas deudas. Mama tuvo que vender su florería y tener que trabajar por varias horas para obtener el suficiente dinero."

    Maria "Luego de un tiempo me acostumbre mucho de solo ver la presencia de mis abuelos en la casa y así fue la situación por un tiempo hasta que mi madre recibió una llamada de un viejo amigo suyo."

    Juan "¿El tal Reed?"

    Maria "Si. Al inicio Reed se acerco a mama porque quería pedirle un concejo sobre que flores podía poner en su mansión para que se viera mas espectacular, así como de técnicas de jardinería para poder mantener en buena calidad los productos que el comercializa. "

    Maria "Luego de enterarse de nuestra situación contrato a mama de forma permanente como la encargada de su jardín. "

    Maria "Al inicio fue algo genial porque ahora ella podía permanecer más tiempo conmigo, pero después de varios meses note como mi madre empezó a recibir regalos de “su amigo” mientras que al mismo tiempo ella empezó a vestirse y maquillarse de forma más linda."

    Maria "Pero luego ocurrió ese día, era el cumpleaños de papa. Ese día lo ocupamos para ir al cementerio y visitar su tumba."

    Maria ". Mama no estaba presente en la casa y le marqué varias veces, pero ella no contestaba, así que fui directamente en donde trabajaba y fue cuando la vi. "

    Maria "Esa mentirosa se estaba besando con ese ODIOSO raptor rosado…"

    Maria "Me sentí muy mal, era su cumpleaños y ella estaba en los brazos de otro. "

    Maria "Posterior a eso nos mudamos a vivir con Reed en su mansión y empezaron los problemas."

    Maria "Mama empezó a criticar mis amistades y algunos aspectos de cómo me visto. Para cuando trate de expresarle de mis incomodidades la escuche decir que estaba pensando en enviar a alguien a una escuela militar. "

    Maria "Estoy segura de que se refería a mi, así como también sospecho que quien le metió esa idea fue ese odioso de Reed"

    Juan "¿Como conociste al tipo que se parecía a mí?"

    Maria "Una amiga al ver el estado pensativo en el que me encontraba me paso el link de un server de Dinoscord en donde pasaban videos y links de anime. "

    Maria "Fue así como empecé a ver anime como el de vaqueros gays llamado Steel Ball Run y el remake de Berserk. "

    Maria "Cuando los terminé le pedí sugerencias a uno de los moderadores, de ahí nació una amistad."

    Maria "Le contaba a veces de mi vida diaria y de cómo me sentía. Fue lindo sentirse escuchada por una vez.  "

    Daniela "Así que toda esta situación es debido a un drama familiar. "

    Juan "Regresaste, ¿Qué te dijeron?"

    Daniela "Que la ayuda viene en media hora"

    unkown "para cuando lleguen los polis ustedes estarán hechos picadillo."

    Juan "Nah la puerta resistirá lo suficiente "

    #(43) Cell Theme - Soundtrack Original Japanese/Español - YouTube

    "Se escucha un enorme ruido proveniente de la puerta y un pedazo sale volando. Del pedazo surje una mano naranja que trata de aflojar la puerta"

    Rosa "¡¡SKINNIIE!!"

    unkown "Te lo dije"

    "Daniela saca de su monedero rojo una imagen de un humano que trae puesto una toga verde y un medallón amarillo. Luego de sacarlo Daniela empieza a juntar sus manos"

    Daniela " ¡Oh venerado San Judas Tadeo! Siervo fiel y amigo de Jesús Raptor. Muchos son los que te honran y te invocan para-"

    Juan "Creo que rezar no servirá"

    " Daniela gira. toda enojada "

    Daniela "¿¡TIENES UNA MEJOR IDEA!?"

    Rosa "¡¡SKINNIIE!!"

    " La puerta sale volando y la doña sale corriendo violentamente hacia mi  "

    Maria "Mamá, ESPERA!"

    Juan "¡¡AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!"

    unkown "Ahora si quieres mi ayuda?"

    Juan "¡¡¡SIIIIIIIIIIIIIIIII!!!"

    unkown "¿seguro?"

    Juan "¡¡QUE SI!!"

    unkown "¿Segurito? "

    Juan "¡¡QUE SI CHINGADA MADRE!!, ¡¡SI QUIERO TU AYUDA!!"

    #SAINT SEIYA Opening Full - Pegasus Fantasy (Cover) (youtube.com)

    " Una luz blanca me empieza a rodear y veo como varios objetos del centro comercial se empiezan a mover hacia a mi "

    unkown "Ahora quédate quieto no quiero rebanarte un dedo. Por lo regular solo bastaría con materializar mi cuerpo alrededor de ti, pero debido a las circunstancias, sumado que me encuentro algo debilitada usare el material que esta alrededor de mi para reconstruir las partes faltantes. Por cierto, mi nombre es pegaso."

    Daniela "¿Qué carajos llevas puesto Juan?"

    Pegaso "¡Ahora caballero ve y enfréntate a la criatura!"

    Maria "¿Esa armadura puede hablar?"

    Juan "Espera ¿Quieres que corra hacia ella? ¡PENSE QUE TU LA DETENDRIAS!"

    Pegaso "Vaya que si se han puesto delicados los mortales pasados los siglos. Mira hare eso, pero no puedo hacerlo desde lejos, necesito que te acerques lo suficiente "
    Juan "¿Y MORIR EN EL INTENTO? Por supuesto que no"

    Pegaso "De todas formas, dudo que sobrevivas a la furia de una latina que te quiere romper los huesos. Así que tu decides, morir intentando defender o morir como cobarde"

    "Mi cara cambia a una de resignacion"
    Juan "....Esta bien"

    "Siguiendo los consejos de la armadura salgo corriendo hacia doñazilla, Jesus raptor en ti confío"

    Pegaso "Deslízate hacia sus piernas para que ella pierda el equilibrio"

    "Hago caso a la armadura logrando que la anquilosaurio resbale, pero ella cae enfrente de mi."

    Rosa "¡OH NO SABANDIJA!"

    "Rosa agarra mi mano izquierda y trata de romperla con toda su fuerza"

    Juan "Mierda si duele, duele feo"

    Pegaso "Extiende tu otra mano, apunta hacia su cabeza y di “Meteoro de Pegaso”"

    Juan "¿Que haga qué? "
    #"insertad sonido de cruijio.mp3"

    Juan "¡AHHHHHHHHH! "

    Pegaso "Si quieres conservar algo de tu mano hazme caso"

    Daniela "¡DEJA A JUAN! "

    " Daniela avienta un bloque de concreto a la cara de Rosa "

    "Con mis fuerzas agarro de mi mano el baston eléctrico y electrocuto a la dinochica logrando que ella me suelte"
    Rosa "¡AHHHHH!"

    "Extiendo mi mano y le doy un puño en su cara para exclamar con todas mis fuerzas "

    Juan "METEORO DE PEGASO"

    "Una luz azul sale de mi brazo que logra que Rosa pueda retroceder por 2 metros "

    Rosa " Así que…. eres un caballero de Athena"

    Pegaso "¿Cómo sabe ella de la existencia de los santos?"

    Rosa "Porque vi el anime durante mi infancia. Pero aun así no podrás escapar de tu destino"

    " Rosa se pone a correr hacia mi otra vez  "

    Pegaso "Esquiva, Patea, pégale en la cara, esquiva, patea, pégale en la mano, salta, esquiva"

    Pegaso "Trata de romperle la pierna izquierda"

    Rosa "Eres un oponente admirable, pero por desgracia yo soy más fuerte  "

    " Rosa usa su cola para agarrarme de la pierna derecha y posteriormente me arroja con fuerza hacia la pared "

    Daniela "¡JUAAAAN!"

    Rosa "Te lo advertí. Sufre las consecuencias."

    Maria "¡Madre detente!"

    Rosa "María por enésima vez ya no quiero escuchar tus mentiras. Me duele enormemente siempre discutir contigo."

    Maria "¡Él no es la persona que me cito!"

    Rosa "Si como no"

    Maria " ¿Por qué nunca me escuchas?  Por eso te odio "

    "Creo que no siento mi mano…."

    Pegaso "Tierra a Juan  "

    Juan "¿Ahora que quieres? "

    Pegaso "Es obvio que no podemos ganar por medio de los puños hay que pensar de otra manera, lo que me lleva a lo siguiente"
    Juan "¿Qué cosa?"

    Pegaso "Mira el piso que está enfrente de nosotros, por la pelea ese piso se empezó a agrietar"

    Juan "¿Lo que implica que?"

    Pegaso "Necesito que la traigas hacia la zona donde hay grietas. Confía en mi"

    "Gran parte de mi cuerpo esta roto. Aunque confié en tu plan no tengo la fuerza suficiente para poder aguantar mas"

    " Daniela avienta un bloque directo a la cara de Rosa "

    Daniela " Anciana. Te crees muy ruda espantando a medio mundo creo que necesitas que te enseñen modales"

    Rosa ": LA QUE NECESITA MODALES ES OTRA. TE ENSEÑARE A RESPETAR A TUS MAYORES"

    Daniela " ¡viene hacia acá Juan!,  !Si vas a hacer algo hazlo ya de una vez¡"

    Pegaso "Espera. Espera"

    Juan "¡pero ahí viene!"

    Pegaso "Espera"

    Juan "Oh mierda"

    Pegaso " Ahora, dale un golpe a ese piso"

    "Extiendo mi brazo bueno, apunto hacia la zona con grietas y grito con todas mis fuerzas "

    Juan "METEORO DE PEGASO "
    "logrando que saliera una estela de luz que choca hacia enfrente de mi"

    Rosa "¿Que carajos? Hehe creo que no funci.."

    "Se escucha un crujido y Rosa pone cara de espantada "

    Rosa "Oh no. "

    " por donde estaba parada Rosa se abre provocando que ella caiga por varios pasillos hacia abajo "

    Rosa "¡¡AHHHHHHHHHHHHHHHHH!!!"

    Maria "¡Mamaaaaaa!"

    " Maria sale corriendo en dirección a la salida "

    Daniela ": Pobre chica, me siento mal por hacerle eso a su.. ¡MADREEEEEEEEEEEEEEEEEEEEE!"

    "La seccion en donde se ubicaba parada Daniela se abre también provocando que ella caiga en el vacio "

    Juan "¡Maldicion! debo salvar a mi amiga. "

    "Sin ningún temor me lanzo hacia el agujero tratando de salvar a mi amiga"
    jump cayendo
    return

label cayendo:
    Pegaso "No creo que sobrevivamos a esto"

    Juan "Tengo una idea, pero necesito impulsarme más hacia dónde está mi amiga ¿alguna sugerencia?"

    Pegaso "Deslízate por las paredes y da un golpe fuerte con el meteoro para poder rebotar con fuerza"

    "Entendido, hago lo que me dictó la armadura logrando que llegue con éxito a mi amiga"

    Juan "¡JUAAAAAAAAN!"
    Juan ": ¡No te preocupes! "
    " la sujeto con mis brazos"

    Juan "¡todo estará bien!"

    Daniela " ¡Pero no creo que podamos librarnos de esto!"

    Juan "Relax mira esto "

    "me acerco a la doña, hago una pose de victoria y doy una patada en el estomago de la anquilosaurio para usar su cuerpo como escudo contra las paredes logrando con éxito caer en el jardín del centro comercial pero no sin antes destruir unas cuantas paredes en el proceso"

    Rosa "..."

    jump al_final
    return

label al_final:
    
    Maria "¡Mama, mama! "
    " la abraza con mucha fuerza "
    Maria "¡Por favor responde!, no te quiero perder a ti también…. "

    Rosa "¿Por qué me odias María? "
    " Rosa pone cara de tristeza "

    Maria "Yo no te odio mama. Solo que desde que papa murió quieres reemplazarlo con alguien mas que no me quiere"

    Rosa "María tu padre siempre tendrá un lugar reservado en nuestros corazones y nunca habrá otro hombre como él. Pero él querría vernos felices viviendo juntas las dos"

    Maria "Si fuera así ¿Por qué me quieren enviar a una escuela de militar?"

    Rosa ": ¿De qué hablas? Yo nunca pensaría en hacerte algo como eso, Preferiría tomar el consejo de Reed de que los 3 vayamos a terapia grupal antes de hacer algo como eso"

    Maria "Pero…. te escuche que dijiste que estás a favor de mandarme a una escuela militar"
    Rosa "Hija. En esa llamada me refería que apoyaba la decisión de unos tíos de mandar a mi primo Arturo a la escuela militar debido a que se la pasaba todo el tiempo en la calle de problemático, de vago o reseñando anime con su supuesta banda musical."

    Maria "Entonces ¿Por qué criticas mi forma de vestir y mis gustos?"

    Rosa "Me dolió enormemente que insultaras mi forma de vestir, pero sobre todo los insultos que le decías a Reed. El ha hecho de todo para aguantar tu actitud e incluso me comento la posibilidad de poder matricularte a esa universidad que tanto deseas ir por medio de sus contactos."

    Maria "...."

    Rosa "Agarra el hombro de María ¿Te gustaría volver a empezar desde cero?"

    Maria "Si"

    " le da un fuerte abrazo a su madre "

    Rosa "Entonces. ¿tu que tienes que ver con mi hija?"

    Juan "Realmente en nada. Reitero me confundieron con alguien mas y se lo puedo demostrar por medio de las cámaras si es que sobrevivió algo del bar"

    Rosa "Perdón por eso… jeje"

    Daniela "No es por ser mala onda pero no la puedo dejar marcharse hasta que se comprometa a pagar todo lo que usted destruyó."

    Rosa "No es por ser mala onda pero no la puedo dejar marcharse hasta que se comprometa a pagar todo lo que usted destruyó."

    Maria "Mama ¿estás segura? Mira por ti misma"

    ## Pongan una imagen del centro comercial con cierta parte en llamas, paredes rotas, el elevador destruido y todo lo demás a punto de romperse 


    Rosa "¿Esa fui yo?"

    Juan "Sip"

    " Se empieza a sonar un celular del bolsillo de Maria y ella contesta la llamada "

    Maria "Buenas"

    Reed "Heyyyyyy hola ¿esta tu madre bien?"

    Maria "Mas o menos "
    Reed "¿Qué paso? Estaba plantando mi carfe cuando recibo varios mensajes de Lucy y Trish donde me mostraban videos de mi novia destrozando un centro comercial"

    Maria "Un malentendido "

    Rosa "¿Quién es?"

    Maria "Es Reed"

    Rosa "Pásamelo. Hola amor, no lo que paso fue que confundí a un humano. Si ya losé Anon se burlaría de nosotros por hacer algo como eso. "

    Reed "¿Qué tanto destrozaste con esos músculos tuyos?"

    Maria "Digamos que ella destruyo casi todo el lugar "

    Reed "No se preocupen,  yo lo pagare, pero necesito que María haga algo por mi"

    Maria "¿Qué necesita que haga?"

    Reed "Que te disculpes con tu madre. Ella aguanto demasiado y sacrifico varias cosas por ti."

    Maria "Ya lo hice papa Reed"

    Reed "¿De verdad lo hizo amor? Espera ¿Cómo me dijiste?"

    Maria "Papa Reed "

    Reed "Vaya. No esperaba que me dijeras así por un buen rato"

    Daniela ": Bueno Juan necesito que te quedes con las chicas y vigiles que no se vayan."

    Daniela "Debo ponerme de acuerdo con los demás comerciantes para saber exactamente que tanto podemos salvar de mercancía asi como de la cantidad que le vamos a cobrar a la señora."

    Daniela "Que día más cardiaco fue este."
    return


label credits:

    play music "Nintendo Wii - Mii Channel Theme.ogg"

    scene credits_continuara

    pause(5.0)

    scene credit

    pause(5.0)

    scene creedit_2

    pause(5.0)

    scene credit_3
    pause(5.0)
return 