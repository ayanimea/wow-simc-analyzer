import requests
from bs4 import BeautifulSoup

class Report:
    def __init__(self, url):
        self.url = url 

    def create_report(self):
        return None

    def read_report(self):
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        return f'{soup.title}'

    def convert_report_to_xml(self):
        return None

if __name__="__MAIN__":
    url_test = "https://www.raidbots.com/simbot/report/w55rdJY7HwiAjqkmWJzxGU" 
    report = Report(url_test)
