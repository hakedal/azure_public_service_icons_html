import sys, os
from xml.etree import ElementTree as ET

folder = os.path.join('Azure_Public_Service_Icons', 'Icons')

html = ET.Element('html')
html.append(ET.Element('meta', attrib={'charset': 'UTF-8'}))
html.append(ET.Element('meta', attrib={'name': 'viewport', 'content': 'width=device-width', 'initial-scale': '1.0'}))
body = ET.Element('body')
html.append(body)
h1 = ET.Element('h1')
h1.text = folder
body.append(h1)

for sub_folder in os.listdir(folder):
    div = ET.Element('div')
    body.append(div)
    h2 = ET.Element('h2')
    h2.text = sub_folder
    div.append(h2)
    for svg_file in os.listdir(os.path.join(folder, sub_folder)):
        src = os.path.join(folder, sub_folder, svg_file)
        div.append(ET.Element('img', attrib={'src': src, 'alt': src, 'title': src, 'style': 'width:54px;height:54px;'}))

ET.ElementTree(html).write(sys.stdout, encoding='unicode', method='html')
