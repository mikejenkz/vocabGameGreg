from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Menu Item 1', on_release=self.goto_page1))
        layout.add_widget(Button(text='Menu Item 2'))
        layout.add_widget(Button(text='Menu Item 3'))
        self.add_widget(layout)

    def goto_page1(self, instance):
        self.manager.current = 'Page1'
