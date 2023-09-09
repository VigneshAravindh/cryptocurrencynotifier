import time
from _ast import BitOr

from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

# import time

import good
from good import main


class Boxlayoutexample(BoxLayout):
    chatid = StringProperty("Not Started")
    choice= StringProperty(" ")
    threshold=StringProperty( " ")


    def openweb(self):
        import  webbrowser
        webbrowser.open('http://t.me/cyptocu_bot')


    def on_toggle_button(self, widget):

        if widget.state == "normal":
            widget.text = "Start"


        else:
            widget.text = "Stop"


            main()


    def update_chatid(self, widget):
        self.chatid = widget.text
        good.ChatId = self.chatid
    def update_choice(self, widget):
        self.choice=widget.text
        good.coin=int(self.choice)

    def update_threshold(self, widget):
        self.threshold= widget.text
        good.threshold= int(self.threshold)


class BitcoinNotifier(App):
    pass


BitcoinNotifier().run()
