import time
from Displays import *
from Lights import *
from Button import *
from motion_sensor import *
from Model import *
from TrafficLight import *

class TrafficLightController:
    def __init__(self):
        # Two displays for each side of the traffic
        self._display1 = LCDDisplay(sda=26, scl=27, i2cid=1)
        self._display2 = LCDDisplay(sda=2, scl=3, i2cid=1)

        # Lights for each side of the traffic
        self._redLight1 = Light(7, "red")
        self._yellowLight1 = Light(11, "yellow")
        self._greenLight1 = Light(22, "green")

        self._redLight2 = Light(12, "red")
        self._yellowLight2 = Light(16, "yellow")
        self._greenLight2 = Light(23, "green")

        # Pedestrian buttons and PIR sensor
        self._button1 = Button(19, "button1", buttonhandler=None, lowActive=True)
        self._button2 = Button(16, "button2", buttonhandler=None, lowActive=True)
        self._motion_sensor = MotionSensor(1)

        # Traffic light states
        self._state_model = Model(3, self, debug=True)

        # Add transitions for state model
        # "Go" state
        self._state_model.addTransition(0, BTN1_PRESS, 1)
        self._state_model.addTransition(0, BTN2_PRESS, 2)
        # "Caution" state
        self._state_model.addTransition(1, BTN1_PRESS, 0)
        self._state_model.addTransition(1, BTN2_PRESS, 2)
        # "Stop" state
        self._state_model.addTransition(2, BTN1_PRESS, 0)
        self._state_model.addTransition(2, BTN2_PRESS, 1)

        # Turn all lights off initially
        self.lights_off()

    def lights_off(self):
        self._redLight1.off()
        self._yellowLight1.off()
        self._greenLight1.off()
        self._redLight2.off()
        self._yellowLight2.off()
        self._greenLight2.off()

    def display_text(self, text, display):
        display.reset()
        display.showText(text)

    def go(self):
        self.lights_off()
        # Side 1
        self.display_text("Go / Walk", self._display1)
        self._greenLight1.on()

        # Side 2
        self.display_text("Stop / Don't Walk", self._display2)
        self._redLight2.on()

    def caution(self):
        self.lights_off()
        # Both sides
        self.display_text("Caution", self._display1)
        self._yellowLight1.on()
        self.display_text("Caution", self._display2)
        self._yellowLight2.on()

    def stop(self):
        self.lights_off()
        # Side 1
        self.display_text("Stop / Don't Walk", self._display1)
        self._redLight1.on()
        # Side 2
        self.display_text("Go / Walk", self._display2)
        self._greenLight2.on()

    def stateDo(self, state):
        if state == 0:  # "Go" state
            self.go()
        elif state == 1:  # "Caution" state# Continuing the code
                self.caution()
        elif state == 2:  # "Stop" state
            self.stop()

    def stateEntered(self, state):
        print(f'State {state} entered')
        if state == 0:  # "Go" state
            self.display_text("Go / Walk", self._display1)
            self._greenLight1.on()
            self.display_text("Stop / Don't Walk", self._display2)
            self._redLight2.on()
        elif state == 1:  # "Caution" state
            self.display_text("Caution", self._display1)
            self._yellowLight1.on()
            self.display_text("Caution", self._display2)
            self._yellowLight2.on()
        elif state == 2:  # "Stop" state
            self.display_text("Stop / Don't Walk", self._display1)
            self._redLight1.on()
            self.display_text("Go / Walk", self._display2)
            self._greenLight2.on()

    def stateLeft(self, state):
        print(f'State {state} left')

    def cycle(self):
        while True:
            # Check conditions to decide the next state
            if self._motion_sensor.motionDetected():
                self._state_model.processEvent(BTN1_PRESS) 
            elif self._button1.isPressed():
                self._state_model.processEvent(BTN2_PRESS)  
            elif self._button2.isPressed():
                self._state_model.processEvent(BTN3_PRESS)  
            else:
                self._state_model.processEvent(TIMEOUT)  

            time.sleep(3)

    def run(self):
        self.cycle()
