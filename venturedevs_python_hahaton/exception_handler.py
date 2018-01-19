from flask import jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

# copied from https://coderwall.com/p/xq88zg/json-exception-handler-for-flask


class JSONExceptionHandler(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def std_handler(self, error):
        response = jsonify(message=str(error))
        response.status_code = error.code if isinstance(error, HTTPException) else 502
        return response

    def init_app(self, app):
        self.app = app
        self.register(HTTPException)
        for code, v in default_exceptions.items():
            self.register(code)

    def register(self, exception_or_code, handler=None):
        self.app.errorhandler(exception_or_code)(handler or self.std_handler)
