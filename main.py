from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window


class MaduraiMessApp(App):
    def build(self):
        # White background
        Window.clearcolor = (1, 1, 1, 1)

        main_layout = BoxLayout(orientation='vertical', padding=25, spacing=20)

        # ---------------- TOP BAR ----------------
        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.25), spacing=15)

        title_label = Label(
            text="Madurai Mess",
            font_size=44,
            bold=True,
            color=(0.90, 0.70, 0.05, 1),  # warm yellow
            size_hint=(0.7, 1),
            halign="left",
            valign="middle"
        )
        title_label.bind(size=title_label.setter('text_size'))

        logo = Image(
            source="Madhurai Mess logo final.png",  # check path
            size_hint=(0.3, 1),
            allow_stretch=True,
            keep_ratio=True
        )

        top_bar.add_widget(title_label)
        top_bar.add_widget(logo)

        # ---------------- WELCOME TEXT ----------------
        welcome = Label(
            text="Purely Authentic South Indian Taste",
            font_size=26,
            bold=True,
            color=(0.15, 0.15, 0.15, 1),
            size_hint=(1, 0.15)
        )

        # ---------------- BUTTONS ----------------
        btn_color = (0.95, 0.75, 0.1, 1)  # yellow
        text_color = (0.1, 0.1, 0.1, 1)   # dark gray

        menu_btn = Button(
            text="View Menu", size_hint=(1, 0.2),
            background_color=btn_color, color=text_color,
            font_size=26, bold=True
        )

        order_btn = Button(
            text="Place Order", size_hint=(1, 0.2),
            background_color=btn_color, color=text_color,
            font_size=26, bold=True
        )

        about_btn = Button(
            text="About Us", size_hint=(1, 0.2),
            background_color=btn_color, color=text_color,
            font_size=26, bold=True
        )

        # Add everything
        main_layout.add_widget(top_bar)
        main_layout.add_widget(welcome)
        main_layout.add_widget(menu_btn)
        main_layout.add_widget(order_btn)
        main_layout.add_widget(about_btn)

        return main_layout


if __name__ == "__main__":
    MaduraiMessApp().run()
