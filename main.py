from TrafficLight import *

# Create an instance of the TrafficLight class
traffic_light = TrafficLight()

# Start a new thread to display the traffic light state on the LCD
def run_traffic_light(traffic_light):
    traffic_light.cycle()

run_traffic_light(traffic_light)

# Start the main loop
while True:
    pass
