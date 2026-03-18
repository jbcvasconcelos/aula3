import requests


class Extract:  # a funsão deixa de chamar fusão e agora passa ser chamado de metodo
    def __init__(self):
        pass

    def extract_country(self, country):

        url = f"http://universities.hipolabs.com/search?country={country}"
        response = requests.get(url)
        response.raise_for_status()
        universities = response.json()

        return universities
