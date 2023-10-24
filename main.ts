// *Rotation forte anti-horaire
// - S1 : servo gauche ; S2 : Servo droite
microbitApp.compassButtonDown(CompassButtonOption.W, function () {
    motor.servo(motor.Servos.S1, 0)
    motor.servo(motor.Servos.S2, 180)
    basic.showLeds(`
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        `)
})
// *Marche avant et virage horaire et virage lent gauche et droite
// - S1 : servo gauche ; S2 : Servo droite
microbitApp.compassButtonDown(CompassButtonOption.N, function () {
    motor.servo(motor.Servos.S1, 0)
    motor.servo(motor.Servos.S2, 0)
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
})
// *Montée
// - S1 : servo gauche ; S2 : Servo droite
microbitApp.compassButtonDown(CompassButtonOption.NE, function () {
    motor.servo(motor.Servos.S1, 90)
    motor.servo(motor.Servos.S2, 90)
    basic.showLeds(`
        # . . . #
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        `)
})
bluetooth.onBluetoothConnected(function () {
    basic.showString("C")
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showString("D")
})
// *Rotation forte horaire
// - S1 : servo gauche ; S2 : Servo droite
microbitApp.compassButtonDown(CompassButtonOption.E, function () {
    motor.servo(motor.Servos.S1, 180)
    motor.servo(motor.Servos.S2, 0)
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
})
basic.showIcon(IconNames.SmallSquare)
