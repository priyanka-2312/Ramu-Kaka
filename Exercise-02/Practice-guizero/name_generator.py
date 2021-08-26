# guizero - Hero name generator
from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox
app = App(title="Hero-o-matic")

# Function definitions for your events go here.

def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.value = "You are... The " + hero + "."



# Your GUI widgets go here
message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Enter a colour?")
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal")
cmb_animal = Combo(app, options=["Aardvark", "Badger", "Cat", "Dolphin", "Velociraptor"], selected="Aardvark", width=20)

btn_make_name = PushButton(app, text='Make me a hero')
lbl_output = Text(app, text="A hero name will appear here")

# Set up event triggers here


btn_make_name = PushButton(app, text='Make me a hero', command=make_hero_name)


#Show the GUI on the screen, start listening to events.
app.display()
