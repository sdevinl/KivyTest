from kivy.app import App
# kivy.require('1.8.0')
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        # self.cols = 6
        self.rows = 3

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text='Two Factor Auth:'))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)


class SimpleKivy(App):
    sm = ScreenManager()
    sm.add_widget(Screen(name='first'))
    sm.add_widget(Screen(name='second'))

    # By default, the first added screen will be shown. If you want to
    # show another one, just set the 'current' property.
    sm.current = 'second'

    # def build(self):
    #   return LoginScreen()


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        
        
        
        Button:
            text: 'Goto settings'
            on_press: 
                root.manager.transition.direction='left'
                root.manager.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
""")


# Declare both screens
class MenuScreen(Screen):
    layout = BoxLayout(orientation = 'vertical ')
    pass


class SettingsScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
