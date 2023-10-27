from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color


class ColoredButton(Button):
    def __init__(self, image_source, **kwargs):
        super().__init__(**kwargs)
        self.image_source = image_source
        self.draw_background()

    def draw_background(self):
        with self.canvas.before:
            Color(128 / 255, 0, 128 / 255, 1)  # RGB values for purple
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button_layout = BoxLayout(size_hint_y=0.25)

        self.add_button(button_layout, 'Navigate', 'abound.png', self.goto_page1)
        self.add_button(button_layout, 'Study', 'image2.png', self.goto_page2)
        self.add_button(button_layout, 'Test', 'image3.png', self.goto_page3)

        layout.add_widget(BoxLayout(size_hint_y=0.75))  # Filler space
        layout.add_widget(button_layout)  # Buttons at bottom

        self.add_widget(layout)

    def add_button(self, layout, text, image_source, on_release):
        button_box = BoxLayout(orientation='vertical', padding=[60, 60, 60, 60])
        button = ColoredButton(image_source, text=text, on_release=on_release, size_hint_y=0.7, color=[50, 50, 50, 50])
        #button.add_widget(Image(source=image_source, size_hint_y=0.5, allow_stretch=True))
        button_box.add_widget(button)
        layout.add_widget(button_box)

    def goto_page1(self, instance):
        print('Navigating to Page 1')

    def goto_page2(self, instance):
        print('Navigating to Page 2')

    def goto_page3(self, instance):
        print('Navigating to Page 3')


class MyApp(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    MyApp().run()

    #def goto_page1(self, instance):
    #    self.manager.current = 'Page1'
