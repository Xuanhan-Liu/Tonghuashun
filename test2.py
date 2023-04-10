from Downloader import Downloader
from Parser import Parser

downloader = Downloader('https://wsgg.sbj.cnipa.gov.cn:9443/tmann/annInfoView/homePage.html')

content = downloader.download(decode=True)['content']
parser = Parser()
parser.load_content(content)
print(parser.parse_html('xpath/wsgg.yaml'))
