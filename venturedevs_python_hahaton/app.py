# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException

from .service import (get_forecasts_from_api, get_forecast_file_path,
                      save_forecast)

from .exception_handler import JSONExceptionHandler

APP = Flask(__name__)

handler = JSONExceptionHandler(APP)


@APP.route('/update-forecast/<int:woe_id>', methods=['POST'])
def update_forecast(woe_id):
    """
    Funkcja widoku dostępna pod URI '/update-forecast/:woe_id'.
    Parametr 'woe_id' powinien być liczbą.

    Funkcja ta powinna odpowiadać tylko na zapytania typu 'POST'. W przypadku
    innych zapytań proszę zwrócić odpowiedni kod błędu.

    Widok pobiera dane z API za pomocą funkcji 'get_forecasts_from_api'. Jeżeli
    nie ma danych dla zadanego 'WOEID' to należy zwrócić kod błędu 404. Jeżeli
    wystąpił inny błąd widok powinien zwrócić kod błędu 502.

    Po poprawnym pobraniu danych pogodowych zapisujemy te dane za pomocą 
    funkcji 'save_forecast' i zwracamy kod odpowiedzi 201.
    """
    try:
        forecast = get_forecasts_from_api(woe_id)
        if forecast is None:
            abort(404, 'Weather forecast for given WOEID not found')
        dir, file_name = get_forecast_file_path(woe_id)
        save_forecast(forecast, dir, file_name)
        return jsonify({'updated': 'ok'}), 201
    except HTTPException:
        raise
    except:
        abort(502)
