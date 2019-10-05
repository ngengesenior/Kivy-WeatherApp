from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class Item(BoxLayout):
    week_day = ObjectProperty(None)
    tmp = ObjectProperty(None)
    condition_img = ObjectProperty(None)
    day_date = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)



class ForecastItemApp(App):
    def build(self):
        return Item()


if __name__ == '__main__':
    ForecastItemApp().run()
