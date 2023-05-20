import time
from Displays import LCDDisplay
from Lights import Light, DimLight

class TrafficLight:
    def __init__(self):
        self._display = LCDDisplay(sda=26, scl=27, i2cid=1)

        self._redLight = Light(7, "red")
        self._yellowLight = Light(11, "yellow")
        self._greenLight = Light(22, "green")
        self._whiteLight = DimLight(15, "white")
        self._orangeLight = Light(14, "orange")

        self._button = Button(19, "button", buttonhandler=self, lowActive=True)
        self._cycle_timer = 3

    def go(self):
        self._display.reset()
        self._display.showText("Go / Walk")
        self._greenLight.on()
        self._yellowLight.off()
        self._redLight.off()
        self._whiteLight.on()
        self._orangeLight.off()
        time.sleep(3)

    def caution(self):
        self._display.reset()
        self._display.showText("caution")
        self._greenLight.off()
        self._yellowLight.on()
        self._redLight.off()
        self._whiteLight.off()
        self._orangeLight.off()
        time.sleep(3)

    def stop(self):
        self._display.reset()
        self._display.showText("Stop / Don't Walk")
        self._greenLight.off()
        self._yellowLight.off()
        self._redLight.on()
        self._whiteLight.off()
        self._orangeLight.on()
        time.sleep(3)

    def walk(self):
        self._display.reset()
        self._display.showText("GO / Walk")
        self._greenLight.on()
        self._yellowLight.off()
        self._redLight.off()
        self._whiteLight.on()
        self._orangeLight.off()
        time.sleep(5)

    def dont_walk(self):
        self._display.reset()
        self._display.showText("Stop /Don't walk")
        self._greenLight.off()
        self._yellowLight.off()
        self._redLight.on()
        self._whiteLight.off()
        self._orangeLight.on()
        time.sleep(10)

    def buttonPressed(self, name):
        if name == 'button' and self._display.getText() != "go":
            self._cycle_timer -= 2
            self._cycle_timer = max(self._cycle_timer, 1)

    def buttonReleased(self, name):
        pass

    def cycle(self):
        while True:
            self.go()
            self.caution()
            self.stop()
            self.walk()
            self.caution()
            self.dont_walk()


