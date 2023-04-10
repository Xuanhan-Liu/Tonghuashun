import yaml
from lxml import etree
import re


class Parser:
    def __init__(self):
        self.content = None

    def load_content(self, content):
        self.content = content

    def validation_re(self, key_element):
        pattern = re.compile(key_element)
        if pattern.search(self.content):
            return False
        else:
            return True

    def load_config(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    def parse_element(self, element, rules):
        result = {}
        for rule in rules:
            name = rule['name']
            xpath = rule['xpath']
            children = rule.get('children', [])
            elements = element.xpath(xpath)
            if children:
                result[name] = [self.parse_element(child, children) for child in elements if elements]
            else:
                if name not in result:
                    result[name] = []
                    for el in elements:
                        text = re.sub(r'[\r\t\n' ']', '', el.text)
                        text = text.strip()
                        if text:
                            result[name].append(text)
        return result

    def parse_html(self, file_path):
        self.config = self.load_config(file_path)
        tree = etree.HTML(self.content)
        result = self.parse_element(tree, self.config['rules'])
        return result
