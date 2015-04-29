import kivy
kivy.require("1.9.0")

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainMenu(GridLayout):

    def __init__(self, **kwargs):
        super(MainMenu,self).__init__(**kwargs)
        self.cols = 2
        self.create = Button(text="Create")
        self.add_widget(self.create)
        self.maintain = Button(text="Maintain")
        self.add_widget(self.maintain)
        self.play = Button(text="Play")
        self.add_widget(self.play)
        self.gamemaster = Button(text="GameMaster")
        self.add_widget(self.gamemaster)
