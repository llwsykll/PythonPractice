from xml.parsers.expat import ParserCreate

# 解析XML
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self,name):
        print('sax:end_element: %s' % name)

    def char_data(self,text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 生成xml
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
# L.append(encode('some & data'))
L.append(r'</root>')


print(L)