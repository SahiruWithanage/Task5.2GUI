import tkinter as tk
import RPi.GPIO as GPIO

# Set up GPIO to standard BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins for LEDs
RED_PIN = 11
GREEN_PIN = 12
BLUE_PIN = 13

# Initialize GPIO pins for LEDs
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Set up PWM for each LED
red_pwm = GPIO.PWM(RED_PIN, 100) 
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

# Start PWM with 0% duty cycle
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Function to update PWM duty cycle based on slider value
def update_pwm(slider_value, pwm):
    duty_cycle = int(slider_value)
    pwm.ChangeDutyCycle(duty_cycle)

# Create GUI window
root = tk.Tk()
root.title("LED Intensity Control")

# Create sliders for each LED
red_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Red LED", command=lambda value: update_pwm(value, red_pwm)).pack()
green_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Green LED", command=lambda value: update_pwm(value, green_pwm)).pack()
blue_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Blue LED", command=lambda value: update_pwm(value, blue_pwm)).pack()

# Run the GUI
root.mainloop()

# Clean up GPIO
red_pwm.stop()
green_pwm.stop()
blue_pwm.stop()
GPIO.cleanup()
