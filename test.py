from Downloader import Downloader
from Parser import Parser
from SeleniumHandler import Selenium_Handler
import re

if __name__ == '__main__':
    url = ''
    key_element = ''
    downloader = Downloader(url)
    parser = Parser()
    handler = Selenium_Handler('', headless=False)

    code, content = downloader.download(decode=True)
    if code != 200:
        content = handler.load_content(url, key_element)

    parser.load_content(content)
    if parser.validation_re(''):
        content = handler.slider_load(url, '', [48, 48], 300)
        parser.load_content(content)
    print(parser.parse_html('xxx.yaml'))
