from xml.parsers.expat import ParserCreate
from urllib import request

weather_dict = {}
which_day = 0

class WeatherSaxHandler(object):
    def start_element(self,name,attrs):
        global weather_dict,which_day
        if name == 'yweather:location':
            weather_dict['city'] = attrs['city']
            weather_dict['country'] = attrs['country']
        if name == 'yweather:forecast':
            which_day += 1
            if which_day == 1:
                weather = {'text':attrs['text'],
                          'low':int(attrs['low']),
                          'high':int(attrs['high'])
                          }
                weather_dict['today'] =weather
            elif which_day == 2:
                weather = {'text':attrs['text'],
                    'low':int(attrs['low']),
                    'high':int(attrs['high'])
                           }
                weather_dict['tomorrow'] = weather

    def end_element(self, name):
        pass

    # char_data函数
    def char_data(self, text):
        pass


def parseXML(xml_str):
    print(xml_str)
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return weather_dict
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXML(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print('ok')