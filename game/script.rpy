# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define carlos = Character("Carlos")
define juan = Character("Juan")
define rosa = Character("Rosa")

#Image of Carlos the Guard
image carlos_ch = "carlos/carlos_neutral.png"
image carlos_ch_angry = "carlos/carlos_angry.png"
image carlos_ch_poker_face = "carlos/carlos_porker_face.png"
image carlos_ch_happy ="carlos/carlos_happy.png"
image carlos_ch_concern = "carlos/carlos_concerned.png"

#Image of Juan the main character
image juan_main_ch = "juan/juan_base.webp"

#Image of Rosa the milf
image rosa_anger = "rosa/rosa_furiosa.png"
image rosa_serious = "rosa/rosa_seria.png"
image rosa_sorprise = "rosa/rosa_sorprendida.png"


image bg_mall = "bg/mall.jpg"

transform half_size:
    zoom 0.39

transform double_size:
    zoom 3.0
    right
        

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_mall

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show carlos_ch at half_size 

    # These display lines of dialogue.

    carlos "Siendo sinceros "

    carlos "El dia va bastante bien"
    
    carlos "Aunque para ser el primer dia, me alegra que todo este bien"

    hide carlos_ch

    show carlos_ch_happy  at half_size

    carlos "Espero poder ir a la tienda de helado, que esta al lado de la tienda de ropa"

    carlos "Escuche que tienen un nuevo helado de menta"

    hide carlos_ch_happy

    show carlos_ch_concern at half_size

    carlos "Aunque siendo sinceros, eso me hace preguntar"

    carlos "por que alguien compraria helado despues de comprar ropa? "

    carlos "No se supone que , la posibilidad de que tu ropa se arruine , incrementa debido a que tienes alimentos con que ensuciarla"

    hide carlos_ch_concern

    show carlos_ch at half_size
    
    carlos "Tal vez estoy pensado demasiado esto "

    show juan_main_ch at double_size

    juan "Hola "

    juan "Me presento para mi primer dia "

    # This ends the game.

    return
