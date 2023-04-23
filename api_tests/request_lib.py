import requests
from requests import Response

class Client:
    @staticmethod
    def custom_request(method: str, url: str, **kwargs) -> Response:
        """
        function create a response using requests library
        :param method: methods for request like GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        :param url: url for request
        :param kwargs: params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        :return: returns an Response object
        """
        return requests.request(method, url, **kwargs)