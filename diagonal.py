from stanfordkarel import *

mov = 0
def mover():
    move()
    put_beeper()
    global  mov
    mov = mov + 1

def giro_esq():
    turn_left()
    global mov
    mov = mov +1
def girar_direita():
    for i in range(3):
        giro_esq()

def girar_180():
    for i in range(2):
        giro_esq()

def esquina_esquerda():
    mover()
    girar_direita()
    mover()
    girar_direita()

def mover_diagonal():
    mover()
    giro_esq()
    mover()

def diagonal_central():
    while front_is_clear():
        mover_diagonal()
        girar_direita()


def diagonal_1(x):
    for i in range(x):
        mover_diagonal()
        girar_direita()

def diagonal_back():
    for i in range(4):
        mover()
        girar_direita()
        mover()
        giro_esq()

def diagonal_back_1():
    for i in range(3):
        giro_esq()
        mover()
        girar_direita()
        mover()

def diagonal_6():
    for i in range(5):
        girar_direita()
        mover_diagonal()

def diagonal_7():
    for i in range(4):
        giro_esq()
        mover()
        girar_direita()
        mover()

def diagonal_8():
    for i in range(3):
        girar_direita()
        mover_diagonal()

def diagonal_9():
    for i in range(2):
        giro_esq()
        mover()
        girar_direita()
        mover()

def diagonal_total():
    put_beeper()
    diagonal_central()
    girar_180()
    diagonal_1(6)
    esquina_esquerda()
    diagonal_1(5)
    girar_180()
    diagonal_1(4)
    esquina_esquerda()
    diagonal_1(3)
    girar_180()
    diagonal_1(2)
    esquina_esquerda()
    mover_diagonal()
    giro_esq()
    mover()
    girar_180()
    diagonal_back()
    diagonal_back_1()

    girar_direita()
    mover()

    diagonal_6()


    giro_esq()
    mover()

    diagonal_7()

    girar_direita()
    mover()

    diagonal_8()

    giro_esq()
    mover()

    diagonal_9()

    girar_direita()
    mover()
    girar_direita()
    mover()
    giro_esq()
    mover()
    giro_esq()
    mover()



def main():
   diagonal_total()
   print(f'Quantidade de movimento: ', mov)


if __name__ == '__main__':
    run_karel_program()