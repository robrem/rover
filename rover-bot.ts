music.setVolume(41)
music.playSound(music.sounds(Sounds.PowerUp))
light.showRing(
`green green green green green green green green green green`
)
pause(__internal.__timePicker(500))
forever(function () {
    light.showAnimationFrame(light.rainbowAnimation)
})
forever(function () {
    crickit.motor1.run(100)
    crickit.motor2.run(25)
    pause(__internal.__timePicker(500))
    crickit.motor1.run(25)
    crickit.motor2.run(100)
    pause(__internal.__timePicker(500))
    if (input.acceleration(Dimension.Y) > 200 || input.acceleration(Dimension.Y) < -200) {
        crickit.motor1.stop()
        crickit.motor2.stop()
        crickit.motor1.setInverted(true)
        crickit.motor2.setInverted(true)
        light.showRing(
        "red red red red red red red red red red"
        )
        music.playTone(698, music.beat(BeatFraction.Half))
        pause(__internal.__timePicker(500))
        crickit.motor1.run(90)
        crickit.motor2.run(90)
        pause(__internal.__timePicker(500))
        crickit.motor1.setInverted(false)
        crickit.motor2.setInverted(false)
        crickit.motor1.run(80)
        crickit.motor2.stop()
        pause(__internal.__timePicker(500))
    }
})
