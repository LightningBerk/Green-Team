#The following functions contain the pin outputs for their respective colors
#These funtions use digital pin outputs, meaning that the pin can either be off or on.
#Analog pin outputs can assign a specific amount of power to a pin which allows for more color 
#variety in the LED. We dont need analog for this project.
def Cyan():
    pins.digital_write_pin(DigitalPin.P0, 0) #sets pin 0 to off
    pins.digital_write_pin(DigitalPin.P1, 1) #sets pin 1 to on
    pins.digital_write_pin(DigitalPin.P2, 1) #sets pin 2 to on
def Yellow():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
def Magenta():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
def Green():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
def Blue():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
def Red():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
#What will happen when button A is pressed. In this case it will display our team name
def on_button_pressed_a():
    basic.show_string("Green Team") #Scrolls "Green Team" across the LED display
#Calls the Button A function when button A is pressed
input.on_button_pressed(Button.A, on_button_pressed_a)
#What will happen when button B is pressed. 
#This line calls all of the color functions defined earlier when button B is pressed
def on_button_pressed_b():
    while True: #The lines in this indent will loop indifenitly until 
                #the reset button is pressed
        Red() #Calls the color function
        basic.pause(500) #Pauses for half a second before moving to the next line
        Green()
        basic.pause(500)
        Blue()
        basic.pause(500)
        Cyan()
        basic.pause(500)
        Yellow()
        basic.pause(500)
        Magenta()
        basic.pause(500)
#Calls the button B function when the B button is pressed
input.on_button_pressed(Button.B, on_button_pressed_b)

