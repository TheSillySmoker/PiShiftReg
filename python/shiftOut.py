from pi74HC595 import pi74HC595
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
shift_register = pi74HC595()

def __init__(
        DS: int = 11, # gpio.BOARD
        ST: int = 13,
        SH: int = 15,
        daisy_chain: int = 1,
    ):
    shift_register = pi74HC595(35, 21, 20)
    shift_register.set_by_list([0, 1, 0, 1, 1, 1, 0, 0])