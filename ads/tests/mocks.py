"""
Mock responses
"""

from httpretty import HTTPretty
from .stubdata.solr import example_solr_response
from .stubdata.metrics import example_metrics_response
import json


class HTTPrettyMock(object):
    """
    httpretty context manager scaffolding
    """

    def __enter__(self):
        HTTPretty.enable()

    def __exit__(self, etype, value, traceback):
        """
        :param etype: exit type
        :param value: exit value
        :param traceback: the traceback for the exit
        """
        HTTPretty.reset()
        HTTPretty.disable()


class MockApiResponse(HTTPrettyMock):
    """
    context manager than mocks an static adsws-api response
    """
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint

        HTTPretty.register_uri(
            HTTPretty.GET,
            self.api_endpoint,
            body='''{"status": "online", "app": "adsws.api"}''',
            content_type="application/json",
            adding_headers={
                'X-RateLimit-Limit': 400,
                'X-RateLimit-Remaining': 397,
                'X-RateLimit-Reset': 1436313600
            }
        )


class MockSolrResponse(HTTPrettyMock):
    """
    context manager that mocks a Solr response
    """
    def __init__(self, api_endpoint):
        """
        :param api_endpoint: name of the API end point
        """

        self.api_endpoint = api_endpoint

        def request_callback(request, uri, headers):
            """
            :param request: HTTP request
            :param uri: URI/URL to send the request
            :param headers: header of the HTTP request
            :return: httpretty response
            """

            resp = json.loads(example_solr_response)

            # Mimic the start, rows behaviour
            rows = int(
                request.querystring.get(
                    'rows', [len(resp['response']['docs'])]
                )[0]
            )
            start = int(request.querystring.get('start', [0])[0])
            try:
                resp['response']['docs'] = resp['response']['docs'][start:start+rows]
            except IndexError:
                resp['response']['docs'] = resp['response']['docs'][start:]

            # Mimic the filter "fl" behaviour
            fl = request.querystring.get('fl', ['id'])
            resp['response']['docs'] = [
                {field: doc.get(field) for field in fl}
                for doc in resp['response']['docs']
            ]

            return 200, headers, json.dumps(resp)

        HTTPretty.register_uri(
            HTTPretty.GET,
            self.api_endpoint,
            body=request_callback,
            content_type="application/json"
        )


class MockMetricsResponse(HTTPrettyMock):
    """
    context manager that mocks a metrics service response
    """
    def __init__(self, api_endpoint):
        """
        :param api_endpoint: name of the API end point
        """

        self.api_endpoint = api_endpoint

        HTTPretty.register_uri(
            HTTPretty.POST,
            self.api_endpoint,
            body=example_metrics_response,
            content_type="application/json"
        )
