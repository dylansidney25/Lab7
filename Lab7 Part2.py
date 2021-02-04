from guizero import App, Text, Box, PushButton
def do_nothing():
    return 0
app = App(title="myapp", height=450, width=800, layout="grid")   #this line sets up the window title and the window dimentions
text = Text(app, text="Some text here", grid=[0,0])              #this line sets a test line in the window in a specified grid location
box = Box(app, layout = "grid", grid=[1,0])                      #this line creates a box that will later contain buttons within a grid

button1 = PushButton(box, command=do_nothing, text="1", grid=[0,0])   #these lines set the buttons to call on the do nothing function when pressed
button2 = PushButton(box, command=do_nothing, text="2", grid=[1,0])
button3 = PushButton(box, command=do_nothing, text="3", grid=[2,0])
button4 = PushButton(box, command=do_nothing, text="4", grid=[0,1])
button5 = PushButton(box, command=do_nothing, text="5", grid=[1,1])
button6 = PushButton(box, command=do_nothing, text="6", grid=[2,1])
app.diplay()