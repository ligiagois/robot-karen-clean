from stanfordkarel import *

def turn_right():
    for contador in range(3):
        turn_left()

def girar_180():
    for contador in range(2):
        turn_left()
def mover():
        move()
        if beepers_present():
            pick_beeper()
def caminho():
    while front_is_clear():
        mover()

def main():

    while beepers_in_bag() ==0:
        while right_is_blocked():
            turn_left()
            caminho()
            if beepers_in_bag()==1:
                break
        if right_is_clear():
            turn_right()
            mover()








if __name__ == '__main__':
    run_karel_program('.\maze_8x8_type_I.w')
