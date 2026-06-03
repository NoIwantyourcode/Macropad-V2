import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())  # Enable layer support

cols = [board.GP2, board.GP3, board.GP4]  # Example column pins
rows = [board.GP5, board.GP6, board.GP7]  # Example row pins

keyboard.col_pins = cols
keyboard.row_pins = rows
keyboard.diode_orientation = "COL2ROW"

keyboard.keymap = [
    # Layer 0
    [
        KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D,
        KC.Z, KC.X, KC.C
    ]
]

if __name__ == '__main__':
    # Start the keyboard firmware
    keyboard.go()