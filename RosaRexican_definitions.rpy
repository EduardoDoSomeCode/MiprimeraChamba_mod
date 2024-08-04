init python:
    mod_menu_access += [{
        'Name': "Mi primera chamba",
        'Label' : "Mi_primera_chamba_start"
    }]

init:
    $RosaRexican = "mods/Mi primera chamba/"

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Carlos = Character("Carlos", color="#c8ffc8")
define Juan = Character("Juan", color="#ADD8E6")
define Rosa = Character("Rosa" ,color="#FFC0CB")
define unknowdaniela = Character("???" ,color="#90EE90") 
define Luis = Character("Luis", color="#FFA500")
define Maria =Character("Maria")
define Daniela = Character("Daniela",color="#90EE90")
define unknow= Character("???", color= "#FF0000" )
define unknowmaria= Character("???")
define Don = Character("Don")
define Pegaso = Character("Pegaso")
define Reed =Character("Reed")


#Image of Carlos the Guard
image Carlos neutral= RosaRexican + "carlos/carlos neutral.png"
image Carlos angry= RosaRexican + "carlos/carlos angry.png"
image Carlos poker_face= RosaRexican + "carlos/carlos porker_face.png"
image Carlos happy=RosaRexican + "carlos/carlos happy.png"
image Carlos concern= RosaRexican + "carlos/carlos concerned.png"
image Carlos ice angry = RosaRexican +"carlos/icecream carlos angry.png"
image Carlos ice concerne = RosaRexican +"carlos/icecream carlos concerned.png"
image Carlos ice happy = RosaRexican +"carlos/icecream carlos happy.png"
image Carlos ice neutral = RosaRexican +"carlos/icecream carlos neutral.png"
image Carlos ice poker = RosaRexican +"carlos/icecream carlos pokerface.png"
image Carlos spin = RosaRexican +"carlos/so_long_gei_carlos.png"


#Image of Juan the main character
image Juan neutral= RosaRexican + "juan/juan neutral.png"
image Juan surprise= RosaRexican + "juan/juan surprised.png"
image Juan suspicious= RosaRexican + "juan/juan suspicious.png"
image Juan concerned= RosaRexican + "juan/juan concerned.png"
image Juan normal = RosaRexican + "juan/juan pre neutral.png"


#Image of Rosa the milf
image Rosa angry= RosaRexican +"rosa/rosa furiosa.png"
image Rosa serious= RosaRexican +"rosa/rosa seria.png"
image Rosa sorprise= RosaRexican +"rosa/rosa sorprendida.png"
image Rosa angry real = RosaRexican +"rosa/rosa angry.png"
image Rosa elevator = RosaRexican +"rosa/rosa elevator.png"
image Rosa lance = RosaRexican +"rosa/rosa_lanzamiento_perfecto.png"
image Rosa smash = RosaRexican +"rosa/Rosa_smash.png"
image Rosa beat Daniela = RosaRexican +"rosa/kathwack_color.png"
image Rosa climb = RosaRexican +"rosa/rosadio.jpg"
image Rosa climb land =RosaRexican +"rosa/rosadiobl.png"


#Image of Maria the daughter
image Maria neutral= RosaRexican + "maria/maria neutral.png"
image Maria happy= RosaRexican + "maria/maria feliz.png"
image Maria sorprise= RosaRexican + "maria/maria impactada.png"
image Maria angry= RosaRexican + "maria/maria enojada.png"
image Maria sad = RosaRexican +"maria/maria sad.png"
image Maria shame = RosaRexican +"maria/Maria_shamed.png"

#Image of Luis the Velociraptor
image Luis neutral= RosaRexican + "luis/luis neutro.png"
image Luis happy= RosaRexican + "luis/luis felih.png"
image Luis angry= RosaRexican + "luis/luis nojao.png"
image Luis sad= RosaRexican + "luis/luis trite.png"
image Luis fear= RosaRexican + "luis/luis cagao.png"
image Luis raqueta = RosaRexican + "luis/raqueta_raptor_color_blur.png"
image Luis raqueta space = RosaRexican + "luis/raqueta_raptor_color_blur.webp"

#Image of Daniela
image Daniela = RosaRexican + "daniela/daniela neutral.png"
image Daniela surprise= RosaRexican + "daniela/daniela surprised.png"
image Daniela happy= RosaRexican + "daniela/daniela happy.png"
image Daniela hopeless= RosaRexican + "daniela/daniela hopeless.png"
image Daniela angry= RosaRexican + "daniela/daniela angry.png"


#Image of the grommer 
image Groomer angry= RosaRexican + "don/groomer angry.png" 
image Groomer happy= RosaRexican + "don/groomer happy.png"
image Groomer neutral= RosaRexican + "don/groomer neutral.png"
image Groomer sad= RosaRexican + "don/groomer sad.png"


image guardia = RosaRexican +"extras/guardia generico/guardia apuntando.png"
image guardia fail =RosaRexican +"extras/guardia generico/guardia lanzado.png"

image ballo = RosaRexican +"bdf.png"
image chair normal = RosaRexican+"chair.png"



# style narrator:
#     italic True
    
#load music assets

image bg_elevator :
    zoom 0.5
    (RosaRexican + "bg/elevator.png")
image bg_mall:
    zoom 0.5
    (RosaRexican + "bg/mall.jpg")

image bg_bar:
    zoom 0.8 
    (RosaRexican + "bg/restaurant.jpg")

image  bg_office:
    zoom 0.38
    (RosaRexican + "bg/office.jpg")

image bg_office_rom:
    zoom 2.0
    (RosaRexican + "bg/officeroom.jpg")

image bg_rosa:
    zoom 2.0
    (RosaRexican + "rosa/rosa elevator.png")

image bg_stairs:
    (RosaRexican +"bg/stairs.jpg")

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

image credits_continuara:
    RosaRexican + "bg/continuara.png"
image credit:
    RosaRexican +"bg/credit1.png"
image creedit_2:
    RosaRexican +"bg/credit2.png"
image credit_3:
    RosaRexican +"bg/credit3.png"
