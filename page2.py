from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image

class Page2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a BoxLayout for the entire screen
        self.layout = BoxLayout(orientation='vertical')

        # Create an AnchorLayout for the Home button
        home_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, 0.1))
        home_button = Button(text='Home', size_hint=(0.2, 0.2), on_release=self.goto_main_menu)
        home_layout.add_widget(home_button)

        # Create an Image widget for displaying the image
        self.image_widget = Image(source='path_to_your_image.jpg', size_hint=(1, 0.8), keep_ratio=True, allow_stretch=True)

        # Create a BoxLayout for the navigation arrows
        self.nav_layout = BoxLayout(size_hint=(1, 0.1))
        back_button = Button(text='Back', background_color=(2, 2, 2, 1), on_release=self.goto_previous_page)
        forward_button = Button(text='Forward', background_color=(2, 2, 2, 1), on_release=self.goto_next_page)
        self.nav_layout.add_widget(back_button)
        self.nav_layout.add_widget(forward_button)

        # Add the Home layout, Image widget, and navigation layout to the main layout
        self.layout.add_widget(home_layout)
        self.layout.add_widget(self.image_widget)
        self.layout.add_widget(self.nav_layout)

        # Add the main layout to the screen
        self.add_widget(self.layout)

    def goto_main_menu(self, instance):
        self.manager.current = 'MainMenu'

    def goto_previous_page(self, instance):
        self.manager.current = 'Page1'

    def goto_next_page(self, instance):
        # Assuming you have a screen named 'Page3'
        self.manager.current = 'Page3'

