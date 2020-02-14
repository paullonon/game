import os

def you_died(why):
    print_game_over()

    print("{}. Lame!".format(why))


    exit(0)


def guard():
    print_guard()

    print("You approach the guard, he's still sleeping.")
    print("Suddenly you knocked a wooden cask with a mug on it... CRASSH!")
    print("\nOi, what you doing 'ere?")


    guard_moved = False


    while True:
        next_action = input("[run | door] > ").lower()
        if next_action == "run" and guard_moved:
            you_died("Guard was faster than Camerons short legs and your world goes dark...")
        elif next_action == "run" and not guard_moved:
            print("Guard jumps up and looks the other way, missing you entirely.")
            guard_moved = True
        elif next_action == "door" and guard_moved:
            print("You just slipped through the door before the guard realised it.")
            print("You are now outside, home free! Huzzah!")
            return
        elif next_action == "door" and not guard_moved:
            you_died("Guard was faster than Camerons short legs and your world goes dark...")
        else:
            print("Not sure what you meant there... try again.")



def blissful_ignorance_of_illusion_room():
    print_chest()

    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the door")
    

    action = input("What do you do? > ")


    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!") 

        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            for treasure in treasure_chest:
                print(treasure)


            print("What do you want to do?")
            print("Take all {} treasure, press '1'".format(len(treasure_chest)))
            print("Leave it, press '2'")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                print("\tWoohoo! Bounty and a shiney new sword. /drops your crappy sword in the empty treasure chest.")
                print("\tYou just received [{}]".format(", ".join(treasure_chest)))
            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
            

            guard()
    else:

        print("The guard is more interesting, let's go that way!")
        guard()


def painful_truth_of_reality_room():
    print_monster()
    print("There you see the great evil Cthulhu. Who's favorite diet consists of short people.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or cast the Love Commander spell?")

    next_move = input("> ")


    if "flee" in next_move:
        start_adventure()
    if "cast the love commander spell" in next_move
        you_died("You life is over. The Dragon now makes you his sex slave!")  
    if "cast spell" in next_move
        you_died("You life is over. The Dragon now makes you his sex slave!")      
    else:

        you_died("You died. Well, that was tasty!")


def get_player_name():

    name = input("What's your name? > ")


    alt_name = "Rainbow Cameron Unicorn"
    answer = input("Your name is {}, is that correct? [Y|N] > ".format(alt_name.upper()))
    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print("You are fun, {}! Let's begin our adventure!".format(name.upper()))
    elif answer.lower() in ["n", "no"]:
        print("Ok, picky. {} it is. Let's get started on our adventure.".format(name.upper()))
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(alt_name.upper()))
        name = alt_name


    return name

def start_adventure():
    print_dungeon()
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ")


    if door_picked == "red":
        painful_truth_of_reality_room()
    elif door_picked == "blue":
        blissful_ignorance_of_illusion_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

def main():
    os.system("clear")

    player_name =  get_player_name()

    start_adventure()
    
    print("\nThe end\n")
    print("Thanks for playing, {}".format(player_name.upper()))
    


def print_dungeon(): 
    print()
    print("   _________________________________________________________")
    print(" /|     -_-                                             _-  |\ ")
    print("/ |_-_- _                                         -_- _-   -| \   ")
    print("  |                            _-  _--                      | ")
    print("  |                            ,                            |")
    print("  |      .-'````````'.        '(`        .-'```````'-.      |")
    print("  |    .` |           `.      `)'      .` |           `.    |          ")
    print("  |   /   |   ()        \      U      /   |    ()       \   |")
    print("  |  |    |    ;         | o   T   o |    |    ;         |  |")
    print("  |  |    |     ;        |  .  |  .  |    |    ;         |  |")
    print("  |  |    |     ;        |   . | .   |    |    ;         |  |")
    print("  |  |    |     ;        |    .|.    |    |    ;         |  |")
    print("  |  |    |____;_________|     |     |    |____;_________|  |  ")
    print("  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |")
    print("  |  |  / __  ()        -|        -  |  /  __--      -   |  |")
    print("  |  | /        __-- _   |   _- _ -  | /        __--_    |  |")
    print("  |__|/__________________|___________|/__________________|__|")
    print(" /                                             _ -        lc \ ")
    print("/   -_- _ -             _- _---                       -_-  -_ \ ")
    print()

def print_monster():
    print()
    print("                           |                     | ")
    print("                        \     /               \     / ")
    print("                       -= .'> =-             -= <'. =- ")
    print("                          '.'.                 .'.' ")
    print("                            '.'.             .'.' ")
    print("                              '.'.----^----.'.' ")
    print("                               /'==========='\ ")
    print("                           .  /  .-.     .-.  \  . ")
    print("                           :'.\ '.O.') ('.O.' /.':   ")
    print("                           '. |               | .'   ")
    print("                             '|      / \      |' ")
    print("                              \     (o'o)     / ")
    print("                              |\             /| ")
    print("                              \('._________.')/ ")
    print("                               '. \/|_|_|\/ .'                ")
    print("                                /'._______.'\ lc ")
    print()

def print_chest():
    print()
    print("                      _.--. ")
    print("                  _.-'_:-'|| ")
    print("              _.-'_.-::::'|| ")
    print("         _.-:'_.-::::::'  || ")
    print("       .'`-.-:::::::'     || ")
    print("      /.'`;|:::::::'      ||_ ")
    print("     ||   ||::::::'     _.;._'-._ ")
    print("     ||   ||:::::'  _.-!oo @.!-._'-. ")
    print("     ('.  ||:::::.-!()oo @!()@.-'_.| ")
    print("      '.'-;|:.-'.&$@.& ()$%-'o.'-U|| ")
    print("        `>'-.!@%()@'@_%-'_.-o _.|'|| ")
    print("         ||-._'-.@.-'_.-' _.-o  |'|| ")
    print("         ||=[ '-._.-+U/.-'    o |'|| ")
    print("         || '-.]=|| |'|      o  |'|| ")
    print("         ||      || |'|        _| '; ")
    print("         ||      || |'|    _.-'_.-' ")
    print("         |'-._   || |'|_.-'_.-' ")
    print("          '-._'-.|| |' `_.-' ")
    print("              '-.||_/.-' ")
    print()

def print_guard():
    print()
    print("                                                  ___I___ ")
    print("                                                 /=  |  #\ ")
    print("                                                /.__-| __ \ ")
    print("                                                |/ _\_/_ \| ")
    print("                                                (( __ \__)) ")
    print("                                             __ ((()))))()) __ ")
    print("                                           ,'  |()))))(((()|# `. ")
    print("                                          /    |^))()))))(^|   =\ ")
    print("                                         /    /^v^(())()()v^;'  .\ ")
    print("                                         |__.'^v^v^))))))^v^v`.__| ")
    print("                                        /_ ' \______(()_____(   | ")
    print("                                   _..-'   _//_____[xxx]_____\.-| ")
    print("                                  /,_#\.=-' /v^v^v^v^v^v^v^v^| _| ")
    print("                                  \)|)      v^v^v^v^v^v^v^v^v| _| ")
    print("                                   ||       :v^v^v^v^v^v`.-' |#  \, ")
    print("                                   ||       v^v^v^v`_/\__,--.|\_=_/ ")
    print("                                   ><       :v^v____|  \_____|_ ")
    print("                                ,  ||       v^      /  \       / ")
    print("                               //\_||_)\    `/_..-._\   )_...__\ ")
    print("                              ||   \/  #|     |_='_(     |  =_(_ ")
    print("                              ||  _/\_  |    /     =\    /  '  =\ ")
    print("                               \\\/ \/ )/ gnv |=____#|    '=....#| ")
    print()

def print_game_over():
    print()
    print("   _____          __  __ ______    ______      ________ _____  ")
    print("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
    print(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
    print(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
    print(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
    print("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\\")
    print()

if __name__ == '__main__':
    main()