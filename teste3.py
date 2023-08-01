from stanfordkarel import *

mov = 0

def mover():
    move()
    put_beeper()
    global mov
    mov = mov +1

def giro_esq():
    turn_left()
    global mov
    mov = mov +1
def mover_lado():
    while front_is_clear():
        mover()

def girar_direita():
    for i in range(3):
        giro_esq()

def mover_lado_interior():
    for i in range(6):
        mover()

def mover_esquina():
    giro_esq()
    mover()
    giro_esq()

def mover_esquina_interior():
    girar_direita()
    mover()
    girar_direita()

def zig_zag():
    mover_esquina()
    mover_lado_interior()
    mover_esquina_interior()
    mover_lado_interior()

def varredura():
    mover_lado()
    giro_esq()
    mover_lado()
    zig_zag()
    zig_zag()
    zig_zag()
    mover_esquina()
    mover_lado()
    giro_esq()


def main():
    varredura()
    print(f'Quantidade de movimentos: ', mov)


if __name__ == '__main__':
    run_karel_program()
