import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation 

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

cols = [board.D0, board.D1, board.D2]
rows = [board.D3, board.D4, board.D5] 

keyboard.col_pins = cols
keyboard.row_pins = rows

keyboard.diode_orientation = DiodeOrientation.COL2ROW 

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D,
        KC.Z, KC.X, KC.C
    ]
]

if __name__ == '__main__':
    keyboard.go()
