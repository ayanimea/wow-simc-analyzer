import requests
from bs4 import BeautifulSoup

class SimulationRange():
    def __init__(self, character):
        self._simulations = []
        self.character = character
        return None

    @property
    def simulations(self):
        return self._simulations

    @simulations.setter
    def simulations(self, new_simulation):
        if not isinstance(new_simulation, Report):
            raise AttributeError("Wrong type: {type(new_simulation}) instead of Report")
        
        self._simulations.append(new_simulations)

class Report():
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
