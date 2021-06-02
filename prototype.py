import requests
from bs4 import BeautifulSoup

class Report:
    def create_report(self):
        return None

    def read_report(self, url):
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        return f'{soup.title}'

    def convert_report_to_xml(self):
        return None
