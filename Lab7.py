from guizero import App, Text, Picture

def exitGUI():
    
    text.destroy()
    if app.yesno("Close", "Do you want to quit?"):     #this line opens a yesno window asking the user if they wish to close the window
        app.destroy()                                  #this line destroys the app when yes is selected
        print("Adios")

app = App(title = "Wanted", height = 350, width = 580) #this line sets up the window title and the window dimentions
app.bg = "red"                                         #this line sets the window background to red
Wanted_text = Text(app,"DRAGON")                       #this line puts a text line in the windopw saying dragon
Wanted_text.text_size = 50                             #this line sets the font size
Wanted_text.font = "Comic Sans MS"                     #this line sets the font
cat = Picture(app, image = "dragon gif")               #this line sets an image into the window
app.display()                                          #this line is a loop that keeps the window open
