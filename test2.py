from Downloader import Downloader
from Parser import Parser

downloader = Downloader('http://www.bankofdl.com/home/pc/gywm/cggg/list_2.shtml')

content = downloader.download(decode=True)['content']
parser = Parser(content)
print(parser.parse_html('xpath/wsgg.yaml'))
