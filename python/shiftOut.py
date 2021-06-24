from pi74HC595 import pi74HC595
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
shift_register = pi74HC595()


shift_register = pi74HC595(35, 21, 20)
shift_register.set_by_list([0, 1, 0, 1, 1, 1, 0, 0])