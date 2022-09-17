"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
# Declaramos inidvidualmente los modulos importados
from random import shuffle
from turtle import tracer, hideturtle, addshape, setup, stamp
from turtle import ontimer, update, write, goto, up, begin_fill
from turtle import shape, clear, end_fill, left, forward
from turtle import color, down, done, onscreenclick
from freegames import path

# Declaracion de variables
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
# Contadores
numTaps = 0
pares = 0
fin = False


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global numTaps
    global pares
    global fin

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        pares += 1


# Contador de los clicks que se da en la pantalla
    numTaps += 1
    print("Numero total de clicks ", numTaps)
    print("Pares enocntrados: ", pares)
    print("")
# Indica cuando se enontraon todos los pares de cartas
    if (pares == 32):
        print("Ganaste!!!!!")
        fin = True
# Termina el juego


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+25, y+10)

        write(tiles[mark], align='center', font=('Arial', 15, 'bold'))

    if (fin):
        return

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
