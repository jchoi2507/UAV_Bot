# Import Necessary Libraries
from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
import time

step_pin = 22
dir_pin = 23
current_step = 0
joybitval = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

# Define functions to execute based on button being pressed
class MyController(Controller):
        def __init__(self, **kwargs):
                Controller.__init__(self,**kwargs)
                self.interrupt = False

        def on_R3_right(self,joy_value):
                self.interrupt = True
                global current_step
                global joybitval
                joybitval = joy_value

                target_step = self.map(joy_value,map_max=50,map_min=-50)
                for _ in range(abs(target_step-current_step)):
                        if current_step > target_step:
                                current_step -= 1
                                GPIO.output(dir_pin,GPIO.LOW)

                                GPIO.output(step_pin,GPIO.HIGH)
                                time.sleep(0.001)
                                GPIO.output(step_pin,GPIO.LOW)
                                time.sleep(0.001)

                        if current_step < target_step:
                                current_step += 1
                                GPIO.output(dir_pin,GPIO.HIGH)

                                GPIO.output(step_pin,GPIO.HIGH)
                                time.sleep(0.001)
                                GPIO.output(step_pin,GPIO.LOW)
                                time.sleep(0.001)

                        print("Current Step:", current_step)

                        if self.interrupt:
                                break

        def on_R3_left(self,joy_value):
                self.interrupt = True
                global current_step
                global joybitval
                joybitval = joy_value

                target_step = self.map(joy_value,map_max=50,map_min=-50)
                for _ in range(abs(target_step-current_step)):
                        if current_step > target_step:
                                current_step -= 1
                                GPIO.output(dir_pin,GPIO.LOW)

                                GPIO.output(step_pin,GPIO.HIGH)
                                time.sleep(0.001)
                                GPIO.output(step_pin,GPIO.LOW)
                                time.sleep(0.001)

                        if current_step < target_step:
                                current_step += 1
                                GPIO.output(dir_pin,GPIO.HIGH)

                                GPIO.output(step_pin,GPIO.HIGH)
                                time.sleep(0.001)
                                GPIO.output(step_pin,GPIO.LOW)
                                time.sleep(0.001)
                        if self.interrupt:
                                break
        def on_R3_x_at_rest
                global joybitval
                if joybitval == 0
                        target_step = 0

        def map(self, analog_value, map_max, map_min):
                return int(((analog_value + 32768)/65535)*(map_max-map_min)+map_min)

        def constrain(self, value, max, min):
                if value > max: return max
                elif value < min: return min
                else: return value

if __name__ == "__main__":
        # Create controller at interface 'dev/input/js0'
        controller = MyController(interface='/dev/input/js0', connecting_using_ds4drv=False)

        # Listen for events and execute associated GPIO commands
        controller.listen()

