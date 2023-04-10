from SeleniumHandler import Selenium_Handler
from Parser import Parser

handler = Selenium_Handler('/Users/macintosh/Downloads/chromedriver_mac_arm64/chromedriver')
content = handler.load_content('http://www.bankofdl.com/home/pc/gywm/cggg/list_2.shtml',
                               '//div[@class="sell_list_rgt"]')
parser = Parser(content)
print(parser.parse_html('xpath/bankofdl.yaml'))