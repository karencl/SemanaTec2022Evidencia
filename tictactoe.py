from turtle import update, setup, onscreenclick, down
from turtle import hideturtle, tracer, done, up, goto, circle

from freegames import line

SIZE = 100  # Tamaño del cuadrícula

board = [False for i in range(9)]  # Arreglo para detectar los lugares


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    diff = 133 - SIZE  # Diferencia entre el tamaño de la cuadrícula y el icono
    line(x+diff, y+diff, x + SIZE, y + SIZE)
    line(x+diff, y + SIZE, x + SIZE, y+diff)


def drawo(x, y):
    """Draw O player."""
    diff = 133 - SIZE
    up()
    goto(x + 67, y + diff//2 + 10)
    down()
    circle(SIZE//2 - 10)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    # Encuentra el índice correspondiente
    index = int((x+200)//133 + (abs(y-66))//133*3)

    # Checa si ya está en uso
    if not board[index]:
        board[index] = True
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player


# Crea una nueva ventana
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Dibuja el grid
grid()
update()

# Detecta la interacción del usuario
onscreenclick(tap)
done()
