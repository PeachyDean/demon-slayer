from sys import exit
from os import system
from os import name
from random import randint

# ENABLE ESCAPE CODES
system("")


def green_text(text):
    print("\033[92m", text, "\033[0m")


def red_text(text):
    print("\033[91m", text, "\033[0m")


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def pause():
    i = input("\nPress enter to continue... ")


def game_over():
    red_text("""
 _____   ___  ___  ___ _____     _____  _   _ ___________ _ 
|  __ \ / _ \ |  \/  ||  ___|   |  _  || | | |  ___| ___ \ |
| |  \// /_\ \| .  . || |__     | | | || | | | |__ | |_/ / |
| | __ |  _  || |\/| ||  __|    | | | || | | |  __||    /| |
| |_\ \| | | || |  | || |___    \ \_/ /\ \_/ / |___| |\ \|_|
 \____/\_| |_/\_|  |_/\____/     \___/  \___/\____/\_| \_(_)

    """)
    pause()
    exit()


def demon_slain():
    red_text("""

__   _______ _   _     _   _   ___  _   _ _____     _____ _       ___  _____ _   _ 
\ \ / /  _  | | | |   | | | | / _ \| | | |  ___|   /  ___| |     / _ \|_   _| \ | |
 \ V /| | | | | | |   | |_| |/ /_\ \ | | | |__     \ `--.| |    / /_\ \ | | |  \| |
  \ / | | | | | | |   |  _  ||  _  | | | |  __|     `--. \ |    |  _  | | | | . ` |
  | | \ \_/ / |_| |   | | | || | | \ \_/ / |___    /\__/ / |____| | | |_| |_| |\  |
  \_/  \___/ \___/    \_| |_/\_| |_/\___/\____/    \____/\_____/\_| |_/\___/\_| \_/
                                                                                   
                                                                                   
              _____ _   _  _____    ______ ________  ________ _   _ _              
             |_   _| | | ||  ___|   |  _  \  ___|  \/  |  _  | \ | | |             
               | | | |_| || |__     | | | | |__ | .  . | | | |  \| | |             
               | | |  _  ||  __|    | | | |  __|| |\/| | | | | . ` | |             
               | | | | | || |___    | |/ /| |___| |  | \ \_/ / |\  |_|             
               \_/ \_| |_/\____/    |___/ \____/\_|  |_/\___/\_| \_(_)             
                                                                                   
    """)
    pause()
    exit()


def health_check(dict):
    clear_screen()

    if dict['hits'] < 1:
        red_text("""
All the damage you have sustained so far has taken its toll...

You are no more.
You are an ex adventurer.
You have gone to meet your maker.
You have shuffled off this mortal coil.
You are DEAD.
        """)
        game_over()


def menu_master(status, options, prompt):
    menu_print(status, options, prompt)
    return menu_input(options)


def menu_print(status, options, prompt):
    green_text(f"{status}\n")
    for i in range(len(options)):
        green_text(f"{i + 1}. {options[i]}")
    print(f"\n{prompt}")


def menu_input(options):
    try:
        value = int(input())
    except:
        value = 0
    if value < 0 or value > len(options):
        value = 0
    return value


# ENCOUNTER FUNCTIONS


def first_name(dict):
    first_status = """
You there! What is your name?
    """
    first_options = ["Jimmy", "Johnny", "Jenny", "Jinny"]
    first_prompt = "Please choose one of these names..."

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(first_status, first_options, first_prompt)
    dict['first'] = first_options[answer - 1]
    green_text(f"\nHello {dict['first']}!\n")


def second_name(dict):

    second_status = f"""
Hello {dict['first']}. What is your last name?
    """
    second_options = ["Rumpleback", "Bumpleback", "Stumpleback", "Fumpleback"]
    second_prompt = "Please choose one of these names..."

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(second_status, second_options, second_prompt)
    dict['second'] = second_options[answer - 1]


def heroic_quest(dict):
    clear_screen()
    green_text(f"""
It's a pleasure to meet you {dict['first']} {dict['second']}.

Please ensure that your terminal window is maximised to display graphics properly!
    """)
    pause()

    clear_screen()
    green_text(f"""
I have a heroic quest for you to complete.

If you'd like a steep climb,

if you can swerve the killer pirhanas,

and you'd love a good fight with an evil demon,

then you might have what it takes to be the...
    """)
    pause()

    clear_screen()
    red_text("""
                                                                                                                        
 ______ ________  ________ _   _     _____ _       _____   _____________ _ 
 |  _  \  ___|  \/  |  _  | \ | |   /  ___| |     / _ \ \ / /  ___| ___ \ |
 | | | | |__ | .  . | | | |  \| |   \ `--.| |    / /_\ \ V /| |__ | |_/ / |
 | | | |  __|| |\/| | | | | . ` |    `--. \ |    |  _  |\ / |  __||    /| |
 | |/ /| |___| |  | \ \_/ / |\  |   /\__/ / |____| | | || | | |___| |\ \|_|
 |___/ \____/\_|  |_/\___/\_| \_/   \____/\_____/\_| |_/\_/ \____/\_| \_(_)
                                                                           

X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
|                           ,,'``````````````',,                            |
X                        ,'`                   `',                          X
|                      ,'                         ',                        |
X                    ,'          ;       ;          ',                      X
|       (           ;             ;     ;             ;     (               |
X        )         ;              ;     ;              ;     )              X
|       (         ;                ;   ;                ;   (               |
X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
|       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
|       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
| (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
| (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
| (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
|",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
|| ) | \ |/ /#/ |#( \; ;     :               ;     ; ;/ )#| \#\ \| / | ( |) |
X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
| \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
|####@,,'`                 `',               ,'`                 `',,@####| |
X#,,'`                        `',         ,'`                        `',,###X
|'                               ~~-----~~                               `' |
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
                                                                                                                                            
    """)
    pause()


def town_guard(dict):
    health_check(dict)

    guard_status = """
A town guard protects the entrance to the mountain path. He stops you and asks

'Where da ya think you're goin? The mountain is off-limits to PEASANTS like YOU!'
    """
    guard_options = [
        "Point to the left of the guard and shout 'Look over there! Its a Pheasant!', then sneak past him.",
        "Tell the guard 'I'm on a quest to slay the Demon!'",
        "Attack the guard with your dagger."
    ]
    guard_prompt = "Choose one of these options..."

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(guard_status, guard_options, guard_prompt)

    if answer == 1:
        dict['hits'] -= 10
        green_text("""
As you sneak past the guard, he whirls around and slices a chunk out of your back. YIKES!
        """)
        pause()
    elif answer == 2:
        green_text("""
The guard laughs hysterically at you. 'Haha good luck with that one!' he cries as you head on.
        """)
        pause()
    else:
        green_text("""
You strike upwards with your dagger, piercing the guard's throat. Mortally wounded, he slumps to the ground.
        """)
        pause()


def sunset(dict):
    health_check(dict)

    sunset_status = """
After a while of trekking up the mountain path, you realise that the sun is setting.

There's still a long way up to reach the peak and the journey there will take at least a few days.

Your legs feel a bit weary from the long walk but you are also determined to be a hero and bring the demon to his end
as soon as you can.
    """
    sunset_options = [
        "Take a big gulp of spiced rum out of your hip flask, and continue your journey.",
        "Find a place to rest, and regain your strength",
        "Find a place to sleep, and get your head down."
    ]
    sunset_prompt = "Choose one of these options..."

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(sunset_status, sunset_options, sunset_prompt)

    if answer == 1:
        green_text("""
Ahhh that's better! Weary, but refreshed, you continue on your quest.
        """)
        pause()
    elif answer == 2:
        dict['hits'] -= 10
        green_text("""
You get distracted by the beautiful sunset that shines above the forest beneath.

As you sit there and stare pointlessly at the sky you suddenly fall asleep.

In the morning you notice your boots are gone and you have to go barefoot for the rest of the journey.

Oh dear! :(
        """)
        pause()
    else:
        dict['hits'] -= 20
        green_text("""
'This looks like a good spot for a peaceful sleep', you think to yourself looking at the little cave on your right.

But once you enter, you are attacked by a Wild Bearcat mother who was guarding her young pups.

You run out screaming in terror as the Bearcat scratches your back with its claws.

No sleep for you now, so you carry on walking with both your back, and your pride, badly wounded. :(
        """)
        pause()


def rockfall(dict):
    health_check(dict)

    rockfall_status = """
You find yourself coming up to a very narrow winding part of the mountain path, you notice there are a few small pieces
of rock crumbling from the edge of the mountain cliff.

Out of the corner of your eye you spot a crevice that could provide an alternate route, it looks like it may need a bit of
digging as some rocks have blocked it.
    """
    rockfall_options = [
        "Try and open the crevice up.",
        "Carefully traverse the narrow path.",
        "Continue walking without a care in the world."
    ]
    rockfall_prompt = "Which route would you like to take?"

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(
            rockfall_status, rockfall_options, rockfall_prompt)

    if answer == 1:
        dict['hits'] -= 5
        green_text("""
You start to dig out the blockage from the crevice and realise the rocks are heavier than you anticipated.

You crawl through the crevice and through to the other side where the path begins to steady out and you continue your
journey.
        """)
        pause()
    elif answer == 2:
        green_text("""
You put your back up against the wall, and start to shuffle across the narrow path to the other side.
        """)
        pause()
    else:
        green_text("""
As you're walking carelessly, you plant your right foot on a weak part of terrain, and suddenly the mountain cliff begins to
give way. 

You slip comically, as if you're a cartoon character slipping on a banana peel, and fall, rather ungraciously,
right in to the river of killer piranhas. 

They proceed to decimate your corpse before you could make it to the river
bed.
        """)
        game_over()


def mountain_approach(dict):
    health_check(dict)

    mountain_approach_status = """
As you're looking for a place to rest your head, you head towards a little cave entrance that you can see not too far away. 
There are 2 different directions the cave heads off in.
You think to yourself 'I've made it this far so SURELY there's nothing dangerous lurking around here...'
    """
    mountain_approach_options = [
        "Set up by the entrance of the cave.",
        "Head down the left tunnel in the cave.",
        "Head down the right tunnel in the cave."
    ]
    mountain_approach_prompt = "Where would you like to rest?"

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(mountain_approach_status,
                             mountain_approach_options, mountain_approach_prompt)

    if answer == 1:
        green_text("""
It's a long but peaceful night, except for those strange sounds you could hear coming from one of the sections of the cave, 'I sure am glad I didn't go in there!'
        """)
    elif answer == 2:
        dict['hits'] -= 10
        green_text("""
You head down the tunnel of the cave, to find a spot with beautiful carvings on the wall and a cave spring.
You relax, and sleep peacefully for a few hours until suddenly, you're swarmed by giant hornets.

UH OH, TIME TO SCRAM!

You head out of the cave quickly, but not before sustaining some painful bites from the little blighters. :(
    """)
    elif answer == 3:
        dict['sword'] = True
        green_text("""
You make the somewhat long walk through the cave until you reach some steps, what can go wrong heading down man made steps inside of a cave!
You stroll down and as you do the room lights up to reveal a gloriously crafted sword laid out on top of a stone table.

As you pick up the sword from the table, an inscription, carved underneath where it was laid, begins to glow to reveal the following message
'Only the bravest and mighty adventurer may claim the powerful Sword of Anshima, remember the incantation' - 'Reeth' - 'Takha' - 'Moytep'.
    """)
    pause()


def dice_lady(dict):
    health_check(dict)

    dice_status = """
When you are about to start climbing further up you notice an old woman sitting on a rock nearby a big beautiful bush.
'How strange...' you think to yourself.

Curiosity takes over and you approach her.

A woman, dressed in old rags, looks up silently and pulls two dice from her pocket.

You stare at her wrinkly old palm, and the two dirty dice. Will you accept her game invitation?
    """
    dice_options = [
        "Roll the dice and hope for the best.",
        "Refuse to play because you are not a child and have some demon slaying to do.",
        "Pull your dagger out and threaten to kill her."
    ]

    dice_prompt = "Chose one of these options..."

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(
            dice_status, dice_options, dice_prompt)

    if answer == 1:
        roll1 = randint(1, 6)
        roll2 = randint(1, 6)
        total = roll1 + roll2

        if total < 4:
            green_text(f"""
You rolled a {roll1} and a {roll2}.

You thought that spontanous human combustion was a myth?

Well, its real.

Now you're on fire and your face is melting!

Not an ideal way to die. :(
            """)
            game_over()

        elif total < 9:
            dict['hits'] -= 30
            green_text(f"""
You rolled a {roll1} and a {roll2}.

Bad luck! Dice magic has you doubled-up in pain, and drains a part of your life force. :(
            """)
            pause()

        else:
            dict['hits'] = 100
            green_text(f"""
You rolled a {roll1} and a {roll2}.

Lady luck was kind to you for once.

You feel fully refreshed and restored. :)
            """)
            pause()

    elif answer == 2:
        green_text("""
Gambling was never your thing, but that might be because you were just terribly poor...

Anyway, onward and upward you go.

That dastardly demon won't kill itself, will it?
        """)
        pause()

    else:
        dict['hits'] -= 50
        green_text("""
You have angered the old hag - who is a witch.

She puts a spell on you that sucks out the life energy from your body.

Then the sorceress vanishes into thin air!
        """)
        pause()


def bridge(dict):
    health_check(dict)

    bridge_status = """
You've FINALLY reached the peak of the mountain, my god what a terrible journey that was... why did you take this quest exactly? Anyway...

Of course it wouldn't be as simple as just entering the tower would it?

Yep there's an old torn looking bridge with what appears to be, a pool of lava below!

Well you're going to have to make a choice here, you can't bring yourself to go back down after all of this effort surely? Onwards.
    """
    bridge_options = [
        "Walk across the bridge normally because you don't have any fear left in you at this point.",
        "Slowly tip toe across the bridge ensuring you don't misstep on any weak planks.",
        "Run across the bridge as fast as you can, because why would anyone want to go slow?"
    ]
    bridge_prompt = "So, how brave are you really?"

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(
            bridge_status, bridge_options, bridge_prompt)

    if dict['second'] == "Stumpleback":
        green_text("""
There is being a giant, useless klutz... and there's you. 
When attempting to skip over a small hole between damaged bridge planks you tripped over and nearly fell into the lava.
Good save, but why did you think this is a good time for a victory dance?

One of the flimsy wooden planks broke under your feet while you were midway your victorious pirouette, and you plummet right into a scorching lava pool. 
Great job, prima ballerina...
            """)
        game_over()

    elif answer == 1:
        green_text("""
You successfully cross the bridge to the entrance of the tower and are ready to finally take on this annoyingly out of the way demon!
        """)
        pause()
    elif answer == 2:
        green_text("""
You successfully, but rather slowly, cross the bridge, good job slowpoke.
        """)
        pause()

    elif answer == 3 and dict['sword'] == False:
        green_text("""
You successfully sprint across the bridge somehow...
        """)
        pause()
    elif answer == 3 and dict['sword'] == True:
        green_text("""
You successfully sprint across the bridge somehow...
But as you get to the end you realise your Sword of Anshima has fallen into the lava below.
Oh dear... well you started the quest without it anyway. :(
        """)
        dict['sword'] = False
        pause()


def boss_fight(dict):
    if dict['sword'] == True:
        boss_fight_with_sword(dict)
    else:
        boss_fight_without_sword(dict)


def boss_fight_with_sword(dict):
    bossfight_status = (f"""
You purposefully walk up to the massive entrance to the tower of which both doors are wide open and prepare yourself
for the battle that is about to come.

'Ahahaha, you there little human, what purpose do you have being here in MY tower?'

'I AM {dict['first'].upper()} {dict['second'].upper()} AND I'VE COME TO S...S...SLAY YOU!!!' you shout whilst nervously,
now realising the sheer size of this monstrosity.
    """)

    bossfight_options = [
        "Reeth, Takha, Moytep",
        "Takha, Moytep, Reeth",
        "Moytep, Reeth, Takha"
    ]

    bossfight_prompt = "Now what was that incantation again?"

    answer = 0
    while answer == 0:
        clear_screen()
        answer = menu_master(
            bossfight_status, bossfight_options, bossfight_prompt)

    if answer == 1:
        green_text("""
As you shout the correct incantation your Sword of Anshima begins to glow extremely bright and you feel a rush of power
flow through you. You pierce the demon straight through the chest and it falls to it's knees
        """)
        red_text(f"""
'HOW?!?! THIS WILL NOT BE THE LAST TIME WE MEET {dict['first'].upper()} {dict['second'].upper()}!'
        """)
        green_text("""
The demon shatters into a million pieces.
        """)
        demon_slain()

    else:
        green_text("""
As you shout the incantation, nothing happens. There's a brief silence. The demon begins to grow even larger in stature
and seems to have gained power from the words you said.
""")
        red_text("""
'YOU FOOL! YOUR IDIOCY HAS INCREASED MY POWER!
NOW I AM STRONG ENOUGH TO KILL YOU ALL!'
""")
        green_text("""
The demon looks at you with a devilish smirk and slams his fist down on the ground, the force of which, shatters every bone in your body. 
In the final seconds of life, you realise, that you screwed up :(
""")
        game_over()


def boss_fight_without_sword(dict):
    boss_hp = 150
    clear_screen()

    green_text("""
You purposefully walk up to the massive entrance to the tower.
Both doors are wide open, and you prepare yourself for the battle that is about to come...
    """)
    red_text("""
'YOU THERE, TINY HUMAN.
 YOU DARE ENTER MY TOWER?'
    """)
    green_text(f"""
'I AM {dict['first'].upper()} {dict['second'].upper()} AND I'VE COME TO S...S...SLAY YOU!!!' you shout nervously,
now realising the sheer size of this monstrosity.
    """)
    pause()

    while boss_hp > 0:
        num = randint(1, 3)
        if num == 1:
            green_text("""
You strike a blow at the demon!
            """)
            boss_hp -= 50
            pause()
        else:
            red_text("""
The demon strikes a blow at you!
            """)
            pause()
            dict['hits'] -= 50
            health_check(dict)

    demon_slain()

# MAIN FUNCTION


def main():
    game = {'sword': False, 'hits': 100, 'first': "", 'second': ""}

    first_name(game)
    second_name(game)
    heroic_quest(game)
    town_guard(game)
    sunset(game)
    rockfall(game)
    mountain_approach(game)
    dice_lady(game)
    bridge(game)
    boss_fight(game)


# ENTRY POINT WITH NAME GUARD
if __name__ == '__main__':
    main()
