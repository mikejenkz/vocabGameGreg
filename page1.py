from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class Page1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a BoxLayout
        self.layout = BoxLayout(orientation='vertical')

        # Create an Image widget for displaying the image
        self.image_widget = Image(source='abound.png', size_hint=(1, 0.9), keep_ratio=True,
                                  allow_stretch=True)

        # Create a BoxLayout for the navigation arrows
        self.nav_layout = BoxLayout(size_hint=(1, 0.1))
        self.nav_layout.add_widget(Button(text='Back', on_release=self.goto_main_menu))
        self.nav_layout.add_widget(Button(text='Forward', on_release=self.goto_next_page))

        # Add the Image widget and navigation layout to the main layout
        self.layout.add_widget(self.image_widget)
        self.layout.add_widget(self.nav_layout)

        # Add the main layout to the screen
        self.add_widget(self.layout)

    def goto_main_menu(self, instance):
        self.manager.current = 'MainMenu'

    def goto_next_page(self, instance):
        # Assuming you have a screen named 'Page2'
        self.manager.current = 'Page2'

