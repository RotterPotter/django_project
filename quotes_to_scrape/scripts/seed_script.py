import json
from bs4 import BeautifulSoup
import os
import json
import sys
# sys.path.insert(1, f'{os.getcwd()}/quotes_to_scrap')
from quotes_app.models import Author, Tag, Quote


QUANTITY = 15
DATA_FOLDER = f'{os.getcwd()}/scripts/data'


def scrap_data(url:str):
    pass


def main():
    Tag.objects.all().delete()
    Author.objects.all().delete()
    Quote.objects.all().delete()

if __name__ == '__main__':
    pass

