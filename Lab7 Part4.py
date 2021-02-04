from guizero import App, Text
from gpiozero import Button
from gpiozero import LED

button = Button(2)
led = LED(17)

def scanInput():
    if button.is_pressed:
        text.value = 1 #GPIO2 ON
        led.on()
    else:
        text.value = 0 #GPIO2 OFF
        led.off()

def exitGUI():
    
    text.destroy()
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        print("Adios")
        
if __name__ == "__main__":
    
    app = App("Reading Gpio")
    text = Text(app, text="1")
    text.repeat(10, scanInput)
    app.when_closed = exitGUI
    app.display()