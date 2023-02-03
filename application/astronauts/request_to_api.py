from http import HTTPStatus

import requests

from application.logging.loggers import get_core_logger


def get_astronauts():
    logger = get_core_logger()
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url,)

    if response.status_code not in (HTTPStatus.OK,):
        return response("ERROR: Something went wrong", status=response.status_code)

