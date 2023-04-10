from SeleniumHandler import Selenium_Handler
from Parser import Parser

handler = Selenium_Handler('/Users/macintosh/Downloads/chromedriver_mac64/chromedriver', headless=False)
content = handler.slider_load('https://tingshen.court.gov.cn/live/34448747', '//*[@class="nc_iconfont btn_slide"]',
                              [48, 48], 300)
print(content)
parser = Parser()
print(parser.parse_html('xpath/court.yaml'))
