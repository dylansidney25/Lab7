from guizero import App, PushButton
from gpiozero import LED

led17 = LED(17)

def GPIO_17():
    if button1.text == "GPIO17_ON ":      #this line checks if the button is currently seeing GPIO17_ON
        button1.text = "GPIO17_OFF"       #if the button sees GPIO17_ON it gets changed to GPIO17_off
        led17.on()                        #This line turns on thr LED
    else:                                 #if the button does not say GPIO17_ON then it must say GPIO17_OFF 
        button1.text="GPIO17_ON "         #this line changes the GPIO17_OFF to GPIO17ON 
        led17.off()                       #this turns off the LED
        
if __name__ == '__main__':
    app = App("Activation GPIO")          #this names the app "activation gpio
    
    button1 = PushButton(app, command=GPIO_17, text="GPIO17_ON ")       #this line calls on the GPIO_17 function
    app.display()                                                       #this function is a loop that opens up the window
    led17.off()                           #this turns off the LED                                                     