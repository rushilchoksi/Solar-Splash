from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.label import Label
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.properties import StringProperty

Window.size = (400, 650)
mainDict = {'clientID': 1, 'timePeriod': 30000, 'dayInterval': 10}

class DemoApp(MDApp):
    pass

class Screen1(Screen):
    frequency = StringProperty("")
    def textInput(self, widget):
        self.frequency = widget.text

    def onClick(self):
        self.textInput(self.ids.text_field)
        self.getConfigurations()

    def getConfigurations(self):
        if self.frequency == '*':
            mainDict['cron'] = '0 6 * * *'
        else:
            configDict = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday', '7': 'Sunday'}
            mainDict['cron'] = f'0 6 * * {",".join(self.frequency.split(","))}'

        print(mainDict)

if __name__ == "__main__":
    DemoApp().run()
