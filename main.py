from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from main_menu import MainMenu
from page1 import Page1
from page2 import Page2  # Import Page2 class from page2.py

class MenuApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main_menu_screen = MainMenu(name='MainMenu')
        self.page1_screen = Page1(name='Page1')
        self.page2_screen = Page2(name='Page2')  # Create an instance of Page2

        self.screen_manager.add_widget(self.main_menu_screen)
        self.screen_manager.add_widget(self.page1_screen)
        self.screen_manager.add_widget(self.page2_screen)  # Add Page2 to the ScreenManager

        return self.screen_manager

if __name__ == '__main__':
    app = MenuApp()
    app.run()

