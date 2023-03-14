# Takes a turn, where each opponent uses an action against eachother
def turn(opponent1, opponent2, turn_counter):
    print("Starting turn " + str(turn_counter))
    opponent1.tick_skills()
    opponent2.tick_skills()
    opponent1.take_action(opponent2)
    opponent2.take_action(opponent1)


# Combat loop
def combat(opponent1, opponent2):
    turn_counter = 1
    print("You encounter a ", end="")
    opponent2.print_self()
    while opponent1.alive and opponent2.alive:
        # If they are both still alive, determines next turn order by speed comparison
        if opponent1.speed >= opponent2.speed:
            turn(opponent1, opponent2, turn_counter)
        else:
            turn(opponent2, opponent1, turn_counter)
        turn_counter += 1
