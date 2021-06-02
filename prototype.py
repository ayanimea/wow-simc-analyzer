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

        return f'{soup.title.encode("utf-8")}'

    def convert_report_to_xml(self):
        return None

if __name__ == "__main__":
    url_test = "https://www.raidbots.com/simbot/report/w55rdJY7HwiAjqkmWJzxGU" 
    report = Report(url_test)
    print(report.read_report())
