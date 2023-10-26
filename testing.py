from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Button(text='Menu Item 1', on_release=self.menu_action))
        self.add_widget(Button(text='Menu Item 2', on_release=self.menu_action))
        self.add_widget(Button(text='Menu Item 3', on_release=self.menu_action))

    def menu_action(self, instance):
        print(f'You selected {instance.text}')


class MenuApp(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    MenuApp().run()

