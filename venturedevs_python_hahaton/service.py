# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from pathlib import Path
import os
import csv

from .settings import FORECASTS_DIR, API_URL, FIELDS_ORDER


def get_forecasts_from_api(woeid):
    """
    Funkcja wykorzystująca moduł 'requests' do pobrania danych pogodowych
    po HTTP.

    Jeżeli kod odpowiedzi z API wynosi 404, to funkcja powinna zwrócić 
    wartość 'None'. W każdym innym przypadku funkcja powinna zwrócić obiekt
    typu 'dict' z zawartości odpowiedzi.
    """
    response = requests.get("{api_url}/api/location/{woeid}/".format(
        api_url=API_URL,
        woeid=woeid,
    ))
    if response.status_code != 404:
        return response.json()


def forecast_to_list(forecast):
    """
    Funkcja zamieniająca obiekt typu 'dict' odpowiedzi z API na listę list
    danych pogodowych.
    Funkcja korzysta z danych znajdujących się pod kluczem
    'consolidated_weather'.
    """
    try:
        consolidated_weather = forecast['consolidated_weather']
    except KeyError:
        return []
    return [
        [entry[field_name] for field_name in FIELDS_ORDER]
        for entry in consolidated_weather
    ]


def get_forecast_file_path(woeid):
    """
    Funkcja zwracająca krotkę (scieżka_do_katalogu, nazwa_pliku).
    Ścieżka powinna mieć następującą strukturę:
    |- katalog o nazwie 'woeid'
      |
      |- katalog zawierający w nazwie znacznik daty (DD-MM-YYYY)

    Nazwa pliku powinna zawierać znacznik czasu (HH-MM-SS) z
    rozszerzeniem '.csv'.
    """
    now = datetime.now()
    dir_path = os.path.join(str(woeid), now.strftime('%d-%m-%Y'))
    file_name = "{}.csv".format(now.strftime('%H-%M-%S'))
    return dir_path, file_name


def save_forecast(forecast, dir, file_name):
    """
    Funkcja zapisująca obiekt typu 'dict' odpowiedzi z API do pliku 'file_name'
    w katalogu podkatalogu 'dir' katalogu 'FORECASTS_DIR'.

    Przed zapisaniem danych do pliku należy je zamienić za pomocą funkcji
    'forecast_to_list'.

    Jeżeli katalog 'dir' nie istnieje to jest on tworzony w tej funkcji.

    Separatorem w pliku '.csv' powinien być znak tabulacji ('\t').
    """
    if forecast is None:
        return
    forecast_lines = forecast_to_list(forecast)
    path = Path(FORECASTS_DIR) / str(dir)
    path.mkdir(parents=True, exist_ok=True)
    with (path / file_name).open('w', newline='') as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter='\t',
            quotechar='|',
            quoting=csv.QUOTE_MINIMAL
        )
        for forecast_line in forecast_lines:
            writer.writerow(forecast_line)
