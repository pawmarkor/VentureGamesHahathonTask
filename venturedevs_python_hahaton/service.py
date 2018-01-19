import requests
from datetime import datetime
import os
import csv

from .settings import FORECASTS_DIR, API_URL


def get_forecasts_from_api(woeid):
    """
    Funkcja wykorzystująca moduł 'requests' do pobrania danych pogodowych
    po HTTP.

    Jeżeli kod odpowiedzi z API wynosi 404, to funkcja powinna zwrócić 
    wartość 'None'. W każdym innym przypadku funkcja powinna zwrócić obiekt
    typu 'dict' z zawartości odpowiedzi.
    """
    pass


def forecast_to_list(forecast):
    """
    Funkcja zamieniająca obiekt typu 'dict' odpowiedzi z API na listę list
    danych pogodowych.
    Funkcja korzysta z danych znajdujących się pod kluczem
    'consolidated_weather'.
    """
    pass


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
    pass


def save_forecast(forecast, dir, file_name):
    """
    Funkcja zapisująca obiekt typu 'dict' odpowiedzi z API do pliku 'file_name'
    w katalogu 'dir'.

    Przed zapisaniem danych do pliku należy je zamienić za pomocą funkcji
    'forecast_to_list'.

    Jeżeli katalog 'dir' nie istnieje to jest on tworzony w tej funkcji.

    Separatorem w pliku '.csv' powinien być znak tabulacji ('\t').
    """
    pass
