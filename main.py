from pprint import pprint
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from requests import ConnectionError
from apixu.client import ApixuClient, ApixuException
from forecast import Item

api_key = '7213cd223d104336be8155252172908'


class ConErrorPop(Popup):
    pass


class ApixuBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ApixuBox, self).__init__(**kwargs)


class ScreenManagerWid(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagerWid, self).__init__(**kwargs)


class CurrentWeather(Screen):
    pressure = ObjectProperty(None)
    tmp_value = ObjectProperty(None)
    temperature = ObjectProperty(None)
    humidity = ObjectProperty(None)
    sunrise = ObjectProperty(None)
    visibility = ObjectProperty(None)
    local_time = ObjectProperty(None)
    precipitation = ObjectProperty(None)
    feels = ObjectProperty(None)
    region = ObjectProperty(None)
    country = ObjectProperty(None)
    city = ObjectProperty(None)
    sky_state = ObjectProperty(None)
    wind = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CurrentWeather, self).__init__(**kwargs)

    def getNowWeather(self, place=None):
        try:
            from apixu.client import ApixuClient, ApixuException
            client = ApixuClient(api_key)
            if not place:
                current = client.getCurrentWeather(q='Buea')
            else:
                current = client.getCurrentWeather(q=str(place))
            cur_ = current['current']
            self.pressure.text = str(cur_['pressure_mb']) + ' mb'
            self.tmp_value.text = str(cur_['temp_c']) + u'\u00b0' + ' C'
            self.temperature.text = str(cur_['temp_c']) + u'\u00b0' + ' C'
            self.humidity.text = str(cur_['humidity']) + '%'
            # self.sunrise.text = to be done
            self.visibility.text = str(cur_['vis_km']) + ' Km'
            self.local_time.text = str(current['location']['localtime'])
            self.precipitation.text = str(cur_['precip_mm']) + 'mm'
            self.feels.text = str(cur_['feelslike_c']) + u'\u00b0' + ' C'
            self.region.text = str(current['location']['region'])
            self.country.text = str(current['location']['country'])
            self.sky_state.text = str(cur_['condition']['text'])
            self.wind.text = str(cur_['wind_kph']) + 'kph'
            self.pressure.text = str(cur_['pressure_mb']) + 'mb'
            self.humidity.text = str(cur_['humidity'])

        except ConnectionError:
            ConErrorPop().open()


class ForecastWeather(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ForecastWeather, self).__init__(**kwargs)

    def populate(self):
        for i in range(7):
            print 'Adding itm'
            self.grid.add_widget(Item())


class ApixuApp(App):
    def build(self):
        return ScreenManagerWid()


if __name__ == '__main__':
    ApixuApp().run()
