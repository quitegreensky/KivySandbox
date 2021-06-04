from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.label import Label

from sandbox import ScreenSandBox

KV = """

<TestButton>
    size_hint: None, None
    size: dp(100), dp(50)
    text: "50dp*30dp"
    font_size: dp(20)


<MySandbox>
    canvas.before:
        Color:
            rgba:  1, 1, 1, 0.4
        Rectangle:
            pos: self.pos
            size: self.size


Screen:

    BoxLayout:
        padding: dp(20)
        spacing: dp(20)
        id: container

        MySandbox:
            id: htc
            screen_width: 1080
            screen_height: 1920
            diagonal_inches: 4.7
            padding: dp(10)
            scale: 0.3
            orientation: "vertical"

        MySandbox:
            id: kindle
            screen_width: 825
            screen_height: 1200
            diagonal_inches: 9.7
            scale: 0.3
            padding: dp(10)
            orientation: "vertical"

"""


class MySandbox(ScreenSandBox):
    pass


class TestButton(Button):
    pass


class TestLabel(Label):
    pass


class MainApp(App):
    def build(self):
        self.main = Builder.load_string(KV)
        return self.main

    def on_start(self):

        with self.root.ids.htc as sandbox:
            # initialize widgets here
            print(dp(1))
            real_dpi = sandbox.dpi()
            height, width = sandbox.screen_height, sandbox.screen_width
            diagonal = sandbox.diagonal_inches
            wid = TestButton()
            label = TestLabel(text=f"{height}*{width} {diagonal} inches {int(real_dpi)} dpi")
            sandbox.add_widget(wid)
            sandbox.add_widget(label)

        with self.root.ids.kindle as sandbox:
            # initialize widgets here
            print(dp(1))
            real_dpi = sandbox.dpi()
            height, width = sandbox.screen_height, sandbox.screen_width
            diagonal = sandbox.diagonal_inches
            wid = TestButton()
            label = TestLabel(text=f"{height}*{width} {diagonal} inches {int(real_dpi)} dpi")
            sandbox.add_widget(wid)
            sandbox.add_widget(label)

        print(dp(1))
        return super().on_start()


MainApp().run()
