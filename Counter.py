from Displays import *
from Button import *
from Buzzer import *
import time
"""
This is a counter class that will implement a basic
increment reset counter and show the count on a display
"""

class Counter:

    """
    Counter Constructor
    """

    def __init__(self):
        print("Counter: constructor")
        self._number = 0
       
        self._display = LCDDisplay(sda=26, scl=27,i2cid=1)
        
        self._greenButton = Button(17, "increase", buttonhandler=self, lowActive=True)
        self._redButton = Button(16, "reset", buttonhandler=self, lowActive=True)
        self._buzz = PassiveBuzzer(13)
        self._buzz.setVolume(10)
        
    def increment(self):
        print("Counter: incrementing")
        self._number = self._number + 1
        self.buzz()

    def reset(self):
        print("Counter: resetting")
        self._number = 0
        self._display.reset()

    def buttonPressed(self, name):
        if name == 'increase':
            self.increment()
        elif name == "reset":
            self.reset()

    def buttonReleased(self, name):
        pass

    def show(self):
        while True:
            self._display.showNumber(self._number)
            time.sleep(0.1)
            
            
    def buzz(self):
        if self._number == 10:
            self._buzz.beep()