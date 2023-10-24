# *Rotation forte anti-horaire
# - S1 : servo gauche ; S2 : Servo droite

def on_compass_button_down_w():
    motor.servo(motor.Servos.S1, 0)
    motor.servo(motor.Servos.S2, 260)
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
microbitApp.compass_button_down(CompassButtonOption.W, on_compass_button_down_w)

# *Marche avant et virage horaire et virage lent gauche et droite
# - S1 : servo gauche ; S2 : Servo droite

def on_compass_button_down_n():
    motor.servo(motor.Servos.S1, 0)
    motor.servo(motor.Servos.S2, 0)
    basic.show_leds("""
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        """)
microbitApp.compass_button_down(CompassButtonOption.N, on_compass_button_down_n)

# *Montée
# - S1 : servo gauche ; S2 : Servo droite

def on_compass_button_down_ne():
    motor.servo(motor.Servos.S1, 90)
    motor.servo(motor.Servos.S2, 90)
    basic.show_leds("""
        # . . . #
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        """)
microbitApp.compass_button_down(CompassButtonOption.NE, on_compass_button_down_ne)

def on_bluetooth_connected():
    basic.show_string("C")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_string("D")
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

# *Rotation forte horaire
# - S1 : servo gauche ; S2 : Servo droite

def on_compass_button_down_e():
    motor.servo(motor.Servos.S1, 180)
    motor.servo(motor.Servos.S2, 0)
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
microbitApp.compass_button_down(CompassButtonOption.E, on_compass_button_down_e)

basic.show_icon(IconNames.SMALL_SQUARE)