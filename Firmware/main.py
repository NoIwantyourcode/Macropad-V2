import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

cols = [board.GP2, board.GP3, board.GP4]
rows = [board.GP5, board.GP6, board.GP7] 

keyboard.col_pins = cols
keyboard.row_pins = rows
keyboard.diode_orientation = "COL2ROW"

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D,
        KC.Z, KC.X, KC.C
    ]
]

if __name__ == '__main__':
    keyboard.go()